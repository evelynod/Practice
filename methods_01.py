#If you want to make your class even more flexible,
#  you could let each wizard have a unique name
#  by using what’s called a constructor (__init__ method):

class Wizard:

    def __init__(self, name):
        self.name = name
        self.mana = 50
    
    

    
    def cast_spell(self, cost):
     if self.mana >= cost:
        self.mana -= cost
        print(f"{self.name} just cast a spell!")
        print(f"{self.name} has {self.mana} mana left!")
     else:
        print(f"{self.name} does not have enough mana to cast the spell!")



    def regenerate_mana(self, mana_regen_amount):
        self.mana += mana_regen_amount 
        print(f"Mana Regeneration of {mana_regen_amount}! \n{self.name}'s mana is now {self.mana}!")

fizzy = Wizard("Fizzy")
dizzy = Wizard("Dizzy")


# Before casting a spell, check to see that mana is enough


fizzy.cast_spell(52)
dizzy.cast_spell(3)
fizzy.regenerate_mana(mana_regen_amount = 2)
dizzy.regenerate_mana(mana_regen_amount = 1)
  






# Fizzy Wizard 
# A challenge from Boots on July 29, 2025
# Write a class called "Wizard" with an attribute called mana (start it at 50)
# Then, if you create a wizard and call cast_spell, the mana will decrease as intended!  

# A challenge from Boots: Add a regenerate mana method that increases Fizzy's mana by a certain
# amount.
# Now allow that regenerate mana amount to be changed.