#!/usr/bin/env python3
"""Pulsar Lab : production des logos et de l'image de partage.

Le script compose le mot PULSAR et le descripteur à partir des polices de
marque/polices, les convertit en tracés, puis écrit :
  - marque/logo/svg/pulsar_*.svg et marque/logo/png/pulsar_*.png,
  - marque/social/og-image.png (1200 x 630).

Construction, retrouvée dans les logos d'origine (octobre 2026) :
  - mot : Sora 500, corps 64, espacement de 0,16 em, crénage de la police,
  - descripteur : IBM Plex Sans 400,
  - symbole : le sablier formé de deux oscillations en opposition de phase,
    repris tel quel, avec un grain de rayon égal à 0,8 fois l'épaisseur du trait,
  - marges : 2 % de la hauteur du contenu, de chaque côté.
Les couleurs viennent de marque/jetons/tokens.json.

Dépendances, à installer dans un environnement Python à part :
    pip install fonttools brotli uharfbuzz resvg-py

Utilisation, depuis la racine du dépôt :
    python marque/outils/generer_logos.py
"""

import io
import json
from pathlib import Path

import resvg_py
import uharfbuzz as hb
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

MARQUE = Path(__file__).resolve().parents[1]
POLICES = MARQUE / "polices"

# ---------- Textes ----------

NOM = "PULSAR"
TITRE = {"en": "Pulsar Lab", "fr": "Laboratoire Pulsar"}
DESCRIPTEUR = {
    "en": ("Neuropsychology,", "electrophysiology and time"),
    "fr": ("Neuropsychologie,", "électrophysiologie et temps"),
}
DESCRIPTEUR_UNE_LIGNE = {
    "en": "Neuropsychology, electrophysiology and time",
    "fr": "Neuropsychologie, électrophysiologie et temps",
}
LIEU = "UQAR · RIMOUSKI"

# ---------- Symbole (identique aux fichiers d'origine) ----------

SABLIER = "M26,16H94M26,104H94M85,16C85,48.1 35,71.9 35,104M35,16C35,48.1 85,71.9 85,104"
GRAIN_X, GRAIN_Y = 60, 77

# ---------- Mesures des logos d'origine ----------

MOT_CORPS = 64
MOT_ESPACEMENT = 0.16  # em
DESC_CORPS_HORIZONTAL = 34.8662
DESC_CORPS_VERTICAL = 31.3796  # 90 % du corps horizontal
INTERLIGNE_HORIZONTAL = 49.51  # de ligne de base à ligne de base
INTERLIGNE_VERTICAL = 45.50

# Image de partage : bloc du logo à l'échelle 1,0152, aligné à x = 99,25 et
# centré verticalement, « UQAR · RIMOUSKI » en IBM Plex Mono 500, corps 20,5,
# espacement 0,22 em, grand sablier en filigrane à droite.
PARTAGE_LARGEUR, PARTAGE_HAUTEUR = 1200, 630
PARTAGE_ECHELLE = 1.0152
PARTAGE_BORD_GAUCHE = 99.25
PARTAGE_LARGEUR_LIGNES = 567.17  # largeur des lignes du descripteur, en unités du logo
LIEU_CORPS, LIEU_ESPACEMENT = 20.5, 0.22
LIEU_X, LIEU_LIGNE_DE_BASE = 97, 568
FILIGRANE_ECHELLE = 8
FILIGRANE_CROISEMENT = (966.5, 315)  # point où les deux oscillations se croisent

# ---------- Couleurs (marque/jetons/tokens.json) ----------

JETONS = json.loads((MARQUE / "jetons" / "tokens.json").read_text(encoding="utf-8"))
C = {nom: valeur["hex"] for nom, valeur in JETONS["couleurs"].items()}
OPACITE_FILIGRANE = JETONS["formes"]["opacite-filigrane"]

VARIANTES = {
    "ardoise": dict(trait=C["ardoise"], mot=C["ardoise"], grain=C["ocre"], desc=C["schiste"]),
    "craie": dict(trait=C["craie"], mot=C["craie"], grain=C["sable"], desc=C["brume"]),
    "mono-ardoise": dict(trait=C["ardoise"], mot=C["ardoise"], grain=C["ardoise"], desc=C["ardoise"]),
    "mono-blanc": dict(trait=C["blanc"], mot=C["blanc"], grain=C["blanc"], desc=C["blanc"]),
}


def nombre(v, decimales=2):
    """Écrit un nombre sans zéros inutiles (63.07, 36, -0.5)."""
    texte = f"{v:.{decimales}f}"
    if "." in texte:
        texte = texte.rstrip("0").rstrip(".")
    return "0" if texte in ("-0", "") else texte


class Police:
    """Police de marque/polices : mise en forme par HarfBuzz, tracés par fontTools."""

    def __init__(self, fichier):
        chemin = POLICES / fichier
        self.tt = TTFont(chemin)
        self.glyphes = self.tt.getGlyphSet()
        self.upm = self.tt["head"].unitsPerEm
        tampon = io.BytesIO()
        copie = TTFont(chemin)
        copie.flavor = None  # HarfBuzz lit le TrueType, pas le WOFF2
        copie.save(tampon)
        self.hb = hb.Font(hb.Face(hb.Blob(tampon.getvalue())))

    def placer(self, texte, espacement=0.0):
        """Positions des glyphes (unités de la police) et avance totale."""
        tampon = hb.Buffer()
        tampon.add_str(texte)
        tampon.guess_segment_properties()
        hb.shape(self.hb, tampon, {})
        x = 0.0
        places = []
        for info, pos in zip(tampon.glyph_infos, tampon.glyph_positions):
            places.append((self.tt.getGlyphName(info.codepoint), x + pos.x_offset, pos.y_offset))
            x += pos.x_advance + espacement * self.upm
        return places, x - espacement * self.upm

    def avance(self, texte, corps, espacement=0.0):
        return self.placer(texte, espacement)[1] * corps / self.upm

    def gauche(self, texte, corps, espacement=0.0):
        """Distance entre l'origine et le bord gauche de la première lettre."""
        places, _ = self.placer(texte, espacement)
        bornes = BoundsPen(self.glyphes)
        self.glyphes[places[0][0]].draw(bornes)
        return bornes.bounds[0] * corps / self.upm

    def tracer(self, texte, x0, ligne_de_base, corps, espacement=0.0):
        """Chemin SVG du texte converti en tracés, et sa boîte englobante."""
        places, _ = self.placer(texte, espacement)
        e = corps / self.upm
        stylo = SVGPathPen(self.glyphes, ntos=nombre)
        bornes = BoundsPen(self.glyphes)
        for nom, gx, gy in places:
            matrice = (e, 0, 0, -e, x0 + gx * e, ligne_de_base - gy * e)
            self.glyphes[nom].draw(TransformPen(stylo, matrice))
            self.glyphes[nom].draw(TransformPen(bornes, matrice))
        return stylo.getCommands(), bornes.bounds


SORA = Police("sora-latin-500-normal.woff2")
PLEX = Police("ibm-plex-sans-latin-400-normal.woff2")
PLEX_MONO = Police("ibm-plex-mono-latin-500-normal.woff2")


def union(*boites):
    return (min(b[0] for b in boites), min(b[1] for b in boites),
            max(b[2] for b in boites), max(b[3] for b in boites))


def symbole(couleurs, echelle, tx, ty, trait):
    """Groupe SVG du sablier et sa boîte englobante (trait compris)."""
    demi = trait / 2
    boite = ((26 - demi) * echelle + tx, (16 - demi) * echelle + ty,
             (94 + demi) * echelle + tx, (104 + demi) * echelle + ty)
    groupe = (
        f'<g transform="translate({nombre(tx, 4)} {nombre(ty, 4)}) scale({nombre(echelle, 4)})" '
        f'fill="none" stroke="{couleurs["trait"]}" stroke-width="{nombre(trait)}" '
        f'stroke-linecap="round" stroke-linejoin="round"><path d="{SABLIER}"/>'
        f'<circle fill="{couleurs["grain"]}" stroke="none" cx="{GRAIN_X}" cy="{GRAIN_Y}" '
        f'r="{nombre(0.8 * trait)}"/></g>'
    )
    return groupe, boite


def document(titre, langue, elements, boite):
    """Enveloppe SVG avec une marge de 2 % de la hauteur du contenu."""
    x0, y0, x1, y1 = boite
    marge = 0.02 * (y1 - y0)
    largeur, hauteur = x1 - x0 + 2 * marge, y1 - y0 + 2 * marge
    attribut_langue = f' lang="{langue}"' if langue else ""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg"{attribut_langue} '
        f'viewBox="{nombre(x0 - marge)} {nombre(y0 - marge)} {nombre(largeur)} {nombre(hauteur)}" '
        f'width="{nombre(largeur)}" height="{nombre(hauteur)}" role="img" aria-labelledby="t">'
        f'<title id="t">{titre}</title>{"".join(elements)}</svg>'
    ), (largeur, hauteur)


def chemin(couleur, d):
    return f'<path fill="{couleur}" d="{d}"/>'


def logo_symbole(couleurs):
    groupe, _ = symbole(couleurs, 1.28, -29.84, -17.01, 5.5)
    # Boîte d'origine conservée telle quelle (fichiers entre-temps_symbole_*)
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="-2.4 -2.4 99.13 124.8" '
        'width="99.13" height="124.8" role="img" aria-labelledby="t">'
        f'<title id="t">{TITRE["en"]}</title>{groupe}</svg>'
    )
    return svg, (99.13, 124.8)


def logo_horizontal(couleurs):
    groupe, boite_symbole = symbole(couleurs, 0.83, -18.2, -9.93, 8)
    x0 = 95.56 - SORA.gauche(NOM, MOT_CORPS, MOT_ESPACEMENT)  # première lettre à x = 95,56
    d, boite_mot = SORA.tracer(NOM, x0, 63.07, MOT_CORPS, MOT_ESPACEMENT)
    return document(TITRE["en"], None, [groupe, chemin(couleurs["mot"], d)], union(boite_symbole, boite_mot))


def logo_horizontal_descripteur(couleurs, langue):
    groupe, boite_symbole = symbole(couleurs, 1.71, -40.27, -23.13, 5)
    x0 = 177.628  # origine commune du mot et du descripteur
    d_mot, b_mot = SORA.tracer(NOM, x0, 46.72, MOT_CORPS, MOT_ESPACEMENT)
    ligne1, ligne2 = DESCRIPTEUR[langue]
    d1, b1 = PLEX.tracer(ligne1, x0, 101.84, DESC_CORPS_HORIZONTAL)
    d2, b2 = PLEX.tracer(ligne2, x0, 101.84 + INTERLIGNE_HORIZONTAL, DESC_CORPS_HORIZONTAL)
    titre = f"{TITRE[langue]}, {ligne1[0].lower()}{ligne1[1:]} {ligne2}"
    elements = [groupe, chemin(couleurs["mot"], d_mot), chemin(couleurs["desc"], d1), chemin(couleurs["desc"], d2)]
    return document(titre, langue, elements, union(boite_symbole, b_mot, b1, b2))


def logo_vertical_descripteur(couleurs, langue):
    centre = SORA.avance(NOM, MOT_CORPS, MOT_ESPACEMENT) / 2  # le mot part de x = 0
    groupe, boite_symbole = symbole(couleurs, 1.3, centre - GRAIN_X * 1.3, -17.21, 5.5)
    d_mot, b_mot = SORA.tracer(NOM, 0, 210.24, MOT_CORPS, MOT_ESPACEMENT)
    ligne1, ligne2 = DESCRIPTEUR[langue]
    elements = [groupe, chemin(couleurs["mot"], d_mot)]
    boites = [boite_symbole, b_mot]
    for texte, base in ((ligne1, 267.41), (ligne2, 267.41 + INTERLIGNE_VERTICAL)):
        x = centre - PLEX.avance(texte, DESC_CORPS_VERTICAL) / 2
        d, b = PLEX.tracer(texte, x, base, DESC_CORPS_VERTICAL)
        elements.append(chemin(couleurs["desc"], d))
        boites.append(b)
    titre = f"{TITRE[langue]}, {ligne1[0].lower()}{ligne1[1:]} {ligne2}"
    return document(titre, langue, elements, union(*boites))


def image_de_partage():
    """Image de partage bilingue : PULSAR, descripteur anglais puis français."""
    couleurs = VARIANTES["craie"]
    ligne_en, ligne_fr = DESCRIPTEUR_UNE_LIGNE["en"], DESCRIPTEUR_UNE_LIGNE["fr"]
    corps = PARTAGE_LARGEUR_LIGNES / max(PLEX.avance(t, 1) for t in (ligne_en, ligne_fr))
    hauteur_capitales = 0.698 * corps
    x0 = 177.628
    base1 = 46.72 + 30.78 + hauteur_capitales  # même blanc qu'à l'origine sous le mot
    base2 = base1 + INTERLIGNE_HORIZONTAL / DESC_CORPS_HORIZONTAL * corps
    d_mot, b_mot = SORA.tracer(NOM, x0, 46.72, MOT_CORPS, MOT_ESPACEMENT)
    d1, b1 = PLEX.tracer(ligne_en, x0, base1, corps)
    d2, b2 = PLEX.tracer(ligne_fr, x0, base2, corps)
    # Le symbole couvre le bloc de texte, du haut des capitales à la place des descendantes
    bas = base2 + (159.34 - 151.35) / DESC_CORPS_HORIZONTAL * corps
    echelle = bas / 93  # hauteur du sablier avec un trait de 5 : 93 unités
    groupe, b_sym = symbole(couleurs, echelle, -(26 - 2.5) * echelle, -(16 - 2.5) * echelle, 5)
    bloc = union(b_sym, b_mot, b1, b2)
    k = PARTAGE_ECHELLE
    tx = PARTAGE_BORD_GAUCHE - bloc[0] * k
    ty = PARTAGE_HAUTEUR / 2 - (bloc[1] + bloc[3]) / 2 * k
    d_lieu, _ = PLEX_MONO.tracer(LIEU, LIEU_X - PLEX_MONO.gauche(LIEU, LIEU_CORPS, LIEU_ESPACEMENT),
                                 LIEU_LIGNE_DE_BASE, LIEU_CORPS, LIEU_ESPACEMENT)
    fx = FILIGRANE_CROISEMENT[0] - 60 * FILIGRANE_ECHELLE
    fy = FILIGRANE_CROISEMENT[1] - 60 * FILIGRANE_ECHELLE
    filigrane, _ = symbole(couleurs, FILIGRANE_ECHELLE, fx, fy, 5.5)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {PARTAGE_LARGEUR} {PARTAGE_HAUTEUR}" '
        f'width="{PARTAGE_LARGEUR}" height="{PARTAGE_HAUTEUR}">'
        f'<rect width="{PARTAGE_LARGEUR}" height="{PARTAGE_HAUTEUR}" fill="{C["ardoise"]}"/>'
        f'<g opacity="{OPACITE_FILIGRANE}">{filigrane}</g>'
        f'<g transform="translate({nombre(tx, 4)} {nombre(ty, 4)}) scale({k})">{groupe}'
        f'{chemin(couleurs["mot"], d_mot)}{chemin(couleurs["desc"], d1)}{chemin(couleurs["desc"], d2)}</g>'
        f'{chemin(couleurs["desc"], d_lieu)}</svg>'
    )


def ecrire_png(svg, fichier, largeur=None, hauteur=None):
    donnees = resvg_py.svg_to_bytes(svg_string=svg, width=largeur, height=hauteur)
    fichier.write_bytes(bytes(donnees))


def main():
    dossier_svg = MARQUE / "logo" / "svg"
    dossier_png = MARQUE / "logo" / "png"
    produits = []

    def sortir(nom, svg, largeur_png=None, hauteur_png=None):
        (dossier_svg / f"{nom}.svg").write_text(svg, encoding="utf-8")
        ecrire_png(svg, dossier_png / f"{nom}.png", largeur_png, hauteur_png)
        produits.append(nom)

    for variante, couleurs in VARIANTES.items():
        svg, _ = logo_symbole(couleurs)
        sortir(f"pulsar_symbole_{variante}", svg, hauteur_png=1000)
    for variante in ("ardoise", "craie"):
        svg, _ = logo_horizontal(VARIANTES[variante])
        sortir(f"pulsar_horizontal_{variante}", svg, largeur_png=2000)
    for langue in ("en", "fr"):
        for variante, couleurs in VARIANTES.items():
            svg, _ = logo_horizontal_descripteur(couleurs, langue)
            sortir(f"pulsar_horizontal-descripteur_{variante}_{langue}", svg, largeur_png=2000)
        for variante in ("ardoise", "craie"):
            svg, _ = logo_vertical_descripteur(VARIANTES[variante], langue)
            sortir(f"pulsar_vertical-descripteur_{variante}_{langue}", svg, largeur_png=1600)

    ecrire_png(image_de_partage(), MARQUE / "social" / "og-image.png", largeur=PARTAGE_LARGEUR)
    print(f"{len(produits)} logos (SVG et PNG) et l'image de partage écrits dans {MARQUE}")


if __name__ == "__main__":
    main()
