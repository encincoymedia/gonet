/* Desplegables nativos y navegación por páginas; sin dependencias. */
(() => {
  'use strict';
  const header = document.querySelector('.site-header');
  const toggle = document.querySelector('.menu-toggle');
  const navigation = document.querySelector('#navegacion-principal');
  if (!header || !toggle || !navigation) return;
  const desktop = window.matchMedia('(min-width: 1024px)');
  const label = toggle.querySelector('.menu-label');
  const dropdowns = [...header.querySelectorAll('.nav-dropdown')];
  const closeDropdowns = (except = null) => {
    dropdowns.forEach(dropdown => {
      if (dropdown !== except) {
        dropdown.open = false;
        dropdown.querySelector('summary')?.setAttribute('aria-expanded', 'false');
      }
    });
  };
  const setMenu = expanded => {
    toggle.setAttribute('aria-expanded', String(expanded));
    navigation.hidden = !desktop.matches && !expanded;
    if (label) label.textContent = expanded ? 'Cerrar' : 'Menú';
    if (!expanded) closeDropdowns();
  };
  const syncViewport = () => {
    const focusedInside = navigation.contains(document.activeElement);
    toggle.hidden = desktop.matches;
    setMenu(false);
    if (!desktop.matches && focusedInside) toggle.focus();
    else if (desktop.matches && document.activeElement === toggle) navigation.querySelector('summary, a')?.focus();
  };
  toggle.addEventListener('click', () => setMenu(toggle.getAttribute('aria-expanded') !== 'true'));
  dropdowns.forEach(dropdown => {
    dropdown.addEventListener('toggle', () => {
      dropdown.querySelector('summary').setAttribute('aria-expanded', String(dropdown.open));
      if (dropdown.open) closeDropdowns(dropdown);
    });
  });
  document.addEventListener('click', event => {
    if (!header.contains(event.target)) {
      const focusedInside = navigation.contains(document.activeElement);
      setMenu(false);
      if (focusedInside && !desktop.matches) toggle.focus();
    }
  });
  document.addEventListener('keydown', event => {
    if (event.key !== 'Escape') return;
    const openDropdown = dropdowns.find(dropdown => dropdown.open);
    if (openDropdown) {
      closeDropdowns();
      openDropdown.querySelector('summary').focus();
      event.preventDefault();
    } else if (!desktop.matches && toggle.getAttribute('aria-expanded') === 'true') {
      setMenu(false);
      toggle.focus();
      event.preventDefault();
    }
  });
  header.addEventListener('focusout', event => {
    // Sin nuevo destino de foco, esperar al clic exterior para no ocultar
    // el enlace antes de que termine la pulsación del ratón.
    if (event.relatedTarget && !header.contains(event.relatedTarget)) closeDropdowns();
  });
  const currentPath = location.pathname.replace(/\/$/, '') || '/';
  navigation.querySelectorAll('a[href]').forEach(link => {
    const path = new URL(link.href, location.href).pathname.replace(/\/$/, '') || '/';
    if (path === currentPath) link.setAttribute('aria-current', 'page');
  });
  desktop.addEventListener('change', syncViewport);
  syncViewport();
})();
