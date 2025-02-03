const darkModeToggle = document.getElementById('dark-mode-toggle');

darkModeToggle.addEventListener('click', () => {
document.body.classList.toggle('dark-mode');
});

document.querySelectorAll('nav a').forEach(link => {
link.addEventListener('click', event => {
event.preventDefault();
const targetId = link.getAttribute('href');
const targetSection = document.querySelector(targetId);
const sections = document.querySelectorAll('main section');
sections.forEach(section => section.style.display = 'none');
targetSection.style.display = 'block';
});
});