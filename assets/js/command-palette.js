(() => {
  if (window.__xianCommandHotkeys) return;
  window.__xianCommandHotkeys = true;
  const trigger = () => document.getElementById("command-palette-trigger")?.click();
  const close = () => document.getElementById("command-palette-close")?.click();
  const moveUp = () => document.getElementById("command-palette-up")?.click();
  const moveDown = () => document.getElementById("command-palette-down")?.click();
  const selectActive = () => document.getElementById("command-palette-select")?.click();
  const closeLightbox = () => document.getElementById("image-lightbox-close")?.click();
  const isLightboxOpen = () => document.getElementById("image-lightbox-container");
  const scrollToActive = () => {
    setTimeout(() => {
      const active = document.getElementById("palette-active-item");
      if (active) {
        active.scrollIntoView({ block: "nearest", behavior: "smooth" });
      }
    }, 50);
  };
  window.addEventListener("keydown", (event) => {
    const key = event.key?.toLowerCase();
    if ((event.metaKey || event.ctrlKey) && key === "k") {
      event.preventDefault();
      trigger();
    }
    if (key === "escape") {
      if (isLightboxOpen()) {
        closeLightbox();
      } else {
        close();
      }
    }
    if (key === "arrowup") {
      event.preventDefault();
      moveUp();
      scrollToActive();
    }
    if (key === "arrowdown") {
      event.preventDefault();
      moveDown();
      scrollToActive();
    }
    if (key === "enter") {
      const active = document.activeElement;
      const isInput = active?.tagName === "INPUT";
      if (isInput) {
        event.preventDefault();
        selectActive();
      }
    }
  });
})();
