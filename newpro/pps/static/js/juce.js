
function addToCart(itemId, itemName, itemPrice) {
    fetch('/add-to-cart/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()  // Ensure CSRF token is included
        },
        body: JSON.stringify({
            id: itemId,
            name: itemName,
            price: itemPrice
        })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message); // Show confirmation
    })
    .catch(error => console.error('Error:', error));
}

// Function to get CSRF token from cookies
function getCSRFToken() {
    let cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        let cookie = cookies[i].trim();
        if (cookie.startsWith('csrftoken=')) {
            return cookie.substring('csrftoken='.length, cookie.length);
        }
    }
    return '';
}


const find=document.getElementById("search-input");
find.addEventListener("keyup", function() {
    let input = find.value.toLowerCase();
    let items = document.querySelectorAll(".lunch1");

    items.forEach(item => {
        let itemName = item.querySelector(".name h3").textContent.toLowerCase();

        if (itemName.includes(input)) {
            item.style.display = "block";
            
        } else {
            item.style.display = "none";
        }
    });
});
const cart=document.getElementById("cart");
const cartContainer=document.getElementById("cartContainer")
const lunch=document.getElementById("lunch-dinner-container");
cart.addEventListener("click",()=>{
    cartContainer.style.right = '0';
    
const closeCart=document.getElementById("closeCart");
})
closeCart.addEventListener("click",()=>{
    cartContainer.style.right = '-400px';
})
//search bar

const finded=document.getElementById("search-input");
finded.addEventListener("keyup", function() {
    let input = finded.value.toLowerCase();
    let items = document.querySelectorAll(".lunch1");

    items.forEach(item => {
        let itemName = item.querySelector(".name h3").textContent.toLowerCase();

        if (itemName.includes(input)) {
            item.style.display = "block";
            
        } else {
            item.style.display = "none";
        }
    });
});