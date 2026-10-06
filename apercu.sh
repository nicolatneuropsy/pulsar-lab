#!/usr/bin/env bash
# Aperçu local du site de Pulsar Lab, sur Mac (équivalent de preview.ps1 sous Windows).
#
# Au premier lancement, le script télécharge la version de Hugo fixée dans
# hugoblox.yaml (la même que sur GitHub) et la range dans le cache de la
# session (~/Library/Caches/pulsar-lab), hors de OneDrive, sans rien installer
# dans le système. Il installe ensuite les dépendances Node au besoin,
# puis lance le serveur d'aperçu sur http://localhost:1313/ (ou le premier port
# libre jusqu'à 1323). Les pages se rechargent à chaque modification.
#
# Utilisation :
#   ./apercu.sh                    aperçu, ouvert dans le navigateur
#   ./apercu.sh --sans-navigateur  aperçu, sans ouvrir le navigateur
#   ./apercu.sh --chemin-hugo      prépare Hugo et affiche son chemin

set -euo pipefail

racine="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$racine"

# Outils installés par Homebrew (Go, Node, pnpm), même hors d'un terminal configuré
if [[ -d /opt/homebrew/bin ]]; then
  PATH="/opt/homebrew/bin:$PATH"
fi

mode="${1:-}"

version_hugo="$(sed -n "s/^[[:space:]]*hugo_version:[[:space:]]*['\"]\{0,1\}\([0-9.]*\).*/\1/p" hugoblox.yaml | head -n 1)"
if [[ -z "$version_hugo" ]]; then
  echo "Version de Hugo introuvable dans hugoblox.yaml." >&2
  exit 1
fi

dossier_hugo="$HOME/Library/Caches/pulsar-lab/hugo-$version_hugo"
hugo="$dossier_hugo/hugo"

if [[ ! -x "$hugo" ]]; then
  echo "Préparation de Hugo $version_hugo (une seule fois)..." >&2
  temp="$(mktemp -d)"
  depot="https://github.com/gohugoio/hugo/releases/download/v$version_hugo"
  paquet="hugo_extended_${version_hugo}_darwin-universal.pkg"
  curl -fsSL "$depot/$paquet" -o "$temp/$paquet"
  curl -fsSL "$depot/hugo_${version_hugo}_checksums.txt" -o "$temp/empreintes.txt"
  attendue="$(awk -v f="$paquet" '$2 == f { print $1 }' "$temp/empreintes.txt")"
  obtenue="$(shasum -a 256 "$temp/$paquet" | awk '{ print $1 }')"
  if [[ -z "$attendue" || "$attendue" != "$obtenue" ]]; then
    rm -rf "$temp"
    echo "Empreinte SHA-256 invalide pour $paquet. Téléchargement refusé." >&2
    exit 1
  fi
  # Extraction du programme sans lancer l'installateur
  pkgutil --expand-full "$temp/$paquet" "$temp/paquet"
  binaire="$(find "$temp/paquet" -type f -name hugo -perm -u+x | head -n 1)"
  if [[ -z "$binaire" ]]; then
    rm -rf "$temp"
    echo "Programme hugo introuvable dans $paquet." >&2
    exit 1
  fi
  mkdir -p "$dossier_hugo"
  cp "$binaire" "$hugo"
  chmod +x "$hugo"
  rm -rf "$temp"
fi

version_obtenue="$("$hugo" version)"
if [[ "$version_obtenue" != *"v$version_hugo"* || "$version_obtenue" != *"+extended"* ]]; then
  echo "Hugo extended $version_hugo attendu, obtenu : $version_obtenue" >&2
  echo "Supprimez le dossier $dossier_hugo puis relancez le script." >&2
  exit 1
fi

if [[ "$mode" == "--chemin-hugo" ]]; then
  echo "$hugo"
  exit 0
fi

for outil in go node pnpm; do
  if ! command -v "$outil" > /dev/null; then
    echo "$outil est introuvable. Installez-le avec : brew install $outil" >&2
    exit 1
  fi
done

if [[ ! -d node_modules ]]; then
  echo "Installation des dépendances Node (pnpm install)..." >&2
  pnpm install
fi

port=""
for candidat in $(seq 1313 1323); do
  if ! nc -z 127.0.0.1 "$candidat" 2> /dev/null; then
    port="$candidat"
    break
  fi
done
if [[ -z "$port" ]]; then
  echo "Aucun port libre entre 1313 et 1323. Fermez un autre aperçu et réessayez." >&2
  exit 1
fi
adresse="http://localhost:$port/"

echo ""
echo "Aperçu de Pulsar Lab : $adresse"
echo "Les pages se mettent à jour à chaque modification. Ctrl+C pour arrêter."
echo ""

if [[ "$mode" != "--sans-navigateur" ]]; then
  (sleep 4 && open "$adresse") &
fi

# --renderToMemory : les pages restent en mémoire, rien n'est écrit dans OneDrive
exec "$hugo" server \
  --renderToMemory \
  --bind 127.0.0.1 \
  --port "$port" \
  --baseURL "$adresse" \
  --poll 700ms \
  --disableFastRender \
  --noTimes
