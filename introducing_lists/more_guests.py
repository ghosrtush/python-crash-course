names = ['albert','john','liam']
print(f"{names[0]}, would you like to come to dinner?")
print(f"{names[1]}, would you like to come to dinner?")
print(f"{names[2]}, would you like to come to dinner?")

guest_who_cant_make_it = names.pop()
print(f"{guest_who_cant_make_it.title()}, can't make it to dinner.")

names.append('michael')
print(f"{names[2].title()}, would you like to come to dinner?")

print("We have found a bigger table!")

names.insert(0,'bob')
names.insert(2,'armin')
names.append('jacob')

print(f"{names[0]}, would you like to come to dinner?")
print(f"{names[1]}, would you like to come to dinner?")
print(f"{names[2]}, would you like to come to dinner?")
print(f"{names[3]}, would you like to come to dinner?")
print(f"{names[4]}, would you like to come to dinner?")

