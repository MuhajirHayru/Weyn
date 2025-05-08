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
