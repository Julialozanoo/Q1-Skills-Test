from pyscript import display, document

def ordering_form(e):
    item1 = document.getElementById('menu1')
    item2 = document.getElementById('menu2')
    item3 = document.getElementById('menu3')
    item4 = document.getElementById('menu4')
    item5 = document.getElementById('menu5')

    total = 0
    for item in [item1, item2, item3, item4, item5]:
        if item.checked:
            total += float(item.value)

    name = document.getElementById("name").value
    address = document.getElementById("address").value
    number = document.getElementById("number").value

    document.getElementById("output").innerHTML = ""

    receipt = f"""
    Name: {name}
    Address: {address}
    Phone: {number}
    Total Amount: ₱{total:.2f}
    """

    display(receipt, target="output")
