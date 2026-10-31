---
name: effacer-traces-ia
description: Recense et efface les marques d'un texte ou d'un site généré par IA (tiret cadratin, « ce n'est pas X, c'est Y », règle de trois, mots gonflés, langage de brochure, importance gonflée, attributions vagues, chiffres sans source, émojis en guise d'icônes, gras partout, gabarits oubliés comme [Votre nom], artefacts comme utm_source=chatgpt.com, phrases de chatbot, flatterie, conclusion qui résume) dans les textes, pages web, documentations, README, commentaires de code, commits, e-mails et contenus marketing. Utilise-le systématiquement dès que tu rédiges, relis ou corriges un texte ou un site à publier, envoyer ou commiter, en français comme en anglais, et quand l'utilisateur demande d'humaniser un texte, d'enlever les traces d'IA, de nettoyer un site ou de vérifier qu'un texte « ne fait pas IA », même sans citer l'IA.
---

# Effacer les traces d'IA

Sources : guide « Les tics de l'IA : la liste complète » de MEZES Corporation, complété par la page Wikipedia « Signs of AI writing », l'étude Kobak et al. sur le vocabulaire en excès et des analyses de sites générés par IA. Deux fichiers donnent le détail avec des exemples avant/après :

- `references/guide-complet.md` : les tics du guide MEZES (ponctuation, structure, tournures, vocabulaire, ton, code).
- `references/autres-marques.md` : les autres marques (importance gonflée, langage de brochure, participe présent de commentaire, attributions vagues, chiffres sans source, artefacts de copier-coller, gabarits oubliés, marques propres aux sites web, code).

Lis-les quand tu as un doute sur un cas précis, et toujours avant de corriger un site complet.

## Le principe

Aucun de ces signes ne prouve à lui seul qu'un texte vient d'une IA. Les écrivains utilisent le tiret cadratin depuis des siècles et beaucoup d'humains aiment les listes. C'est l'accumulation et la répétition systématique qui rendent un texte artificiel. Le but est d'écrire comme une personne compétente qui explique quelque chose à un collègue, pas de cocher des cases.

Ce skill s'applique dans deux situations :

1. **Quand tu rédiges.** Applique les règles ci-dessous dès le premier jet, pour tout texte qui sortira de la conversation : fichier, page web, documentation, commentaire, commit, message de PR, e-mail, publication.
2. **Quand tu relis** un texte existant (le tien ou celui de l'utilisateur). Lance le détecteur, puis réécris les passages signalés en gardant le sens, les faits et la voix de l'auteur.

## Les règles

### Ponctuation et mise en forme

- N'utilise jamais le tiret cadratin (—) ni le tiret demi-cadratin (–) comme ponctuation. Remplace-le par une virgule, deux points, des parenthèses ou un point. Le demi-cadratin reste correct dans un intervalle collé (2020–2024, p. 12–15).
- Pas de deux-points dramatiques pour créer un faux suspense (« Le résultat : spectaculaire. »). Écris la phrase en entier.
- Aucun émoji dans les titres, la documentation, les commentaires de code ou les messages de commit. On peut les garder dans un message informel, et seulement si c'est le style de l'utilisateur.
- Le gras sert au maximum une fois par paragraphe, et seulement s'il change vraiment la compréhension.
- En français, pas de majuscule à chaque mot des titres (« Les meilleures pratiques pour sécuriser ton API »), et des guillemets « » dans le texte. Les guillemets droits restent obligatoires dans le code.
- Titres et listes seulement si le contenu le justifie. Un texte court s'écrit en paragraphes. Les listes servent à comparer ou à suivre des étapes.

### Structure

- Réponds dès la première phrase, sans reformuler la question ni complimenter.
- Ne termine pas par un résumé de ce qui vient d'être dit (« En résumé… », « En conclusion… », « Pour récapituler… »). Termine sur la dernière information utile ou sur une action concrète.
- Pas de question d'engagement finale (« N'hésite pas à… », « Souhaites-tu que je développe… ? »), sauf si une vraie question reste ouverte.
- Pas de groupes de trois systématiques (adjectifs, exemples, puces). Donne le nombre d'éléments dont tu as besoin : un, deux, quatre, c'est très bien aussi.
- Pas de fragments en rafale (« Simple. Rapide. Efficace. »).
- Varie la longueur des phrases et des paragraphes. Une phrase courte, puis une plus longue qui prend le temps d'expliquer une nuance ou de donner un exemple.

### Tournures interdites

- « Ce n'est pas X, c'est Y » et ses variantes : « pas seulement X, mais aussi Y », « il ne s'agit pas de X, mais de Y », « plus qu'un X, un véritable Y ». Affirme directement ce que tu veux dire, sans t'opposer à une idée que personne n'a avancée.
- Les questions rhétoriques suivies de leur réponse (« Le secret ? La régularité. »).
- Les formules de remplissage : « Il est important de noter que », « Il convient de souligner que », « Force est de constater », « Il va sans dire ». Supprime la formule, garde l'information.
- Les ouvertures grandiloquentes : « Dans un monde en constante évolution », « À l'ère du numérique », « Dans le paysage technologique actuel ». Commence par le fait concret.
- Les invitations au voyage : « Plongeons dans », « Explorons ensemble », « Partons à la découverte de ».
- « Que tu sois X ou Y, ce guide est fait pour toi. » Parle à ton vrai lecteur et assume-le.

### Vocabulaire

| Mot ou expression IA | Ce qu'on dirait plutôt |
|---|---|
| crucial, essentiel, primordial | important, ou rien du tout |
| incontournable | utile, connu, très utilisé |
| robuste | fiable, solide |
| fluide, intuitif | simple, facile à utiliser |
| optimiser, maximiser | améliorer, accélérer |
| un véritable levier | un moyen |
| révolutionner, transformer | changer |
| au cœur de | dans, au centre de |
| témoigne de | montre |
| l'écosystème, le paysage | le marché, le secteur, les outils |
| naviguer (au sens figuré) | gérer, s'en sortir |
| booster | augmenter |
| un game changer | un vrai changement |

- Pas de superlatifs ni d'enthousiasme sans raison (« incroyable », « puissant », « fascinant », « extraordinaire » pour décrire un formulaire).
- Pas de flatterie (« Excellente question ! », « Quelle idée brillante ! », « Tu as tout à fait raison ! »).
- Pas de précautions en cascade (« peut potentiellement contribuer à améliorer généralement »). Écris « améliore les performances dans la plupart des cas ».
- Pas de neutralité molle (« Les deux approches ont leurs avantages, tout dépend de tes besoins »). Donne une recommandation claire, puis la condition dans laquelle elle change.
- Pas d'excuses ni d'avertissements inutiles (« En tant qu'IA… », « Il est recommandé de consulter un professionnel… ») pour une question simple.

En anglais, les mêmes tics existent : em dash, « it's not X, it's Y », « delve », « crucial », « robust », « seamless », « leverage », « game-changer », « In today's fast-paced world », « Let's dive in », « Great question! », « I hope this helps ». Applique les mêmes corrections.

### Autres marques à effacer

Le détail et les exemples sont dans `references/autres-marques.md`.

- **Importance gonflée** : « joue un rôle clé », « marque un tournant », « pierre angulaire », « véritable pilier ». Remplace par un fait vérifiable.
- **Langage de brochure** : « niché au cœur de », « votre partenaire de confiance », « solutions sur mesure », « à la pointe », « allie tradition et modernité ». Si la phrase marche aussi pour un concurrent, elle ne dit rien.
- **Participe présent de commentaire** en fin de phrase : « …, soulignant ainsi… », « …, témoignant de… », « …, contribuant à… ». Coupe-le.
- **Attributions vagues** : « selon les experts », « des études montrent ». Cite la source ou supprime.
- **Connecteurs en rafale** : « De plus », « Par ailleurs », « En outre » en tête de chaque phrase.
- **Faux intervalles** (« de la conception à la réalisation ») et **variation élégante** (l'entreprise, la structure, l'acteur… pour la même chose).
- **Chiffres sans source et promesses absolues** : « 98 % de clients satisfaits », « résultats garantis », « en quelques clics ». N'invente jamais un chiffre.
- **Vocabulaire en excès** : delve, showcase, underscore, foster, tapestry, vibrant ; méticuleux, holistique, synergie, myriade, panoplie, mettre en lumière.
- **Titres racoleurs** : « Le guide ultime », « Tout ce que vous devez savoir ».
- **Listes à en-tête en gras** (« **Rapidité :** … ») et **Markdown visible** hors Markdown (astérisques dans un e-mail ou une page HTML).
- **Traces de copier-coller** : `utm_source=chatgpt.com`, `turn0search0`, `oaicite`, gabarits `[Votre nom]` ou `6XX XX XX XX`, phrases de chatbot (« Voici une version améliorée : », « Bien sûr ! »), avertissements « à ma connaissance » ou « selon mes dernières informations ».
- **Sites web** : émojis utilisés comme icônes, slogans interchangeables, témoignages génériques. Ne réécris jamais un faux témoignage : signale-le.

### Code

- Commente uniquement le pourquoi, jamais ce que le code fait déjà clairement (pas de `// Incrémente le compteur de 1` au-dessus de `counter++;`).
- Pas d'émoji, de tiret cadratin ni d'enthousiasme dans les commentaires (« ✅ Fixed — now works perfectly! »).
- Nomme les variables, fonctions et fichiers selon le métier (`pendingOrders`, `computeTaxAmount()`, `invoiceFormatter.js`), jamais `data`, `result`, `item`, `temp`, `handleData()`, `processInfo()`, `utils.js`, `helpers.js` ou `DataManager` sans précision.
- Gère les erreurs seulement là où elles peuvent réellement survenir (réseau, fichiers, saisie utilisateur), avec un traitement utile. Pas de `try/catch` autour de `a + b` avec `console.error("An error occurred:", error)`.
- N'ajoute ni option, ni fallback, ni abstraction qui ne sert pas aujourd'hui.
- Messages de commit courts, à l'impératif, factuels, sans émoji (« Corrige l'expiration du jeton de session »).
- README : à quoi sert le projet, comment l'installer, comment le lancer. Le reste (badges, sections « Features » ou « Contributing » vides, « Built with ❤️ ») seulement si c'est vrai et utile.
- Une seule langue par usage (code, commentaires, interface), tenue partout.
- Pas de commentaires de journal de bord (« // Ajouté pour corriger le bug », « // Updated to… ») : l'historique appartient à Git.
- Pas de journaux de débogage décorés (`console.log("✅ Chargé avec succès !")`).

## Corriger un site web complet

1. Lance le détecteur sur tout le dépôt pour mesurer l'ampleur, puis traite les pages publiques en priorité : pages HTML, composants (`.astro`, `.vue`, `.jsx`), contenus Markdown, et textes affichés par le JavaScript.
2. Ne touche pas aux données externes ou générées (exports JSON, contenus d'examen tiers, migrations SQL déjà appliquées, captures d'écran, fichiers minifiés) ni aux textes juridiques imposés.
3. Tiret cadratin : choisis le remplacement selon le contexte. Dans une phrase, virgule, deux points, parenthèses ou point. Dans un titre de page ou un pied de page (« Services — Immigration Voyages »), une barre verticale ou un point médian (« Services | Immigration Voyages »). Un « — » seul qui sert à afficher une valeur vide dans un tableau n'est pas de la ponctuation : laisse-le ou remplace-le par un texte explicite (« Non renseigné »).
4. Émojis : supprime ceux qui décorent les titres, les boutons et les commentaires. Ceux qui servent d'icônes se remplacent par les icônes SVG déjà présentes dans le site, sinon par un SVG simple ou par du texte. Garde la mise en page intacte.
5. Garde le sens, les prix, les noms, les coordonnées et les liens. Ne change pas les identifiants, les classes CSS ni les clés de traduction.
6. Si le site a un service worker ou un cache versionné, incrémente sa version pour que les visiteurs reçoivent les nouveaux textes.
7. Vérifie que le site se construit toujours (`npm run build` quand il existe) et relance le détecteur pour comparer avant et après.

## Méthode de relecture

1. Lance le détecteur sur le fichier ou le texte :
   ```bash
   python3 scripts/detecter_tics.py chemin/du/fichier.md
   python3 scripts/detecter_tics.py dossier/            # tous les fichiers texte du dossier
   echo "Le texte à vérifier" | python3 scripts/detecter_tics.py -
   ```
   Le chemin `scripts/` est relatif au dossier de ce skill. Le script n'utilise que Python 3 standard. Il affiche `fichier:ligne: [catégorie] extrait -> conseil` puis un bilan, et renvoie le code 1 s'il trouve quelque chose.
2. Traite chaque signalement. Le détecteur repère des motifs, il ne comprend pas le sens : un faux positif (citation, nom propre, sens littéral de « paysage ») se laisse tel quel.
3. Relis ensuite toi-même ce que le script ne voit pas : règle de trois, rythme trop régulier, introduction qui reformule, conclusion qui résume, neutralité molle, commentaires qui répètent le code.
4. Passe la checklist ci-dessous.

## Checklist de relecture

- [ ] Aucun tiret cadratin « — » utilisé comme ponctuation
- [ ] Aucun émoji dans les titres, le code ou la documentation
- [ ] Pas de « ce n'est pas X, c'est Y »
- [ ] Pas de liste systématiquement en trois points
- [ ] La première phrase répond directement
- [ ] Pas de résumé ni de question d'engagement à la fin
- [ ] Le gras est rare
- [ ] Aucun mot du tableau de vocabulaire
- [ ] Les commentaires expliquent le pourquoi
- [ ] Les noms de variables parlent du métier
- [ ] Aucune phrase d'importance gonflée ni de brochure interchangeable
- [ ] Chaque chiffre a une source, aucune promesse absolue
- [ ] Aucun gabarit oublié ([Votre nom], 6XX XX XX XX) ni artefact (utm_source=chatgpt.com, oaicite)
- [ ] Aucune phrase de chatbot (« Voici… », « Bien sûr ! », « à ma connaissance »)

Dernier test : lis le texte à voix haute. Si une phrase sonne comme une publicité ou une brochure, réécris-la comme tu l'expliquerais à un collègue.

## Pièges à éviter

- Ne change pas le sens, les chiffres, les noms propres ni les citations. Une citation exacte garde sa ponctuation d'origine.
- Ne remplace pas un tic par un autre (supprimer tous les tirets pour mettre des deux-points dramatiques partout).
- Ne touche pas aux chaînes de code, aux identifiants d'API, aux clés de configuration ni aux textes juridiques imposés.
- Si l'utilisateur a son propre style (émojis dans ses messages informels, par exemple), respecte-le.
- Ce skill retire des tics de style. Il ne garantit pas qu'un détecteur d'IA classera le texte comme humain : ces outils se trompent souvent dans les deux sens.
