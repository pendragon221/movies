let menuBtn = document.getElementById('menu-btn')
let mobileMenu = document.getElementById('mobile-menu')

menuBtn.onclick = (e) => {
    e.preventDefault()
    if (mobileMenu.classList.contains('hidden')) {
        mobileMenu.classList.remove('hidden')
    }
    else
        mobileMenu.classList.add('hidden')
}