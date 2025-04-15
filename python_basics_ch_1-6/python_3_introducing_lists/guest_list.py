guest_list = ['George', 'Tom', 'Nathaniel']
print(guest_list)

print(f"Hey, {guest_list[0].title()}! Come work out with us. It'll be great!")
print(f"Hey, {guest_list[1].title()}! Come work out with us. It'll be great! {guest_list[0].title()} is coming, too.")
print(f"Hey, {guest_list[2].title()}! Come work out with us. It'll be great! {guest_list[0].title()} and {guest_list[1].title()} are coming, too.")

#Changing guest list.
print(guest_list[1])

#modify the list by replacing a name with a different name.
guest_list[1] = 'Sam'
print(guest_list)

print(f"Hey, {guest_list[0].title()}! Come to the workout! {guest_list[1].title()} and {guest_list[2].title()} will be there.")
print(f"Hey, {guest_list[1].title()}! Come to our workout! {guest_list[0].title()} and {guest_list[2].title()} will be there.")
print(f"Hey, {guest_list[2].title()}! Come to the workout! {guest_list[0].title()} and {guest_list[1].title()} will be there.")

#more guests!
print(f"Hey, Everyone! We got more guys coming the workout!")

guest_list.insert(0, 'William')
print(guest_list)
guest_list.insert(2, 'Joseph')
guest_list.append('Zack')
print(guest_list)

print(f"Hey, {guest_list[0].title()}! Come to the workout! We got even more guys coming.")
print(f"Hey, {guest_list[1].title()}! Come to the workout! We got even more guys coming.")
print(f"Hey, {guest_list[2].title()}! Come to the workout! We got even more guys coming.")
print(f"Hey, {guest_list[3].title()}! Come to the workout! We got even more guys coming.")
print(f"Hey, {guest_list[4].title()}! Come to the workout! We got even more guys coming.")
print(f"Hey, {guest_list[-1].title()}! Come to the workout! We got even more guys coming.")

#Shrinking guest list
print(f"Hey Guys, bad news. The gym shrunk and only two of you can come. Sorry 'bout that.")

first_out = guest_list.pop(4)
print(f"Hey, {first_out.title()}. Sorry you can't work out with us. Maybe next time.")
print(guest_list)
second_out = guest_list.pop(2)
print(f"Hey, {second_out.title()}. Sorry you can't work out with us. Maybe next time.")
print(guest_list)
third_out = guest_list.pop(-1)
print(f"Hey {third_out.title()}. Sorry you can't work out with us. Maybe next time.")
fourth_out = guest_list.pop()
print(f"Hey {fourth_out.title()}. Sorry you can't work out with us. Maybe next time.")

print(guest_list)

print(f"Hey, {guest_list[0].title()}! Good news! You're still invited. See you there!")
print(f"Hey, {guest_list[1].title()}! Good news! You're still invited. See you there!")

del guest_list[0]
del guest_list[0]

print(guest_list)