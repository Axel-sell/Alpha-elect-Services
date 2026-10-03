# Alpha Elec Services — instructions pour Claude

Site vitrine statique d'une entreprise d'électricité : `Alpha Elec Site/index.html`
(HTML + CSS + JS intégrés, un seul fichier) et `Alpha Elec Site/Logo.png`.
Pas de framework, pas de build, pas de backend. Contacts : mailto et lien WhatsApp.

Le propriétaire est novice en informatique : explique en français simple, et pour toute
manipulation qu'il doit faire lui-même, avance au maximum puis donne des étapes détaillées.

## Chaîne d'agents (automatique, à appliquer sans qu'on le demande)

Chaque demande passe par la chaîne ci-dessous. Choisis le niveau selon la taille :

| Taille | Étapes |
|---|---|
| Petite (texte, couleur, lien, faute) | Construire → vérification rapide par toi-même. Pas de sous-agent. |
| Moyenne/grande (nouvelle section, refonte, fonctionnalité) | Réfléchir → Construire → Auditer + Sécuriser en parallèle → Corriger |
| Touche à un formulaire, des données clients, un script externe, un paiement, une clé/API | Toujours inclure **Sécuriser**, quelle que soit la taille |
| Lenteur constatée ou images lourdes ajoutées | Ajouter **Optimiser** |

1. **Réfléchir** — lance l'agent `architecte` : il propose un plan court (fichiers touchés, risques).
   Ne bloque pas dessus pour les tâches moyennes : commence ce qui ne dépend pas du plan.
2. **Construire** — c'est toi (session principale) qui écris le code, selon le plan.
3. **Auditer** et **Sécuriser** — lance `auditeur` et `securite` **en parallèle, dans le même message**,
   en arrière-plan, et continue pendant ce temps (ex. préparer le commit, la description de PR).
4. **Optimiser** — lance `optimiseur` uniquement dans les cas prévus au tableau.
5. **Corriger** — applique les problèmes bloquants remontés. Ignore les suggestions purement
   cosmétiques si elles ne servent pas la demande. Si une correction est importante, relance
   l'agent concerné une fois pour confirmer.
6. Termine par un résumé en français : ce qui a été fait, ce que chaque agent a trouvé,
   ce qui a été corrigé, et ce qui reste éventuellement à faire par le propriétaire.

Les agents de relecture ne modifient jamais les fichiers : ils rapportent, toi tu corriges.

## Règles du projet

- Garder un seul `index.html` autonome sauf demande contraire.
- Tout lien `target="_blank"` doit avoir `rel="noopener noreferrer"`.
- Pas de secret (clé API, mot de passe) dans le code : le site est public.
- Le site doit rester lisible sur téléphone (la majorité des visiteurs).
