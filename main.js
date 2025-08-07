window.addEventListener('scroll', () => {
  const header = document.querySelector('.nav-bar');
  if (header) {
    header.classList.toggle('shrink', window.scrollY > 50);
  }
});

