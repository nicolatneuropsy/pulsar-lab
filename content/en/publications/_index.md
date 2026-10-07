---
title: Publications
summary: "Articles, preprints and book chapters by Nicola Thibault and Pulsar Lab."
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

        Articles, preprints and book chapters, from most recent to oldest.
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
