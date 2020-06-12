while True:
    age = input("How old are you? ")
    age = int(age)

    if age <=3:
        print(f"\tThe ticket is free")
    elif 3<age<12:
        print(f"\tThe ticket is $10")
    elif age >= 12:
        print(f"\tThe ticket is $15")