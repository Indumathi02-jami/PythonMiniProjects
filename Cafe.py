menu={
    'PIZZA':40,
    'PASTA':50,
    'BURGER':60,
    'SALAD':70,
    'COFFEE':80
}
#print(menu)
print("Welcome to PYTHON Restaurant")
print("Pizza : Rs40\n Pasta: Rs50 \n Burger: Rs60\n Salad: Rs70\n Coffee: Rs80 ")
order_total=0
item_1=input("Enter the name of the item you want to order:").upper()
if item_1 in menu:
    order_total+= menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not avaialabe yet!")
another_order=input("Do you want to add another item?(Yes/No)").upper()
while(another_order=="Yes"):
    
    item_2=input("Enter the name of the item you want to order:").upper()
    if item_2 in menu:
        order_total+= menu[item_2]
        print(f"Your item {item_2} has been added to your order")

    else:
        print(f"Ordered item {item_2} is not avaialabe yet!")
    another_order=input("Do you want to add another item?(Yes/No)")
print(f"The total amount of items is {order_total}")