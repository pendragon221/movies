let menuBtn = document.getElementById('menu-btn')
let mobileMenu = document.getElementById('mobile-menu')

menuBtn.onclick = (e) => {
    e.preventDefault()
    if (mobileMenu.style.display === 'none')
        mobileMenu.style.display = 'block'
    else
        mobileMenu.style.display = 'none'
}