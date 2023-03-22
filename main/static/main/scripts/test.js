const cartLink = document.getElementById('check-link')
const wrapperListCart = document.getElementById('check-list')

cartLink.addEventListener('click', (event) => {
  if (wrapperListCart.classList.contains('disabled')) {
    wrapperListCart.classList.replace('disabled', 'active')
  } else {
    wrapperListCart.classList.replace('active', 'disabled')
  }
})
