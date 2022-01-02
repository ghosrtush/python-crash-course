names = ['albert','john','liam']
print(f"{names[0]}, would you like to come to dinner?")
print(f"{names[1]}, would you like to come to dinner?")
print(f"{names[2]}, would you like to come to dinner?")

guest_who_cant_make_it = names.pop()
print(f"{guest_who_cant_make_it.title()}, can't make it to dinner.")

names.append('michael')
print(names)