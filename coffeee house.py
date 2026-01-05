menu=[
    {"item":"cofee","price":5.0},
    {"item":"tea","price":3.0},
    {"item":"cake","price":10}
]


total_bill=0

while True:
    for food in menu:
        print(f"{food['item']} - ${food['price']}")
    food_need=input("Enter item name (or 'quit' to finish): ")

    if food_need=="quit":
       break
    else:
        for food in menu:
         if food["item"] == food_need:
            total_bill += food["price"]
            print(f"Added {food_need} to order.")
            found = True
            break
         if not found:
           print("sorry Item not found!")


print(f"Total bill: {total_bill}")


