const menuBtn = document.querySelector('.menu-btn');
const wrapper = document.querySelector('#wrapper');
let menuOpen = false;
menuBtn.addEventListener('click', () => {
    if (!menuOpen) {
        menuBtn.classList.add('open');
        wrapper.classList.add('toggled');
        menuOpen = true;
    } 
    else{
        menuBtn.classList.remove('open');
        wrapper.classList.remove('toggled');
        menuOpen = false;
    }
})