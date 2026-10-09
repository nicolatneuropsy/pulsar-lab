# Pulsar Lab : guide de marque

## Nom et descripteur

- Nom : **Pulsar Lab** en anglais, **laboratoire Pulsar** en français (« Laboratoire Pulsar » en début de phrase ou comme titre). Le nom Pulsar ne se traduit pas.
- Le logo écrit PULSAR en capitales, sans « Lab ». Le même logo sert aux deux langues.
- Descripteur : « Neuropsychology, electrophysiology and time » en anglais, « Neuropsychologie, électrophysiologie et temps » en français.
- Ancien nom : Entre-temps, dans la trousse de départ. Renommé Pulsar Lab le 6 octobre 2026.

## L'idée

Le symbole est un sablier dessiné par deux oscillations en opposition de phase. Un seul grain tombe, dans la couleur d'accent. Un pulsar est une étoile dont les impulsions reviennent à intervalles très réguliers, à la manière d'une horloge : le nom rejoint le temps et les oscillations qu'étudie le laboratoire.

## Fichiers

Tous les logos sont vectorisés (le texte est converti en tracés), donc ils s'affichent correctement sans les polices installées. Ils sont produits par `outils/generer_logos.py` : toute modification passe par ce script.

| Fichier (logo/svg et logo/png) | Usage |
|---|---|
| `pulsar_horizontal-descripteur_{couleur}_{en,fr}` | Pied de page du site (dans la langue de la page), en-têtes de documents, présentations, affiches |
| `pulsar_horizontal_{couleur}` | Barre de navigation, signature courriel, petits formats |
| `pulsar_vertical-descripteur_{couleur}_{en,fr}` | Page couverture, écran d'accueil, publication carrée |
| `pulsar_symbole_{couleur}` | Avatar, filigrane, petits espaces |
| `favicon/favicon.svg`, `favicon.ico`, `favicon-16.png`, `favicon-32.png` | Onglet du navigateur |
| `favicon/apple-touch-icon.png`, `icon-192.png`, `icon-512.png`, `site.webmanifest` | Écran d'accueil des téléphones |
| `social/og-image.png` | Image de partage (1200 × 630), bilingue, pour les réseaux et les messageries |

Variantes de couleur :

- `ardoise` : pour fond clair (Craie ou Blanc). Grain en Ocre.
- `craie` : pour fond sombre (Ardoise ou Ardoise nuit). Grain en Sable.
- `mono-ardoise` et `mono-blanc` : une seule couleur, pour l'impression, la gravure ou les fonds photographiques.

## Zone de protection et tailles minimales

- Garder autour du logo un espace libre au moins égal à la moitié de la largeur du symbole.
- `horizontal-descripteur` : au moins 240 px de large à l'écran, 60 mm à l'impression, pour que le descripteur reste lisible.
- `horizontal` : au moins 140 px de large.
- `symbole` : au moins 24 px de haut. En dessous, utiliser `favicon.svg`, dont le trait est plus épais.

## Couleurs

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
| Sable | #C9A46A | Accent sur fond sombre |
| Ocre | #8A6B33 | Accent sur fond clair |

Les contrastes vérifiés sont notés à la fin de `jetons/tokens.css`. Le Sable ne sert jamais pour du texte sur fond clair, et l'Ocre jamais pour du texte sur fond sombre.

## Typographie

- **Sora** (500 et 600) : titres, menu, étiquettes et éléments de marque. Le mot PULSAR du logo est en Sora 500.
- **Urbanist** (400, 500, 600, italique 400) : texte courant, et descripteur du logo en 400.
- **IBM Plex Sans**, sous-ensemble grec seulement : appoint pour les lettres grecques (Θ, Ψ, Δ, α), absentes de Sora et d'Urbanist.
- Étiquettes : Sora 500, casse normale, en gris (Schiste sur fond clair, Brume sur fond sombre). Ni capitales espacées, ni police mono, ni couleur d'accent.
- Les trois familles sont sous licence SIL Open Font License et sont fournies dans `polices/` pour l'auto-hébergement.

## Filigrane

Le symbole peut apparaître en très grand derrière une section, dépassant du cadre, avec une opacité de 5 à 8 %. Une seule fois par page.

## Logo de l'UQAR

- Source : page Direction de l'UQAR (uqar.ca/luniversite/direction-et-secretariat-general/direction/), fichier officiel RVB « officiel » (bleu foncé), téléchargé le 8 octobre 2026.
- Les versions « renversées » publiées par l'UQAR ont un fond gris semi-opaque, qui ferait un rectangle pâle sur nos fonds sombres. `assets/media/uqar/` contient donc le tracé officiel repeint en Craie (#F3F5F6, proche du gris clair des versions renversées), avec la transparence d'origine et sans les marges vides. Le dessin n'est pas modifié.
- En-tête : logo officiel complet, à la largeur du logo Pulsar (147 px), sous celui-ci, sans lien (décision du 9 octobre 2026, à la place du « logo seul »).
- Pied de page : logo officiel complet, 180 px de large, sous le logo Pulsar, avec un lien vers uqar.ca.
- Ne pas redessiner, déformer ni recolorer autrement. Sur un fond clair, utiliser les fichiers officiels en bleu.

## À éviter

- Déformer, incliner ou recadrer le logo.
- Le recolorer hors de la palette, ou lui ajouter ombre, contour ou dégradé.
- Retaper PULSAR en texte au lieu d'utiliser le fichier, ou ajouter « LAB » au logo.
- Poser le logo sur une photo chargée sans voile Ardoise d'au moins 70 %.
