const assert = require('node:assert/strict');
const { readFileSync } = require('node:fs');
const { join } = require('node:path');
const { test } = require('node:test');
const vm = require('node:vm');

function navigationFixture() {
  const frames = [];
  const target = () => ({
    listeners: {},
    addEventListener(type, listener) {
      (this.listeners[type] ||= []).push(listener);
    },
    emit(type, event) {
      for (const listener of this.listeners[type] || []) listener(event);
    },
    setAttribute() {},
  });
  const document = target();
  const header = target();
  const navigation = target();
  const toggle = target();
  const summary = target();
  const productLink = {};
  const outside = {};
  const dropdown = { open: false, querySelector: () => summary, ...target() };
  const inside = new Set([header, navigation, toggle, summary, productLink]);
  header.contains = element => inside.has(element);
  header.querySelectorAll = () => [dropdown];
  toggle.querySelector = () => ({ textContent: 'Menú' });
  navigation.contains = element => inside.has(element);
  navigation.querySelectorAll = () => [];
  document.querySelector = selector => ({
    '.site-header': header,
    '.menu-toggle': toggle,
    '#navegacion-principal': navigation,
  })[selector];
  document.activeElement = summary;
  vm.runInNewContext(readFileSync(join(__dirname, '../script.js'), 'utf8'), {
    document,
    window: { matchMedia: () => ({ matches: true, addEventListener() {} }) },
    location: { pathname: '/' },
    requestAnimationFrame: callback => frames.push(callback),
  });
  dropdown.open = true;
  return {
    document, header, dropdown, productLink, outside,
    flushFrames: () => { while (frames.length) frames.shift()(); },
  };
}

test('A pointer focus change with no related target keeps the product link available', () => {
  const fixture = navigationFixture();
  fixture.document.activeElement = fixture.outside;
  fixture.header.emit('focusout', { relatedTarget: null });
  fixture.flushFrames();
  assert.equal(fixture.dropdown.open, true);
});

test('Keyboard focus leaving the header closes the dropdown', () => {
  const fixture = navigationFixture();
  fixture.document.activeElement = fixture.outside;
  fixture.header.emit('focusout', { relatedTarget: fixture.outside });
  fixture.flushFrames();
  assert.equal(fixture.dropdown.open, false);
});

test('Moving focus to the product link keeps the dropdown open', () => {
  const fixture = navigationFixture();
  fixture.document.activeElement = fixture.productLink;
  fixture.header.emit('focusout', { relatedTarget: fixture.productLink });
  fixture.flushFrames();
  assert.equal(fixture.dropdown.open, true);
});

test('Clicking outside still closes the dropdown', () => {
  const fixture = navigationFixture();
  fixture.document.activeElement = fixture.outside;
  fixture.document.emit('click', { target: fixture.outside });
  assert.equal(fixture.dropdown.open, false);
});
