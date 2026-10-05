# Inspiration et structure du site

## animate.bio : ce qu'on retient

Site d'Animate Biosciences, observé le 3 octobre 2026.

- Héros plein écran très sombre avec une vidéo de particules qui forment des vagues. Chez nous : un canvas léger de points en vagues, en Brume sur Ardoise, qui évoque un tracé EEG et se fige quand `prefers-reduced-motion` est actif.
- Logo : un symbole à trait unique à côté d'un nom en capitales très espacées.
- Sur-titres en capitales espacées dans la couleur d'accent (« OUR TEAM »), titres centrés en Sora 600, paragraphes courts, beaucoup d'air.
- Le symbole du logo revient en filigrane géant et pâle derrière la section équipe.
- Équipe : portraits noir et blanc aux coins arrondis, carrousel avec flèches dans des cercles, bouton « + » qui ouvre la biographie.
- Chez eux : marine, cyan et ambre, polices Sora et Urbanist. Chez nous : Ardoise, Craie, Sable et Ocre, polices Sora et IBM Plex Sans.

## labosage.com et le gabarit rempsyc/lab : ce qu'on garde

- Hugo Blox Kit (gabarit academic-cv) : site statique, rapide, sans base de données.
- Le bilinguisme déjà configuré. Dans le gabarit, les pages françaises vivent sous `/fr/`. Pour Entre-temps, le français doit être la langue principale : choisir avec moi entre le français à la racine ou deux préfixes `/fr/` et `/en/`.
- Les pages de membres, les publications générées à partir de fichiers BibTeX, les nouvelles et la recherche dans le site.
- Le déploiement automatisé (GitHub Actions ou Netlify).

## Arborescence proposée

| Page | Page anglaise | Contenu |
|---|---|---|
| Accueil | Home | Héros, axes de recherche, neuropsychologie 2.0, équipe, publications récentes, appel à participer, nouvelles |
| Recherche | Research | Quatre axes : perception du temps, électrophysiologie, fonctions exécutives, tests ouverts et biodonnées. Projets en cours [À COMPLÉTER] |
| Équipe | Team | Direction, étudiantes et étudiants, collaborations, anciens membres |
| Publications | Publications | Liste générée depuis BibTeX, filtres par année et par type |
| Tests ouverts | Open tests | Outils et tests libres du laboratoire, liens GitHub, licences, documentation |
| Participer à une étude | Take part in a study | Études en recrutement, critères, déroulement, compensation, contact [À COMPLÉTER] |
| Nouvelles | News | Billets courts : publications, conférences, arrivées, financement |
| Contact | Contact | Adresse à l'UQAR, courriel, plan [À COMPLÉTER] |

## Page d'accueil proposée, de haut en bas

1. Héros sombre (Ardoise) : fond animé de points en vagues, logo horizontal en version craie, sur-titre « NEUROPSYCHOLOGIE 2.0 », titre court et phrase de mission [À COMPLÉTER], deux boutons : « Nos recherches » (plein, Sable) et « Participer à une étude » (contour).
2. Axes de recherche sur fond Craie : quatre cartes, chacune avec une petite icône à trait unique dans l'esprit du symbole.
3. Bandeau Ardoise « Neuropsychologie 2.0 » : texte court, liens vers les tests ouverts et vers GitHub.
4. Équipe : sur-titre « NOTRE ÉQUIPE », portraits noir et blanc, sablier en filigrane.
5. Publications récentes : les trois dernières, lien vers la liste complète.
6. Appel à participer : bandeau clair, bouton Ocre.
7. Nouvelles : les trois derniers billets.
8. Pied de page Ardoise nuit : logo horizontal avec descripteur (version craie), adresse [À COMPLÉTER], liens utiles, crédit du gabarit.

## Détails à soigner

- Sélecteur de langue FR et EN visible dans l'en-tête.
- Sur mobile : menu replié, héros plus court, cartes empilées.
- Images en WebP avec textes alternatifs, portraits recadrés de la même façon.
- Favicons et `site.webmanifest` copiés à la racine publique du site.
- `marque/social/og-image.png` branchée dans les métadonnées Open Graph.
