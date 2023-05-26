let menuBtn = document.getElementById('menu-btn')
let mobileMenu = document.getElementById('mobile-menu')

menuBtn.onclick = (e) => {
    e.preventDefault()
    console.log(mobileMenu.style.display)
    let display = mobileMenu.style.display
    if (display === 'none' || mobileMenu.classList.contains('hidden')) {
        mobileMenu.style.display = 'block'
        mobileMenu.classList.remove('hidden')
    }
    else
        mobileMenu.style.display = 'none'
}