import random

class base_roller():

    def init(self, dice_amt=1, dice_sides=20):
        self.dice = dice_amt
        self.sides = dice_sides

    def roll(self):
        return random.randint(1,self.sides)

    def double_roll(self, type_of_roll):
        """
        The double roll function will handle anything that
        needs to be rolled for advantage or disadvantage.
        If for advantage, it will return the greater of the
        two numbers, else it will return the lesser of the
        two.

        Valid strings for type_of_roll are 'adv' and 'dis'
        for advantage and disadvantage respectively.
        """

        roll_1, roll_2 = self.roll(), self.roll()

        if   type_of_roll == "adv": return max(roll_1, roll_2)
        elif type_of_roll == "dis": return min(roll_1, roll_2)
        else:                       return "Unknown roll type"

    def stealth_roll(self):
        """
        Basically an advantage roll. Doing a 
        double roll here. This function is 
        purely for ease of understanding.
        """
        return double_roll("adv")

def temp(type_of_roll='adv'):
    roll_1 = random.randint(1,20)
    roll_2 = random.randint(1,20)
    if   type_of_roll == "adv": return max(roll_1, roll_2)
    elif type_of_roll == "dis": return min(roll_1, roll_2)
    else                      : return "Unknown roll type"

print(temp())