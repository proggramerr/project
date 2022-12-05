const Burger = document.querySelector('.Burger')
const Menu = document.querySelector('.Menu')
const Info = document.querySelector('.Info')


Burger.addEventListener('click', () => {
    Burger.classList.toggle('active');
    Menu.classList.toggle('active');
    // Info.style.display = 'none';
} )

document.querySelectorAll('.Menu li').forEach(n => n.addEventListener('click', () => {
    Burger.classList.remove('active');
    Menu.classList.remove('active');
    // Info.removeAttribute('style', '');
}))

// if (Burger.className == 'Burger active'){
//     Info.style.display = 'none';
// }

window.onscroll = function showHeader () {
    const Header = document.querySelector('.Header_line');
    if (Menu.className == "Menu active"){
        Header.classList.add('fix');
    }

    if ((window.pageYOffset > 800) && (Header.className != "Header_line fix"))
    {
        Header.classList.add('fixed');
    }
}

const openPopUp = document.getElementById('OpenPopUp');
const closePopUp = document.getElementById('PopUpClose');
const popUp = document.getElementById('PopUp');
const openPopUp1 = document.getElementById('OpenPopUp1');
const html = document.getElementsByClassName('html')


openPopUp.addEventListener('click', function(e){
    e.preventDefault();
    popUp.classList.add('active');
    document.body.style.overflow = 'hidden';
})

openPopUp1.addEventListener('click', function(e){
    e.preventDefault();
    popUp.classList.add('active');
    document.body.style.overflow = 'hidden';
})

closePopUp.addEventListener('click',  () => {
    popUp.classList.remove('active');
    document.body.style.overflow = 'visible';
}) 