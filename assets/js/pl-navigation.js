// Pulsar Lab : bouton « Menu » sur mobile et cible du lien « Aller au contenu ».
(() => {
  const initialiser = () => {
    const entete = document.getElementById("site-header");
    const bouton = document.getElementById("pl-menu-bouton");
    const menu = document.getElementById("nav-menu");

    if (entete && bouton && menu) {
      const basculer = (ouvrir) => {
        entete.classList.toggle("pl-menu-ouvert", ouvrir);
        bouton.setAttribute("aria-expanded", ouvrir ? "true" : "false");
      };

      bouton.addEventListener("click", () => {
        basculer(bouton.getAttribute("aria-expanded") !== "true");
      });

      // Échap referme le menu et rend le focus au bouton
      document.addEventListener("keydown", (evenement) => {
        if (evenement.key === "Escape" && bouton.getAttribute("aria-expanded") === "true") {
          basculer(false);
          bouton.focus();
        }
      });
    }

    // Le corps de page de Hugo Blox n'a pas d'identifiant : on lui donne celui
    // que vise le lien d'évitement.
    const corps = document.querySelector(".page-body");
    if (corps && !document.getElementById("contenu")) {
      corps.id = "contenu";
      corps.setAttribute("tabindex", "-1");
    }
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initialiser);
  } else {
    initialiser();
  }
})();
