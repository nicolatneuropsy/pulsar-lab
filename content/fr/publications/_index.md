---
title: Publications
summary: "Articles, prépublications et chapitres de livre de Nicola Thibault et du laboratoire Pulsar."
translationKey: publications
# Pages des publications : pas de temps de lecture (le résumé seul ne fait pas un texte à lire)
cascade:
  params:
    reading_time: false
type: landing

sections:
  - block: markdown
    content:
      text: |
        # Publications

        Articles, prépublications et chapitres de livre, du plus récent au plus ancien.
    design:
      columns: "1"
      spacing:
        padding: ["3rem", "0", "1rem", "0"]

  - block: collection
    content:
      count: 0
      filters:
        folders:
          - publications
        exclude_featured: false
    design:
      view: citation
      spacing:
        padding: ["1rem", "0", "3rem", "0"]
---
