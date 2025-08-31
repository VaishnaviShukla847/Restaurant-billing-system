#define the mwnu of restaurant
menu =  {
    "Pizza":40,
    "Pasta":70,
    "Coffee":70,
    "Burger":50,
    "Momos":60,
    "Noodles":80,
    "Salad":100,
    "Dosa":85,
}
#greet
print("Welcome to FLAVOUR HEAVEN Restaurant")
print("Here our's menu:")
for item , price in menu.items():
    print(f"{item}: Rs{price}")
# initialised total order cost

order_total = 0
#80 + 70 = 150

item_1 = input("Please enter the name of the item you want to order: ").title()
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item '{item_1}' has been added to your order.")
else:
    print(f"Ordered item '{item_1}' is not available!")
    
another_order = input("Do you want to add another item? (Yes/No): ").strip().lower()
if another_order == "yes":
    item_2 = input("Please enter the name of another item: ").title()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item '{item_2}' has been added to your order.")
    else:
        print(f"Ordered item '{item_2}' is not available!")

print(f"The total amount of the item to pay is Rs{order_total}:")
print("Thanks for the order") 
