/* =============================================================
   BASE.JS — sidebar toggle apenas
   Sem lógica de negócio.
   ============================================================= */

'use strict';

const hamburger     = document.getElementById('hamburger');
const sidebarToggle = document.getElementById('sidebarToggle');

function toggleSidebar() {
  document.body.classList.toggle('sb-collapsed');
}

if (hamburger)     hamburger.addEventListener('click', toggleSidebar);
if (sidebarToggle) sidebarToggle.addEventListener('click', toggleSidebar);