# Entre-temps : site web du laboratoire

## Le projet

Site web bilingue du laboratoire Entre-temps, à l'Université du Québec à Rimouski (UQAR), dirigé par Nicola Thibault-Protic, neuropsychologue et professeur.

- Descripteur officiel : « Laboratoire sur la neuropsychologie, l'électrophysiologie et le temps ».
- Thèmes : perception du temps, électrophysiologie (EEG), fonctions exécutives et cognitives, neuropsychologie 2.0 (biodonnées, tests ouverts et libres).
- Langues : français par défaut, anglais en version complète. Le nom Entre-temps reste en français dans les deux langues.

## Point de départ technique

- Gabarit : https://github.com/rempsyc/lab, le site du Laboratoire SAGE de Rémi Thériault (UQAR), sous licence MIT, lui-même généré à partir de HugoBlox/hugo-theme-academic-cv (Hugo Blox Kit).
- On part d'une copie propre du gabarit, sans son historique git. Garder le fichier de licence MIT de Rémi et un crédit discret dans le pied de page.
- Hébergement visé : GitHub Pages ou Netlify (le gabarit contient un netlify.toml et des workflows GitHub). Domaine : [À COMPLÉTER].
- Poste de travail : Mac à puce Apple. Outils attendus : git, Hugo extended (version exigée par le gabarit), Go, Node et pnpm.

## Identité visuelle

Tout est dans `marque/`. Lire `marque/MARQUE.md` avant toute décision visuelle.

- Nom : Entre-temps, avec trait d'union. Le logo l'écrit ENTRE-TEMPS.
- Symbole : un sablier formé de deux oscillations en opposition de phase, avec un grain qui tombe. Le grain et le trait d'union portent la couleur d'accent.
- Utiliser les fichiers de `marque/logo/svg/` tels quels. Ne pas redessiner, recolorer ni retaper le logo en texte.
- Couleurs, polices et rôles : `marque/jetons/tokens.css`. Toujours passer par ces variables, aucune couleur codée en dur.
- Polices auto-hébergées depuis `marque/polices/`. Pas de Google Fonts ni d'autre service externe de polices (Loi 25).

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
| Sable | #C9A46A | Accent sur fond sombre : liens, grain, trait d'union, bouton principal |
| Ocre | #8A6B33 | Accent sur fond clair : liens, grain, trait d'union |

Les paires texte et fond prévues respectent WCAG AA (détail à la fin de `tokens.css`). Le Sable ne sert jamais pour du texte sur fond clair, l'Ocre jamais pour du texte sur fond sombre.

### Typographie

- Sora 500 ou 600 : titres et éléments de marque.
- IBM Plex Sans : texte courant (400, 500, 600 et italique 400), lettres grecques comprises.
- IBM Plex Mono : sur-titres, étiquettes, données, code.
- Sur-titres en capitales avec un espacement d'environ 0,22 em.

### Direction artistique

Voir `reference/inspiration.md`. En bref : la sobriété d'animate.bio, transposée en ardoise et sable. Grands aplats Ardoise, sections claires couleur Craie, beaucoup d'espace, sur-titres espacés, symbole du sablier réutilisé en filigrane géant et très pâle derrière une section par page, portraits d'équipe en noir et blanc. Dans le héros, un fond animé discret de points en vagues qui évoque l'EEG, en canvas léger plutôt qu'en vidéo, figé quand `prefers-reduced-motion` est actif.

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
- Avant d'annoncer qu'une étape est terminée : lancer l'aperçu local et vérifier le rendu sur bureau et sur mobile, en français et en anglais.
- Accessibilité WCAG AA : contrastes, navigation au clavier, textes alternatifs, titres bien hiérarchisés.
- Aucun traceur ni outil d'analytique sans mon accord (Loi 25).
- Je code surtout en R et je commence en Python. Expliquer en une phrase les commandes Hugo, git et pnpm la première fois qu'elles servent.
