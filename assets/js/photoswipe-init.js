(function () {
  var attempts = 0;
  var maxAttempts = 40;

  function ensureStylesheet(href) {
    if (document.querySelector('link[data-pswp-href="' + href + '"]')) return Promise.resolve();
    return new Promise(function (resolve) {
      var link = document.createElement('link');
      link.rel = 'stylesheet';
      link.href = href;
      link.setAttribute('data-pswp-href', href);
      link.onload = resolve;
      link.onerror = resolve;
      document.head.appendChild(link);
    });
  }

  function ensureScript(src) {
    if (document.querySelector('script[data-pswp-src="' + src + '"]')) return Promise.resolve();
    return new Promise(function (resolve) {
      var script = document.createElement('script');
      script.src = src;
      script.async = true;
      script.setAttribute('data-pswp-src', src);
      script.onload = resolve;
      script.onerror = resolve;
      document.body.appendChild(script);
    });
  }

  function setupTrendLightbox() {
    if (!window.PhotoSwipe || !window.PhotoSwipeUI_Default) return false;
    var pswpElement = document.querySelector('.pswp');
    if (!pswpElement) return false;
    var containers = Array.prototype.slice.call(document.querySelectorAll('.trend-image'));
    if (!containers.length) return false;

    var items = containers.map(function (container) {
      var img = container.querySelector('img');
      return {
        src: img ? img.getAttribute('src') : null,
        msrc: img ? img.getAttribute('src') : null,
        w: img ? (img.naturalWidth || img.width || 1200) : 1200,
        h: img ? (img.naturalHeight || img.height || 800) : 800,
        el: img
      };
    });

    function openGallery(index) {
      var item = items[index];
      if (!item || !item.el) return;
      item.w = item.el.naturalWidth || item.el.width || item.w;
      item.h = item.el.naturalHeight || item.el.height || item.h;
      var gallery = new PhotoSwipe(pswpElement, PhotoSwipeUI_Default, items, {
        bgOpacity: 0.9,
        closeOnScroll: true,
        fullscreenEl: false,
        history: false,
        shareEl: false,
        zoomEl: false,
        index: index,
        getThumbBoundsFn: function (i) {
          var thumbnail = items[i].el;
          var pageYScroll = window.pageYOffset || document.documentElement.scrollTop;
          var rect = thumbnail.getBoundingClientRect();
          return { x: rect.left, y: rect.top + pageYScroll, w: rect.width };
        }
      });
      gallery.init();
    }

    containers.forEach(function (container, index) {
      if (container.dataset.pswpBound === 'true') return;
      container.dataset.pswpBound = 'true';
      container.addEventListener('click', function (event) {
        if (event.target && event.target.closest('a')) return;
        openGallery(index);
      });
    });

    return true;
  }

  function attemptSetup() {
    ensureStylesheet('https://cdnjs.cloudflare.com/ajax/libs/photoswipe/4.1.3/photoswipe.min.css')
      .then(function () {
        return ensureStylesheet('https://cdnjs.cloudflare.com/ajax/libs/photoswipe/4.1.3/default-skin/default-skin.min.css');
      })
      .then(function () {
        return ensureScript('https://cdnjs.cloudflare.com/ajax/libs/photoswipe/4.1.3/photoswipe.min.js');
      })
      .then(function () {
        return ensureScript('https://cdnjs.cloudflare.com/ajax/libs/photoswipe/4.1.3/photoswipe-ui-default.min.js');
      })
      .then(function () {
        var ready = setupTrendLightbox();
        if (!ready && attempts < maxAttempts) {
          attempts += 1;
          setTimeout(attemptSetup, 100);
        }
      });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', attemptSetup);
  } else {
    attemptSetup();
  }
  window.addEventListener('pageshow', attemptSetup);
})();
