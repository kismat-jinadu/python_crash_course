class Die:
    """representation of a die"""
    def __init__(self,sides=6):
        """initialise the die features"""
        self.sides = sides
        self.number_roll = 1

    def roll_die(self,roll):
        """simulate die roll and print random number"""
        self.number_roll =roll
        from random import randint
        print(randint(1,self.sides))

    def ten_sided_die(self):
        """define a ten sided die"""
        self.sides = 10

    def twenty_sided_die(self):
        """define a twenty sided die"""
        self.sides = 20

new_die=Die()
new_die.roll_die(10)
new_die.ten_sided_die()
new_die.roll_die(10)
new_die.twenty_sided_die()
new_die.roll_die(10)



