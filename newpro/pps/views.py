from django.shortcuts import render
from .models import fooditem ,drinkitem, Order 
from django.http import JsonResponse



# Create your views here.
def home(request):
  
    return render(request,'index.html',)

def juicee(request):
    breaks=drinkitem.objects.filter(Dstatus='juice')
    context={
        'breaks':breaks
    }
    return render(request,'juice.html',context)
def drink(request):
    breaks=drinkitem.objects.filter(Dstatus='hot_drink')
    context={
        'breaks':breaks
    }
    return render(request,'hotdrink.html',context)

def lunch(request):
    breaks=fooditem.objects.filter(Fstatus='lunch_and_dinner')
    context={
        'breaks':breaks
    }

    return render(request,'lunch.html',context)


def breakfast(request):
    breaks=fooditem.objects.filter(Fstatus='breakfast')
    context={
        'breaks':breaks
    }

    return render(request,'breakFast.html',context)
      
def order_success(request):
    return render(request, "order_success.html")

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Order

@csrf_exempt  # Use @csrf_protect if you're using CSRF tokens in JavaScript
def place_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        customer_name = data.get('customer_name')
        phone_number = data.get('phone_number')
        items = data.get('items', [])  # List of selected food and drink items
        total_price = data.get('total_price', 0)

        # Convert the items to JSON string and save the order
        items_json = json.dumps(items)

        order = Order.objects.create(
            customer_name=customer_name,
            phone_number=phone_number,
            items=items_json,
            total_price=total_price
        )

        return JsonResponse({'message': 'Order placed successfully!'}, status=201)

    return JsonResponse({'error': 'Invalid request'}, status=400)



import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def add_to_cart(request):
    if request.method == 'POST':
        try:
            cart = request.session.get('cart', {})
            data = json.loads(request.body)

            item_id = data.get('id')
            item_name = data.get('name')
            item_price = float(data.get('price'))

            # 🛠 Try to guess type based on ID or incoming data
            item_type = data.get('type')
            if not item_type:
                try:
                    fooditem.objects.get(id=item_id)
                    item_type = 'food'
                except fooditem.DoesNotExist:
                    item_type = 'drink'

            if not item_id or not item_name or not item_price:
                return JsonResponse({'error': 'Missing item data!'}, status=400)

            if item_id in cart:
                cart[item_id]['quantity'] += 1
            else:
                cart[item_id] = {
                    'id': item_id,
                    'name': item_name,
                    'price': item_price,
                    'type': item_type,
                    'quantity': 1
                }

            request.session['cart'] = cart
            request.session.modified = True

            return JsonResponse({'message': f'{item_name} added to cart!', 'cart': cart})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON!'}, status=400)

    return JsonResponse({'error': 'Invalid request'}, status=400)




def cart_view(request):
    cart = request.session.get('cart', {})
    total_price = sum(item['price'] * item['quantity'] for item in cart.values())

    return render(request, 'cart.html', {'cart': cart, 'total_price': total_price})
import json
from django.shortcuts import render, redirect
from .models import Order
from typing import List, Dict

def checkout(request):
    cart = request.session.get('cart', {})

    if not cart:
        return redirect('cart')

    total_price = sum(item['price'] * item['quantity'] for item in cart.values())

    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        phone_number = request.POST.get('phone_number')
        
        
        
        items_for_order: List[Dict[str, any]] = [
            {"name": item["name"], "quantity": item["quantity"]}
            for item in cart.values()
        ]

        try:
            print(f"[DEBUG] Creating order for {customer_name}, phone: {phone_number}")
            order = Order.objects.create(
                customer_name=customer_name,
                phone_number=phone_number,
                items=json.dumps(items_for_order),
                total_price=total_price
            )

            for cart_item in cart.values():
                item_id = int(cart_item['id'])
                quantity = cart_item['quantity']
                print(f"[DEBUG] Processing item: {cart_item['name']} | Type: {cart_item['type']} | Qty: {quantity}")

                if cart_item['type'] == 'food':
                    item = fooditem.objects.get(id=item_id)
                elif cart_item['type'] == 'drink':
                    item = drinkitem.objects.get(id=item_id)
                else:
                    continue

                print(f"[DEBUG] Available stock: {item.quantity}")
                if item.quantity >= quantity:
                    item.quantity -= quantity
                    item.save()
                    print(f"[DEBUG] New stock: {item.quantity}")
                else:
                    return render(request, 'checkout.html', {
                        'cart': cart,
                        'total_price': total_price,
                        'error': f"Not enough stock for {item.name}. Only {item.quantity} left."
                    })

            request.session['cart'] = {}
            request.session.modified = True
            order.items_for_order = json.loads(order.items)  # Convert JSON string back to Python list

            return render(request, 'order-success.html', {'order': order})

        except Exception as e:
            print(f"[ERROR] {str(e)}")
            return render(request, 'checkout.html', {
                'cart': cart,
                'total_price': total_price,
                'error': f"Error processing order: {str(e)}"
            })

    return render(request, 'checkout.html', {'cart': cart, 'total_price': total_price})
