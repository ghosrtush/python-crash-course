pizzas = ['meatlovers','chicken','the lot','cheese',"vegitarian","dessert"]

for pizza in pizzas:
    print(f"I like {pizza} pizza")

print('My favourite pizza is from Pizza Capers\n')
print("I do not like the pizza from Dominos")
print("I really like pizza")

print("Three items from the middle of the list are:")
for pizza in pizzas[:3]:
    print(pizza)

print("The first 3 items in the list are:")
for pizza in pizzas[3:]:
    print(pizza)