# Pulsar Lab : site web du laboratoire

## Le projet

Site web bilingue de Pulsar Lab (en français : laboratoire Pulsar), à l'Université du Québec à Rimouski (UQAR), dirigé par Nicola Thibault, Ph. D., neuropsychologue et professeur adjoint au Département des sciences de la santé (campus de Rimouski).

- Descripteur : « Neuropsychology, electrophysiology and time » en anglais, « Neuropsychologie, électrophysiologie et temps » en français.
- Thèmes : perception du temps, électrophysiologie (EEG), fonctions exécutives et cognitives, neuropsychologie 2.0 (biodonnées, tests ouverts et libres).
- Langues : anglais par défaut, à la racine du site (`/research/`), et français en version complète sous `/fr/` (`/fr/recherche/`). Le nom Pulsar ne se traduit pas : Pulsar Lab en anglais, laboratoire Pulsar en français.
- Ancien nom : le laboratoire s'appelait Entre-temps dans la trousse de départ (`LISEZMOI.md`, `PROMPT_DEMARRAGE.md`). Il a été renommé Pulsar Lab le 6 octobre 2026.
- Faits fournis par Nicola : `A_REMPLIR.md` et le dossier `photos_a_traiter/`, gardés hors de git. Ce sont les seules sources du contenu, avec les documents Claude Docs « Recherche de Pulsar Lab : axes et projets » et « Fiche de membre du laboratoire Pulsar ».

## Point de départ technique

- Gabarit : https://github.com/rempsyc/lab, le site du Laboratoire SAGE de Rémi Thériault (UQAR), sous licence MIT, lui-même généré à partir de HugoBlox/hugo-theme-academic-cv (Hugo Blox Kit).
- On part d'une copie propre du gabarit, sans son historique git. Garder le fichier de licence MIT de Rémi et un crédit discret dans le pied de page.
- Hébergement visé : GitHub Pages ou Netlify (le gabarit contient un netlify.toml et des workflows GitHub). Domaine : [À COMPLÉTER].
- Poste de travail : Mac à puce Apple. Outils attendus : git, Hugo extended (version exigée par le gabarit), Go, Node et pnpm.

## Identité visuelle

Tout est dans `marque/`. Lire `marque/MARQUE.md` avant toute décision visuelle.

- Nom : Pulsar Lab en anglais, laboratoire Pulsar en français. Le logo écrit PULSAR, sans « Lab », et sert aux deux langues.
- Symbole : un sablier formé de deux oscillations en opposition de phase, avec un grain qui tombe. Le grain porte la couleur d'accent.
- Utiliser les fichiers de `marque/logo/svg/` tels quels. Ne pas les redessiner, les recolorer ni retaper le logo en texte. Ils sont produits par `marque/outils/generer_logos.py` : toute modification des logos passe par ce script, avec mon accord.
- Couleurs, polices et rôles : `marque/jetons/tokens.css` (variables `--pl-*`). Toujours passer par ces variables, aucune couleur codée en dur.
- Polices auto-hébergées depuis `marque/polices/`. Pas de Google Fonts ni d'autre service externe de polices (Loi 25).
- Logo de l'UQAR : en petit sous le logo Pulsar dans l'en-tête (« logo seul ») et sous le logo du pied de page (logo officiel), en Craie sur fond sombre. Source et règles dans `marque/MARQUE.md`.

### Palette ardoise et sable

| Nom | Hex | Usage |
|---|---|---|
| Ardoise nuit | #1D262D | Pied de page, sections les plus sombres |
| Ardoise | #2C3842 | Fond sombre principal, texte principal sur fond clair |
| Ardoise claire | #33404A | Cartes et surfaces sur fond sombre |
| Schiste | #4B5A66 | Texte secondaire sur fond clair |
| Lauze | #7D8C98 | Filets, icônes, éléments décoratifs (jamais pour du texte) |
| Brume | #AAB6BF | Texte secondaire sur fond sombre |
| Nuage | #D9E0E5 | Bordures et séparateurs sur fond clair |
| Craie | #F3F5F6 | Fond clair principal |
| Sable | #C9A46A | Accent sur fond sombre : liens, grain, bouton principal |
| Ocre | #8A6B33 | Accent sur fond clair : liens, grain |

Les paires texte et fond prévues respectent WCAG AA (détail à la fin de `tokens.css`). Le Sable ne sert jamais pour du texte sur fond clair, l'Ocre jamais pour du texte sur fond sombre.

### Typographie

- Sora 500 ou 600 : titres, menu, étiquettes et éléments de marque.
- Urbanist : texte courant (400, 500, 600 et italique 400), comme sur animate.bio. IBM Plex Sans ne sert plus qu'en appoint pour les lettres grecques.
- Étiquettes (sur-titres) en casse normale, en Sora 500, en gris : Schiste sur fond clair, Brume sur fond sombre. Ni capitales espacées, ni police mono, ni couleur d'accent : ce style faisait trop « thème Claude » (décision du 7 octobre 2026).
- L'Ocre et le Sable servent aux liens, au menu actif et au grain du sablier.

### Direction artistique

Voir `reference/inspiration.md`. En bref : la sobriété d'animate.bio, transposée en ardoise et sable. Grands aplats Ardoise, sections claires couleur Craie, beaucoup d'espace, étiquettes sobres en casse normale, symbole du sablier réutilisé en filigrane géant et très pâle derrière une section par page, portraits d'équipe en noir et blanc. Dans le héros, un fond animé discret de points en vagues qui évoque l'EEG, en canvas léger plutôt qu'en vidéo, figé quand `prefers-reduced-motion` est actif.

## Règles d'écriture

Elles s'appliquent à tout le texte visible (pages, menus, boutons, textes alternatifs) en français et en anglais, ainsi qu'aux messages de commit.

- Aucun tiret cadratin (U+2014) ni demi-cadratin (U+2013) comme ponctuation. Utiliser la virgule, les deux-points ou les parenthèses.
- Éviter le point-virgule.
- Éviter les tournures « Si X, alors Y » et les paires de phrases qui répètent une seule idée (exemple à éviter : « L'exemption se demande au comité. Elle ne se décrète pas. »).
- Ton sobre, précis et humain. Rien qui sonne comme un texte généré : pas de superlatifs creux, pas d'énumérations de trois adjectifs.
- Français : québécois soutenu, typographie de l'OQLF. Anglais : formal American English.
- Ne jamais inventer de faits (projets, publications, membres, financement, coordonnées). Écrire [À COMPLÉTER] à la place.

## Façon de travailler

- Pour toute étape importante : mode Plan d'abord, présenter le plan, attendre mon accord.
- Petites étapes, avec un commit git clair et en français pour chacune.
- Avant d'annoncer qu'une étape est terminée : lancer l'aperçu local et vérifier le rendu sur bureau et sur mobile, en anglais et en français.
- Accessibilité WCAG AA : contrastes, navigation au clavier, textes alternatifs, titres bien hiérarchisés.
- Aucun traceur ni outil d'analytique sans mon accord (Loi 25).
- Je code surtout en R et je commence en Python. Expliquer en une phrase les commandes Hugo, git et pnpm la première fois qu'elles servent.
