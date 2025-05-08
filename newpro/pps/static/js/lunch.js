
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
// Open popup with selected food details
function openPopupWithCheckedItems() {
    const checkedItems = Array.from(document.querySelectorAll('.checkbox-type input:checked'));
    const selectedItemsContainer = document.getElementById('selectedItems');
    selectedItemsContainer.innerHTML = '';

    if (checkedItems.length === 0) {
        alert('Please select at least one item.');
        return;
    }

    checkedItems.forEach((checkbox, index) => {
        const lunchItem = checkbox.closest('.lunch1');
        const foodName = lunchItem.querySelector('h3').innerText;
        const price = parseFloat(lunchItem.querySelector('.price').innerText);

        const itemDiv = document.createElement('div');
        itemDiv.classList.add('selected-item');
        itemDiv.innerHTML = `
            <p><strong>${foodName}:</strong> <span class="item-price">${price.toFixed(2)}</span> birr</p>
            <label for="quantity${index}">Quantity:</label>
            <input type="number" id="quantity${index}" min="0" value="1" onchange="updateItemPrice(${index}, ${price})">
            <button class="remove-item" onclick="removeSelectedItem(${index})">X</button>
        `;
        selectedItemsContainer.appendChild(itemDiv);

        // Update total immediately based on initial quantity
        updateItemPrice(index, price);
    });

    updatePopupTotal();
    document.getElementById('orderPopup').style.display = 'block';
}

// Update item price and manage SVG, checkbox, and total price immediately
function updateItemPrice(index, price) {
    const quantityInput = document.getElementById(`quantity${index}`);
    const quantity = parseInt(quantityInput.value) || 0;
    const itemPriceElement = document.querySelectorAll('.selected-item')[index]?.querySelector('.item-price');
    const checkbox = document.querySelectorAll('.checkbox-type input')[index];
    const svg = document.querySelectorAll('.checkbox-type svg')[index];

    // Update item price instantly
    const totalItemPrice = price * quantity;
    if (itemPriceElement) {
        itemPriceElement.innerText = totalItemPrice.toFixed(2);
    }

    // Update SVG and checkbox based on quantity
    if (quantity > 0) {
        svg.style.fill = 'green';
        checkbox.disabled = false;
    } else {
        svg.style.fill = 'red';
        checkbox.disabled = true;
        checkbox.checked = false;
    }

    // Immediately update total price
    updatePopupTotal();
}

// Update the total price based on all quantities
function updatePopupTotal() {
    let total = 0;
    document.querySelectorAll('.selected-item').forEach(item => {
        const itemPrice = parseFloat(item.querySelector('.item-price').innerText) || 0;
        total += itemPrice;
    });
    document.getElementById('popupTotalPrice').innerText = `${total.toFixed(2)} birr`;
}

// Remove a selected item and update the total price immediately
function removeSelectedItem(index) {
    const selectedItems = document.querySelectorAll('.selected-item');
    const itemToRemove = selectedItems[index];

    if (itemToRemove) {
        itemToRemove.remove();

        // Reset checkbox and SVG
        const checkbox = document.querySelectorAll('.checkbox-type input')[index];
        const svg = document.querySelectorAll('.checkbox-type svg')[index];

        if (checkbox) {
            checkbox.disabled = true;
            checkbox.checked = false;
            svg.style.fill = 'red';
        }

        updatePopupTotal(); // Update total immediately after removing an item
    }
}

// Place order after validation
function placeOrder() {
    const firstName = document.getElementById('popupFirstName').value.trim();
    const lastName = document.getElementById('popupLastName').value.trim();
    const phone = document.getElementById('popupPhoneNumber').value.trim();
    const selectedItems = document.querySelectorAll('.selected-item');

    if (!firstName || !lastName || !phone) {
        alert('Please enter your first name, last name, and phone number.');
        return;
    }

    if (selectedItems.length === 0) {
        alert('Please select at least one item.');
        return;
    }
    alert('Order placed successfully!');
    closePopup();
}

// Close the popup form
function closePopup() {
    document.getElementById('orderPopup').style.display = 'none';
}

// Initialize order buttons
document.querySelectorAll('.order').forEach(button =>
    button.addEventListener('click', openPopupWithCheckedItems)
);
// Initialize SVG and checkbox behavior on page load
document.querySelectorAll('.checkbox-type input').forEach((checkbox, index) => {
    const svg = document.querySelectorAll('.checkbox-type svg')[index];
    const quantityInput = document.getElementById(`quantity${index}`);

    const initialQuantity = quantityInput ? parseInt(quantityInput.value) : 0;
    if (initialQuantity > 0) {
        svg.style.fill = 'green';
        checkbox.disabled = false;
    } else {
        svg.style.fill = 'red';
        checkbox.disabled = true;
        checkbox.checked = false;
    }

    // Optional: Update SVG when checkbox changes
    checkbox.addEventListener('change', () => {
        svg.style.fill = checkbox.checked ? 'green' : 'red';
    });
});
