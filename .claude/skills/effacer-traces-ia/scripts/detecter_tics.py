#!/usr/bin/env python3
"""Repère les tics d'écriture typiques des textes générés par IA.

Usage :
    python3 detecter_tics.py FICHIER [FICHIER ...]
    python3 detecter_tics.py DOSSIER          (parcourt les fichiers texte et code)
    echo "texte" | python3 detecter_tics.py -
    python3 detecter_tics.py --bilan DOSSIER  (affiche seulement le bilan)

Code de sortie : 0 si rien n'est trouvé, 1 si des tics sont signalés,
2 en cas d'erreur d'utilisation.

Le script repère des motifs, il ne comprend pas le sens. Chaque signalement
est une piste à vérifier, pas une faute certaine. Ce qu'il ne voit pas
(règle de trois, rythme trop régulier, introduction qui reformule,
commentaires qui répètent le code) reste à relire à la main.
"""

import argparse
import html
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

EXT_MARKDOWN = {".md", ".markdown", ".txt", ".rst"}
EXT_HTML = {".html", ".htm"}
EXT_CODE = {
    ".py", ".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs", ".css", ".scss",
    ".php", ".java", ".kt", ".go", ".rb", ".rs", ".c", ".h", ".cpp", ".cs",
    ".swift", ".sh", ".vue", ".svelte",
}
DOSSIERS_IGNORES = {"node_modules", "__pycache__", "venv", "dist", "build"}

FLAGS = re.IGNORECASE

# Mots-outils français : servent à deviner si une ligne ou un titre est en français.
MOTS_FR = {
    "le", "la", "les", "de", "des", "du", "pour", "ton", "ta", "tes", "votre",
    "vos", "et", "un", "une", "avec", "dans", "en", "à", "au", "aux", "sur",
    "par", "nos", "notre", "mon", "ma", "mes", "son", "sa", "ses", "qui",
    "que", "est", "pas", "ne", "ce", "cette", "nous", "vous", "il", "elle",
}

TIRET_CADRATIN = re.compile("—")
TIRET_DEMI_CADRATIN_ESPACE = re.compile(r"\s–\s")
EMOJI = re.compile(
    "[\U0001F300-\U0001FAFF\U0001F000-\U0001F2FF"
    "☀-➿⬀-⯿⏩-⏺]"
)

# (motif, catégorie, conseil)
MOTIFS_PHRASES = [
    # Ce n'est pas X, c'est Y
    (r"\b(?:ce|ça) n'est pas\b[^.!?\n]{0,80}?,\s*(?:c'est|mais)\b",
     "ce n'est pas X, c'est Y", "affirme directement ce que tu veux dire"),
    (r"\bce n'est pas (?:seulement|que|qu'une?|juste|simplement)\b",
     "ce n'est pas X, c'est Y", "affirme directement ce que tu veux dire"),
    (r"\bil ne s'agit pas\b[^.!?\n]{0,80}?\bmais\b",
     "ce n'est pas X, c'est Y", "affirme directement ce que tu veux dire"),
    (r"\bpas (?:seulement|uniquement|simplement)\b[^.!?\n]{0,80}?\bmais (?:aussi|également)\b",
     "ce n'est pas X, c'est Y", "affirme directement ce que tu veux dire"),
    (r"\bnon seulement\b[^.!?\n]{0,80}?\bmais\b",
     "ce n'est pas X, c'est Y", "affirme directement ce que tu veux dire"),
    (r"\bplus qu'une?\b[^.!?\n]{0,60}?\bvéritable\b",
     "ce n'est pas X, c'est Y", "affirme directement ce que tu veux dire"),
    (r"\b(?:it's|it is|this is|that's) not (?:just |only |merely )?[^.!?\n]{1,60}?[,;]\s*(?:it's|it is|but)\b",
     "ce n'est pas X, c'est Y", "affirme directement ce que tu veux dire"),
    (r"\bnot (?:just|only|merely)\b[^.!?\n]{0,80}?\bbut\b",
     "ce n'est pas X, c'est Y", "affirme directement ce que tu veux dire"),
    # Formules de remplissage
    (r"\bil est (?:important|essentiel|crucial|primordial|intéressant) de (?:noter|souligner|rappeler|comprendre|mentionner)\b",
     "formule de remplissage", "supprime la formule, garde l'information"),
    (r"\bil convient de (?:noter|souligner|rappeler|préciser)\b",
     "formule de remplissage", "supprime la formule, garde l'information"),
    (r"\bforce est de constater\b", "formule de remplissage", "supprime la formule, garde l'information"),
    (r"\bil va sans dire\b", "formule de remplissage", "supprime la formule, garde l'information"),
    (r"\bil est à noter\b", "formule de remplissage", "supprime la formule, garde l'information"),
    (r"\b(?:it's|it is) (?:important|worth|crucial) (?:to note|noting|to mention|to remember)\b",
     "formule de remplissage", "supprime la formule, garde l'information"),
    # Ouvertures grandiloquentes
    (r"\bdans un monde (?:en (?:constante|perpétuelle) évolution|où|qui)\b",
     "ouverture grandiloquente", "commence par le fait concret"),
    (r"\bà l'ère (?:du|de la|des|de l')\b", "ouverture grandiloquente", "commence par le fait concret"),
    (r"\bdans le paysage (?:\w+ )?actuel\b", "ouverture grandiloquente", "commence par le fait concret"),
    (r"\bin today's (?:fast-paced|digital|ever-changing|modern)\b",
     "ouverture grandiloquente", "commence par le fait concret"),
    (r"\b(?:ever-evolving|ever-changing|fast-paced) (?:world|landscape)\b",
     "ouverture grandiloquente", "commence par le fait concret"),
    # Invitations au voyage
    (r"\b(?:plongeons|explorons|embarquons|découvrons ensemble|partons à la découverte)\b",
     "invitation au voyage", "va droit au contenu"),
    (r"\blet's (?:dive|delve|explore)\b", "invitation au voyage", "va droit au contenu"),
    # Que tu sois X ou Y
    (r"\bque (?:tu sois|vous soyez)\b[^.!?\n]{1,50}\bou\b",
     "que tu sois X ou Y", "parle à ton vrai lecteur"),
    (r"\bwhether you're\b[^.!?\n]{1,50}\bor\b", "que tu sois X ou Y", "parle à ton vrai lecteur"),
    # Conclusion qui résume
    (r"\b(?:en résumé|en conclusion|pour récapituler|pour conclure|en somme)\b",
     "conclusion qui résume", "termine sur la dernière info utile ou une action concrète"),
    (r"\b(?:in summary|in conclusion|to sum up|to summarize)\b",
     "conclusion qui résume", "termine sur la dernière info utile ou une action concrète"),
    # Question d'engagement finale
    (r"\bn'hésite(?:z)? pas à\b", "question d'engagement", "supprime-la sauf vraie question ouverte"),
    (r"\bsouhaite(?:s-tu|z-vous) que\b", "question d'engagement", "supprime-la sauf vraie question ouverte"),
    (r"\b(?:veux-tu|voulez-vous) que je\b", "question d'engagement", "supprime-la sauf vraie question ouverte"),
    (r"\bj'espère que (?:cela|ça|ceci) (?:t'|vous |)aide", "question d'engagement", "supprime la phrase"),
    (r"\b(?:feel free to|i hope this helps|let me know if you)\b",
     "question d'engagement", "supprime-la sauf vraie question ouverte"),
    # Flatterie
    (r"\b(?:excellente|très bonne|bonne) question\b", "flatterie", "réponds directement"),
    (r"\bquelle (?:idée|question) (?:brillante|excellente|géniale)\b", "flatterie", "réponds directement"),
    (r"\b(?:tu as|vous avez) (?:tout à fait|entièrement|parfaitement) raison\b", "flatterie", "réponds directement"),
    (r"\b(?:great|excellent) question\b", "flatterie", "réponds directement"),
    (r"\byou're absolutely right\b", "flatterie", "réponds directement"),
    # Disclaimers inutiles
    (r"\ben tant qu'(?:ia|intelligence artificielle|assistant|modèle de langage)\b",
     "disclaimer inutile", "supprime-le"),
    (r"\bje ne suis pas en mesure de\b", "disclaimer inutile", "supprime-le si la question est simple"),
    (r"\b(?:il est recommandé|je (?:te|vous) recommande) de consulter un (?:professionnel|spécialiste|expert)\b",
     "disclaimer inutile", "supprime-le si la question est simple"),
    (r"\bas an ai\b", "disclaimer inutile", "supprime-le"),
    # Neutralité molle
    (r"\b(?:les deux|chaque) (?:approches?|options?|solutions?|méthodes?) (?:ont|a) (?:leurs|ses) (?:avantages|forces|atouts)\b",
     "neutralité molle", "donne une recommandation claire et sa condition"),
    (r"\btout dépend de (?:tes|vos) besoins\b", "neutralité molle", "donne une recommandation claire et sa condition"),
    # Précautions en cascade
    (r"\bpotentiellement\b", "précautions en cascade", "affirme, en précisant le cas"),
    (r"\bpourrait (?:éventuellement|potentiellement)\b", "précautions en cascade", "affirme, en précisant le cas"),
    (r"\bdans une certaine mesure\b", "précautions en cascade", "affirme, en précisant le cas"),
    (r"\bcould potentially\b", "précautions en cascade", "affirme, en précisant le cas"),
]

MOTS_GONFLES = [
    (r"crucia(?:l|le|les|ux)", "important, ou rien du tout"),
    (r"essentiel(?:le)?s?", "important, ou rien du tout"),
    (r"primordia(?:l|le|les|ux)", "important, ou rien du tout"),
    (r"incontournables?", "utile, connu, très utilisé"),
    (r"robustes?", "fiable, solide"),
    (r"fluides?", "simple, facile à utiliser (sauf sens propre)"),
    (r"fluidité", "simplicité"),
    (r"intuiti(?:f|ve|fs|ves)", "simple, facile à utiliser"),
    (r"optimis\w*", "améliorer, accélérer"),
    (r"maximis\w*", "améliorer, augmenter"),
    (r"leviers?", "un moyen"),
    (r"révolution\w*", "changer"),
    (r"au c(?:œ|oe)ur d(?:e|u|es|')", "dans, au centre de"),
    (r"témoign\w* d(?:e|u|es|')", "montre"),
    (r"écosystèmes?", "le marché, le secteur, les outils"),
    (r"paysages?", "le marché, le secteur (sauf sens littéral)"),
    (r"navigu\w*", "gérer, s'en sortir (sauf sens propre)"),
    (r"boost\w*", "augmenter"),
    (r"game[\s-]?changers?", "un vrai changement"),
    # Enthousiasme permanent
    (r"incroyables?", "garde les superlatifs pour ce qui les mérite"),
    (r"puissante?s?", "garde les superlatifs pour ce qui les mérite"),
    (r"fascinante?s?", "garde les superlatifs pour ce qui les mérite"),
    (r"extraordinaires?", "garde les superlatifs pour ce qui les mérite"),
    (r"véritables?", "souvent inutile, supprime-le"),
    # Anglais
    (r"delv\w*", "look at, examine"),
    (r"robust", "reliable, solid"),
    (r"seamless(?:ly)?", "simple, smooth"),
    (r"leverag\w*", "use"),
    (r"cutting-edge", "new, recent"),
    (r"groundbreaking", "new"),
    (r"pivotal", "important"),
    (r"tapestry", "mix"),
    (r"testament to", "shows"),
    (r"empower\w*", "help, let"),
]

MOTIFS_PHRASES_C = [(re.compile(m, FLAGS), cat, conseil) for m, cat, conseil in MOTIFS_PHRASES]
MOTS_GONFLES_C = [(re.compile(r"\b" + m + r"\b", FLAGS), conseil) for m, conseil in MOTS_GONFLES]

NOMS_GENERIQUES = re.compile(
    r"\b(?:const|let|var|def|function|val|auto)\s+"
    r"(data|result|results|item|items|temp|tmp|info|obj|handleData|processData|processInfo|doStuff)\b"
    r"|\bclass\s+(DataManager|Manager|Helper|Helpers|Utils?)\b"
    r"|^\s*(data|result|temp|tmp)\s*=[^=]"
)
FICHIERS_GENERIQUES = {"utils", "util", "helpers", "helper", "misc"}
ERREUR_GENERIQUE = re.compile(
    r"[\"'](?:An error occurred|An unexpected error occurred|Something went wrong|"
    r"Une erreur est survenue|Une erreur s'est produite)",
    FLAGS,
)
CODE_EN_LIGNE = re.compile(r"`[^`]*`")
GRAS = re.compile(r"\*\*[^*\n]+\*\*|__[^_\n]+__")
GUILLEMETS_ANGLAIS = re.compile(r"\"[^\"\n]{1,80}\"|“[^”\n]{1,80}”")
TITRE_MD = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$")
TITRE_HTML = re.compile(r"<h[1-6][^>]*>(.*?)</h[1-6]>", re.IGNORECASE)
QUESTION_REPONSE = re.compile(
    r"(?:^|[.!?]\s+)((?:[\w'-]+\s+){0,3}[\w'-]+)\s?\?\s+([A-ZÀ-ÖØ-Þ][^.?!\n]{0,60}[.!])"
)
DEUX_POINTS = re.compile(r"^\W*([\w'-]+(?:\s+[\w'-]+){0,3})\s?:\s+([\w'-]+(?:\s+[\w'-]+)?)\s*[.!]$")
SEPARATEUR_PHRASES = re.compile(r"(?<=[.!?])\s+")


@dataclass
class Signalement:
    chemin: str
    ligne: int
    categorie: str
    extrait: str
    conseil: str


def normaliser(texte):
    """Uniformise les apostrophes pour que les motifs couvrent ' et ’."""
    return texte.replace("’", "'").replace("ʼ", "'")


def extrait_autour(texte, debut, fin, marge=25):
    a = max(0, debut - marge)
    b = min(len(texte), fin + marge)
    morceau = texte[a:b].strip()
    if a > 0:
        morceau = "…" + morceau
    if b < len(texte):
        morceau = morceau + "…"
    return morceau


def semble_francais(texte):
    mots = re.findall(r"[\wà-ÿ']+", texte.lower())
    return sum(1 for m in mots if m in MOTS_FR) >= 2


def titre_en_majuscules(titre):
    mots = re.findall(r"[\wÀ-ÿ'-]+", titre)
    if len(mots) < 3:
        return False
    if not any(m.lower() in MOTS_FR for m in mots):
        return False
    suivants = [m for m in mots[1:] if m[0].isalpha() and not m.isupper() and not any(c.isdigit() for c in m)]
    if len(suivants) < 2:
        return False
    majuscules = sum(1 for m in suivants if m[0].isupper())
    return majuscules >= 2 and majuscules / len(suivants) >= 0.6


class Analyseur:
    def __init__(self, chemin_affiche):
        self.chemin = chemin_affiche
        self.signalements = []
        self._vus = set()

    def ajouter(self, ligne, categorie, extrait, conseil):
        cle = (ligne, categorie, extrait)
        if cle in self._vus:
            return
        self._vus.add(cle)
        self.signalements.append(Signalement(self.chemin, ligne, categorie, extrait, conseil))

    def verifier_universel(self, num, texte):
        """Contrôles valables partout, y compris dans le code."""
        for m in TIRET_CADRATIN.finditer(texte):
            self.ajouter(num, "tiret cadratin", extrait_autour(texte, m.start(), m.end()),
                         "virgule, deux points, parenthèses ou point")
        for m in TIRET_DEMI_CADRATIN_ESPACE.finditer(texte):
            self.ajouter(num, "tiret demi-cadratin", extrait_autour(texte, m.start(), m.end()),
                         "virgule, deux points, parenthèses ou point")
        m = EMOJI.search(texte)
        if m:
            self.ajouter(num, "émoji", extrait_autour(texte, m.start(), m.end()),
                         "aucun émoji dans les titres, la doc, le code ou les commits")

    def verifier_code(self, num, texte):
        m = NOMS_GENERIQUES.search(texte)
        if m:
            nom = next(g for g in m.groups() if g)
            self.ajouter(num, "nom générique", nom, "nomme selon le métier (pendingOrders, computeTaxAmount)")
        m = ERREUR_GENERIQUE.search(texte)
        if m:
            self.ajouter(num, "erreur générique", extrait_autour(texte, m.start(), m.end()),
                         "gère l'erreur là où elle peut arriver, avec un traitement utile")

    def verifier_vocabulaire(self, num, texte):
        texte = normaliser(texte)
        categories_vues = set()
        for motif, categorie, conseil in MOTIFS_PHRASES_C:
            if categorie in categories_vues:
                continue
            m = motif.search(texte)
            if m:
                categories_vues.add(categorie)
                self.ajouter(num, categorie, extrait_autour(texte, m.start(), m.end(), 10), conseil)
        for motif, conseil in MOTS_GONFLES_C:
            for m in motif.finditer(texte):
                self.ajouter(num, "mot gonflé", m.group(0), conseil)

    def verifier_prose(self, num, texte):
        """Contrôles de style sur du texte rédigé (hors code)."""
        texte = normaliser(CODE_EN_LIGNE.sub("", texte))
        self.verifier_vocabulaire(num, texte)

        titre = TITRE_MD.match(texte)
        if titre and titre_en_majuscules(titre.group(1)):
            self.ajouter(num, "majuscules dans le titre", titre.group(1),
                         "en français, majuscule au premier mot seulement")

        if semble_francais(texte):
            for m in GUILLEMETS_ANGLAIS.finditer(texte):
                self.ajouter(num, "guillemets anglais", m.group(0), "en français, utilise « »")

        phrases = [p.strip() for p in SEPARATEUR_PHRASES.split(texte.strip()) if p.strip()]
        serie = []
        for phrase in phrases + [""]:
            nb_mots = len(phrase.split())
            if phrase and phrase[-1] in ".!" and 1 <= nb_mots <= 2:
                serie.append(phrase)
                continue
            if len(serie) >= 3:
                self.ajouter(num, "fragments en rafale", " ".join(serie),
                             "fais une vraie phrase (« C'est simple et ça va vite. »)")
            serie = []
        for phrase in phrases:
            m = DEUX_POINTS.match(phrase)
            if m and not phrase.lstrip().startswith(("#", "-", "*", "|")):
                self.ajouter(num, "deux-points dramatiques", phrase, "écris la phrase en entier")

        for m in QUESTION_REPONSE.finditer(texte):
            self.ajouter(num, "question rhétorique", extrait_autour(texte, m.start(1), m.end(2), 0),
                         "affirme directement (« Le plus important, c'est… »)")

    def verifier_gras(self, num_debut, paragraphe):
        nb = len(GRAS.findall(CODE_EN_LIGNE.sub("", paragraphe)))
        if nb > 1:
            self.ajouter(num_debut, "gras partout", f"{nb} passages en gras dans le paragraphe",
                         "un seul gras par paragraphe au maximum")


def analyser_markdown(analyseur, lignes):
    dans_code = False
    paragraphe, debut_paragraphe = [], 0
    for num, ligne in enumerate(lignes, 1):
        if re.match(r"^\s*(```|~~~)", ligne):
            dans_code = not dans_code
            continue
        analyseur.verifier_universel(num, ligne)
        if dans_code:
            analyseur.verifier_code(num, ligne)
            continue
        analyseur.verifier_prose(num, ligne)
        if ligne.strip():
            if not paragraphe:
                debut_paragraphe = num
            paragraphe.append(ligne)
        else:
            analyseur.verifier_gras(debut_paragraphe, " ".join(paragraphe))
            paragraphe = []
    if paragraphe:
        analyseur.verifier_gras(debut_paragraphe, " ".join(paragraphe))


def analyser_html(analyseur, lignes):
    dans_balise = False
    dans_script = False
    for num, ligne in enumerate(lignes, 1):
        analyseur.verifier_universel(num, ligne)
        bas = ligne.lower()
        if dans_script or "<script" in bas or "<style" in bas:
            if re.search(r"<(script|style)\b", bas):
                dans_script = True
            if re.search(r"</(script|style)>", bas):
                dans_script = False
            analyseur.verifier_code(num, ligne)
            continue
        for m in TITRE_HTML.finditer(ligne):
            titre = html.unescape(re.sub(r"<[^>]*>", "", m.group(1))).strip()
            if titre_en_majuscules(titre):
                analyseur.ajouter(num, "majuscules dans le titre", titre,
                                  "en français, majuscule au premier mot seulement")
        texte = []
        for car in ligne:
            if dans_balise:
                if car == ">":
                    dans_balise = False
                continue
            if car == "<":
                dans_balise = True
                texte.append(" ")
                continue
            texte.append(car)
        visible = html.unescape("".join(texte)).strip()
        if visible:
            analyseur.verifier_prose(num, visible)


def analyser_code(analyseur, lignes):
    for num, ligne in enumerate(lignes, 1):
        analyseur.verifier_universel(num, ligne)
        analyseur.verifier_code(num, ligne)
        analyseur.verifier_vocabulaire(num, ligne)


def analyser_texte(chemin_affiche, contenu, extension):
    analyseur = Analyseur(chemin_affiche)
    lignes = contenu.splitlines()
    if extension in EXT_HTML:
        analyser_html(analyseur, lignes)
    elif extension in EXT_CODE:
        analyser_code(analyseur, lignes)
        if Path(chemin_affiche).stem.lower() in FICHIERS_GENERIQUES:
            analyseur.ajouter(0, "nom générique", Path(chemin_affiche).name,
                              "nomme le fichier selon le métier (invoiceFormatter.js)")
    else:
        analyser_markdown(analyseur, lignes)
    return analyseur.signalements


def lister_fichiers(cible):
    if cible.is_file():
        yield cible
        return
    for chemin in sorted(cible.rglob("*")):
        relatif = chemin.relative_to(cible).parts
        if any(p.startswith(".") or p in DOSSIERS_IGNORES for p in relatif[:-1]):
            continue
        if chemin.is_file() and chemin.suffix.lower() in EXT_MARKDOWN | EXT_HTML | EXT_CODE:
            yield chemin


def main(argv=None):
    parseur = argparse.ArgumentParser(description="Repère les tics d'écriture typiques de l'IA.")
    parseur.add_argument("cibles", nargs="+", help="fichiers, dossiers, ou - pour lire l'entrée standard")
    parseur.add_argument("--bilan", action="store_true", help="n'affiche que le bilan par catégorie")
    args = parseur.parse_args(argv)

    signalements = []
    nb_fichiers = 0
    for cible in args.cibles:
        if cible == "-":
            signalements += analyser_texte("<entrée>", sys.stdin.read(), ".md")
            nb_fichiers += 1
            continue
        chemin = Path(cible)
        if not chemin.exists():
            print(f"Introuvable : {cible}", file=sys.stderr)
            return 2
        for fichier in lister_fichiers(chemin):
            contenu = fichier.read_text(encoding="utf-8", errors="replace")
            signalements += analyser_texte(str(fichier), contenu, fichier.suffix.lower())
            nb_fichiers += 1

    if not args.bilan:
        for s in signalements:
            print(f"{s.chemin}:{s.ligne}: [{s.categorie}] « {s.extrait} » -> {s.conseil}")

    if not signalements:
        print(f"Aucun tic détecté dans {nb_fichiers} fichier(s). Relis quand même à la main : "
              "règle de trois, rythme, introduction et conclusion ne se détectent pas automatiquement.")
        return 0

    fichiers_touches = len({s.chemin for s in signalements})
    print(f"\nBilan : {len(signalements)} signalement(s) dans {fichiers_touches} fichier(s) "
          f"sur {nb_fichiers} analysé(s).")
    for categorie, nb in Counter(s.categorie for s in signalements).most_common():
        print(f"  {nb:4d}  {categorie}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
