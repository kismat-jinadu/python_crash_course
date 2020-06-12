def describe_pet(animal_type,pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster','harry')
describe_pet('dog','willie')

#make sure the order of the arguments are correct. however keywords can be used in any order

describe_pet(animal_type='hamster',pet_name ='harry')
describe_pet(pet_name ='harry',animal_type='hamster')

#default values can be defined
def describe_pet(pet_name,animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')
describe_pet('willie')
describe_pet(pet_name='harry', animal_type='hamster')