/* Solo las anclas corporativas; la navegación compartida procede de GoBuilder. */
(() => {
  'use strict';
  const navigation = document.querySelector('#navegacion-principal');
  const toggle = document.querySelector('.menu-toggle');
  if (!navigation || !toggle) return;
  navigation.querySelectorAll('a[href*="#"]').forEach(link => {
    link.removeAttribute('aria-current');
  });
  navigation.addEventListener('click', event => {
    const link = event.target.closest('a[href]');
    if (!link) return;
    const url = new URL(link.href, location.href);
    if (url.origin !== location.origin || url.pathname !== location.pathname || !url.hash) return;
    if (toggle.getAttribute('aria-expanded') === 'true') toggle.click();
    navigation.querySelectorAll('details[open]').forEach(item => { item.open = false; });
    const target = document.getElementById(decodeURIComponent(url.hash.slice(1)));
    target?.focus({preventScroll: true});
  });
})();
