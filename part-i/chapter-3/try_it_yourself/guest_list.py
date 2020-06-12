guest_list=['Beyonce','Serena','Michelle']
print(f"My dear {guest_list[0]}, you are cordially invited to dinner with Kismat")
print(f"My dear {guest_list[1]}, you are cordially invited to dinner with Kismat")
print(f"My dear {guest_list[2]}, you are cordially invited to dinner with Kismat")

cant_make_it=guest_list.pop(2)
print(f"{cant_make_it} can not make it")
guest_list.insert(2,'Ellen')
print(f"My dear {guest_list[0]}, you are cordially invited to dinner with Kismat")
print(f"My dear {guest_list[1]}, you are cordially invited to dinner with Kismat")
print(f"My dear {guest_list[2]}, you are cordially invited to dinner with Kismat")

print("All, I have found a bigger table. I will add some more to the party")

guest_list.insert(0,'Stevie')
guest_list.insert(2,'Roger')
guest_list.append('RBG')
print(f"My dear {guest_list[0]}, you are cordially invited to dinner with Kismat")
print(f"My dear {guest_list[1]}, you are cordially invited to dinner with Kismat")
print(f"My dear {guest_list[2]}, you are cordially invited to dinner with Kismat")
print(f"My dear {guest_list[3]}, you are cordially invited to dinner with Kismat")
print(f"My dear {guest_list[4]}, you are cordially invited to dinner with Kismat")
print(f"My dear {guest_list[5]}, you are cordially invited to dinner with Kismat")

print("I'm sorry guys, we lost the big table. I can only invite two")
reject_list=guest_list.pop(4)
print(f"I'm sorry {reject_list}, I'm unable to invite you to dinner anymore")
reject_list=guest_list.pop(4)
print(f"I'm sorry {reject_list}, I'm unable to invite you to dinner anymore")
reject_list=guest_list.pop(0)
print(f"I'm sorry {reject_list}, I'm unable to invite you to dinner anymore")
reject_list=guest_list.pop(1)
print(f"I'm sorry {reject_list}, I'm unable to invite you to dinner anymore")
print(f"My dear {guest_list[0]}, you are still invited to dinner with Kismat")
print(f"My dear {guest_list[1]}, you are still invited to dinner with Kismat")
del guest_list[1]
del guest_list[0]
print(guest_list)

guest_list=['Beyonce','Serena','Michelle']

print(f"The number of guests are {len(guest_list)}")