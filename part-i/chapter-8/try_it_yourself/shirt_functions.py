def make_shirt(size, text):
    """Display shirt size and text"""
    print(f"You have chosen a {size} shirt")
    print(f"The text to be printed on it is: {text.title()}")

def order_shirt(
            style, size, 
            colour, fabric,length):
            """order new shirt based on style, size, colour, fabric,length"""
            print("\nYou have ordered a shirt with the following spec:")
            print(f"Style:{style.title()}")
            print(f"Size:{size.title()}")
            print(f"Colour:{colour.title()}")
            print(f"Fabric:{fabric.title()}")
            print(f"Length:{length}")