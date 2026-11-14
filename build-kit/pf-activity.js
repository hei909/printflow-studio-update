/* PrintFlow Studio — activity gate (v2.5)
   Panels only talk to Illustrator while you are using them: mouse over the panel,
   or a click / key press in it during the last few seconds. Docked or idle panels stay silent,
   so Illustrator is never slowed down by panels running in the background. */
(function () {
  "use strict";
  var last = 0, over = false, wake = [], IDLE = 5000;
  function active() { return !document.hidden && (over || Date.now() - last < IDLE); }
  function touch() {
    var was = active(); last = Date.now();
    if (!was) for (var i = 0; i < wake.length; i++) { try { wake[i](); } catch (e) {} }
  }
  var root = document.documentElement;
  root.addEventListener("mouseenter", function () { var was = active(); over = true; last = Date.now(); if (!was) touch(); });
  root.addEventListener("mouseleave", function () { over = false; last = Date.now() - IDLE + 1500; });
  ["mousedown", "keydown", "wheel", "focusin"].forEach(function (t) { document.addEventListener(t, touch, true); });
  window.addEventListener("focus", touch);
  document.addEventListener("visibilitychange", function () { if (!document.hidden) touch(); });
  window.PFActivity = {
    active: active,
    onWake: function (fn) { wake.push(fn); },
    /* like setInterval, but skipped while the panel is idle; runs once right away when you come back */
    every: function (fn, ms) { wake.push(fn); return setInterval(function () { if (active()) fn(); }, ms); }
  };
})();
