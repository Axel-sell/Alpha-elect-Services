# Autres marques d'IA (au-delà du guide MEZES)

Ce fichier complète `guide-complet.md`. Il rassemble les marques relevées par d'autres sources, avec leur correction. Comme pour le reste du skill, une marque isolée ne prouve rien : c'est leur accumulation qui fait « texte généré ».

Sources :
- Wikipedia, page « Signs of AI writing » tenue par le WikiProject AI Cleanup : https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing (présentée par TechCrunch le 20 novembre 2025 : https://techcrunch.com/2025/11/20/the-best-guide-to-spotting-ai-writing-comes-from-wikipedia/). La page n'est pas une règle officielle de Wikipedia et elle évolue souvent.
- Kobak et al., « Delving into LLM-assisted writing in biomedical publications through excess vocabulary », arXiv 2406.07016 : https://arxiv.org/abs/2406.07016 (mots dont la fréquence a explosé depuis ChatGPT, par exemple delves, showcasing, underscores, crucial, potential).
- Analyses des sites générés par IA : https://adriankrebs.ch/blog/design-slop/ , https://www.925studios.co/blog/ai-slop-design-tells , https://pages.thefountaininstitute.com/posts/7-tells-that-a-ui-is-ai-generated
- Articles francophones : https://next.ink/article/71730/comment-tenter-didentifier-textes-emanant-dintelligences-artificielles-generatives , https://www.blogdumoderateur.com/chatgpt-mots-utilises-chatbot/

## A. Langue et ton

### A.1 L'importance gonflée

Le texte répète pourquoi le sujet compte au lieu de dire ce qu'il fait.

- Exemples : « joue un rôle clé », « joue un rôle crucial », « marque un tournant », « constitue une pierre angulaire », « véritable pilier », « s'inscrit dans une dynamique », « laisse une empreinte durable », « incarne l'excellence ». En anglais : plays a pivotal role, stands as a testament, marks a turning point, enduring legacy, underscores the importance.
- Version IA : Notre entreprise joue un rôle clé dans le développement énergétique de la région.
- Version humaine : Nous avons raccordé 40 bâtiments au réseau à Douala depuis 2019.
- Correction : remplace l'affirmation d'importance par un fait vérifiable (chiffre, lieu, date, nom de client si autorisé).

### A.2 Le langage de brochure

- Exemples : « niché au cœur de », « havre de paix », « à couper le souffle », « riche patrimoine », « allie tradition et modernité », « une expérience unique », « un savoir-faire unique », « des solutions sur mesure », « à la pointe de », « votre partenaire de confiance », « l'excellence à votre service », « des solutions innovantes », « qualité supérieure », « des prix compétitifs ». En anglais : nestled, boasts, vibrant, breathtaking, rich heritage, state-of-the-art, cutting-edge, one-stop shop.
- Test : si on peut remplacer le nom de l'entreprise par celui d'un concurrent sans changer la phrase, elle ne dit rien.
- Correction : dis ce que l'entreprise fait, pour qui, où, et ce qui la distingue réellement.

### A.3 Le participe présent de commentaire

Une phrase factuelle suivie d'une interprétation plaquée en fin de phrase.

- Exemples : « …, soulignant ainsi l'importance de… », « …, reflétant… », « …, contribuant à… », « …, favorisant… », « …, témoignant de… », « …, illustrant… », « …, garantissant… », « …, renforçant… ». En anglais : « …, highlighting… », « …, underscoring… », « …, ensuring… », « …, reflecting… », « …, showcasing… ».
- Version IA : Le cabinet a ouvert un bureau à Yaoundé, témoignant de sa volonté de se rapprocher de ses clients.
- Version humaine : Le cabinet a ouvert un bureau à Yaoundé en 2024.
- Correction : coupe la fin de phrase ou transforme-la en fait.

### A.4 Les attributions vagues

- Exemples : « selon les experts », « de nombreux spécialistes s'accordent à dire », « des études montrent », « il est largement reconnu que », « certains observateurs ». En anglais : experts say, studies show, observers note, it is widely recognized.
- Correction : cite la source précise (nom, date, lien) ou supprime l'affirmation.

### A.5 Les connecteurs en rafale

« De plus », « Par ailleurs », « En outre », « De surcroît », « Ainsi », « En effet », « Néanmoins » en tête de presque chaque phrase ou paragraphe. En anglais : Moreover, Furthermore, Additionally, Notably, Importantly.

- Correction : garde un connecteur seulement quand il exprime un vrai lien logique. La plupart des phrases s'enchaînent très bien sans.

### A.6 Les faux intervalles « de X à Y »

« De la conception à la réalisation », « des débutants aux experts », « des PME aux grands groupes », quand ces deux bornes ne décrivent pas une vraie échelle.

- Correction : liste ce qui est réellement couvert, ou choisis un public.

### A.7 La variation élégante

Le même objet nommé différemment d'une phrase à l'autre pour éviter la répétition : « l'entreprise », puis « la structure », « l'acteur », « le spécialiste », « la société ».

- Correction : garde le même mot. La répétition est plus claire que la synonymie forcée.

### A.8 Les chiffres sans source et les promesses absolues

- Exemples : « 10 fois plus rapide », « +200 % de visibilité », « 98 % de clients satisfaits », « des milliers de clients », « résultats garantis », « 100 % de réussite », « sans effort », « en quelques clics », « clé en main », « la solution idéale », « tout ce dont vous avez besoin ».
- Correction : un chiffre réel et vérifiable, avec sa source et sa date, ou rien. Ne jamais inventer un chiffre. Sur un site commercial, une promesse invérifiable peut aussi poser un problème juridique (publicité trompeuse).

### A.9 Le vocabulaire en excès

Mots dont l'usage a fortement augmenté depuis 2023 (étude Kobak et al., page Wikipedia).

- Anglais : delve, showcase, underscore, intricate, meticulous, commendable, notably, comprehensive, enhance, foster, garner, interplay, realm, pivotal, align with, valuable, key (adjectif), landscape (abstrait), tapestry (abstrait), testament, vibrant, enduring, highlight (verbe).
- Français (équivalents fréquents) : méticuleux, minutieux, holistique, synergie, catalyseur, tremplin, pierre angulaire, une myriade de, une panoplie de, un éventail de, mettre en lumière, captivant, époustouflant, inestimable, fondamental, indispensable, favoriser, renforcer, englober.
- Correction : le mot simple qu'on emploierait à l'oral, ou rien.

### A.10 Les titres racoleurs

« Le guide ultime », « Tout ce que vous devez savoir sur… », « Le guide complet », « Les secrets de… ». En anglais : The Ultimate Guide, Everything You Need to Know, Unlock the power of, Unleash, Elevate your, Supercharge.

- Correction : un titre qui dit ce que le lecteur va trouver.

## B. Forme

### B.1 Les listes à en-tête en gras

Chaque puce commence par un mot en gras suivi de deux points : « **Rapidité :** … », « **Fiabilité :** … », « **Accompagnement :** … ».

- Correction : une phrase normale, ou un tableau si on compare vraiment des éléments.

### B.2 Le Markdown visible là où il n'a rien à faire

Des `**astérisques**`, des `###` ou des tirets de liste qui s'affichent tels quels dans un e-mail, un SMS, un message WhatsApp, une publication Facebook, un champ de formulaire ou une page HTML.

- Correction : retire la syntaxe Markdown et utilise la mise en forme du support (ou aucune).

### B.3 L'incohérence typographique

Apostrophes droites (') et courbes (’) mélangées dans le même texte, guillemets droits et chevrons mélangés, espaces avant la ponctuation double présentes ici et absentes là. C'est la trace typique d'un texte assemblé à partir de plusieurs sorties d'IA.

- Correction : choisis une convention et applique-la partout.

## C. Traces techniques laissées par le copier-coller

### C.1 Les artefacts de citation

`turn0search0`, `:contentReference[oaicite:0]{index=0}`, `oai_citation`, `【4†source】`, `utm_source=chatgpt.com` ou `utm_source=openai` dans un lien, `grok_card`, `attached_file`.

- Correction : supprime l'artefact. Pour un lien, retire le paramètre `utm_source` et vérifie que la page existe.

### C.2 Les gabarits oubliés

`[Votre nom]`, `[Nom de l'entreprise]`, `[Insérer le lien]`, `[Your Name]`, `XX/XX/2025`, `+237 6XX XX XX XX`, `contact@votresite.com`, `Lorem ipsum`.

- Correction : remplace par la vraie valeur ou supprime. Attention : un `placeholder="Votre nom"` dans un champ de formulaire est normal.

### C.3 Les phrases de chatbot restées dans le texte

« Voici une version améliorée de votre texte : », « Bien sûr ! », « Certainement ! », « Absolument ! », « J'espère que cela vous aide ». En anglais : Certainly!, Sure! Here is, Of course!, I hope this helps.

### C.4 Les avertissements de date de connaissance

« À ma connaissance », « selon mes dernières informations », « à la date de ma dernière mise à jour », « je n'ai pas accès à des informations en temps réel ». En anglais : as of my last knowledge update, as of my knowledge cutoff, I don't have real-time information.

- Correction : vérifie l'information et donne-la avec sa date, ou retire la phrase.

### C.5 La fin coupée ou le changement de style brutal

Un texte qui s'arrête au milieu d'une liste, ou un paragraphe dont le ton, la langue ou le tutoiement change d'un coup : souvent une sortie d'IA collée sans relecture.

## D. Sites web

Ces marques relèvent du design autant que du texte. Le détecteur repère les émojis ; le reste se signale à l'utilisateur, car le corriger demande une décision de design.

- **Émojis utilisés comme icônes** (📞 ✉️ 📍 ⚡ 🚀 ✅ 💡) : remplace-les par un seul jeu d'icônes SVG cohérent, ou par du texte. Ne mélange pas plusieurs bibliothèques d'icônes.
- Dégradés violet-bleu, effet verre dépoli, halos néon, formes 3D floues en fond, police Inter partout.
- Mise en page par défaut : grand titre centré, puis exactement trois cartes « Qualité / Rapidité / Fiabilité », puis « Pourquoi nous choisir ? ».
- Petit badge en majuscules au-dessus du titre principal (« ✨ NOUVEAU », « 🚀 LANCEMENT »).
- Slogans interchangeables (voir A.2) et chiffres invérifiables (voir A.8).
- Témoignages génériques sans nom complet, sans date ni contexte. Ne jamais en inventer : un faux avis client est une pratique commerciale trompeuse. Si les témoignages ne sont pas réels, signale-le à l'utilisateur au lieu de les réécrire.

## E. Code

- **Commentaires de journal de bord** : « // Ajouté pour corriger le bug », « // Nouvelle version », « // MODIFIÉ : », « // Updated to… », « // Now handles… ». L'historique appartient à Git, pas au code.
- **Docstring ou JSDoc exhaustif sur une fonction triviale** : un paramètre `id` décrit comme « l'identifiant ».
- **Journaux de débogage décorés** : `console.log("✅ Données chargées avec succès !")`, `print("🚀 Starting...")`. Retire-les, ou garde un message court et utile.
- **Commentaires en majuscules ou alarmistes** : « // IMPORTANT !!! », « // NE PAS TOUCHER ». Explique plutôt pourquoi.
