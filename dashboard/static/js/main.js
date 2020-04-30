const menuBtn = document.querySelector('.menu-btn');
const sidebar = document.querySelector('.sidebar');
const topnav = document.querySelector('.t2b-navbar-primary');
let menuOpen = false;
menuBtn.addEventListener('click', () => {
    if (!menuOpen) {
        menuBtn.classList.add('open');
        sidebar.classList.add('open')
        topnav.classList.add('open');
        // topnav.style.cssText = "left: 250px; transition: 0.3s ease-in;"
        menuOpen = true;
    } 
    else{
        menuBtn.classList.remove('open');
        sidebar.classList.remove('open');
        topnav.classList.remove('open');
        // topnav.style.cssText = "left: 0px; transition: 0.3s ease-out;"
        menuOpen = false;
    }
})