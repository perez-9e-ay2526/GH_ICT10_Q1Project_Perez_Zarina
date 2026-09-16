# Calculating the customer's order

from pyscript import document, display

def creating_order(e):

    # Getting order values

    carrot_cake = document.getElementById("carrotcake")
    banana_bread = document.getElementById("bananabread")
    apple_pie = document.getElementById("applepie")
    cherry_turnover = document.getElementById("cherryturnover")
    americano_order = document.getElementById("americano")
    latte_order = document.getElementById("latte")

    # SUBTOTAL
    subtotal = (float(carrot_cake.value) * carrot_cake.checked) + (float(banana_bread.value) * banana_bread.checked) + (float(apple_pie.value) * apple_pie.checked) + (float(cherry_turnover.value) * cherry_turnover.checked) + (float(americano_order.value) * americano_order.checked) + (float(latte_order.value) * 
    latte_order.checked)


    # VAT
    VAT = subtotal * float(0.12)

    #ORDER TOTAL
    total = subtotal + VAT

    #Displaying in HTML
    display(f'Subtotal: PHP {subtotal} <br> VAT: PHP {VAT} <br> Total: PHP {total}', target="receipt")

    document.getElementById('receipt').innerHTML=f'Subtotal: PHP {subtotal} <br> VAT: PHP {VAT} <br> <b>Total:</b> PHP {total}'

def generate_sku(e):

    # Getting input values

    prod_category = document.getElementById("category").value
    prod_name = document.getElementById("prodname").value
    prod_quantity = document.getElementById("stockquan").value

    # Clearing values

    category_val = prod_category.strip()
    name_val = prod_name.strip()
    quantity_val= int(prod_quantity or 0)

    # Reducing values to 3 letters only

    category_SKU = category_val[:3]
    name_SKU = name_val[:3]
    quantity_SKU = quantity_val

    # Displaying values w/ them in uppercase

    sku_display = f'{category_SKU.upper()}-{name_SKU.upper()}-{quantity_SKU}'

    document.getElementById('display').innerHTML=sku_display
    