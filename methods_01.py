class Wizard:
    mana = 50
    

    def cast_spell(self, cost):
        self.mana = self.mana - cost
        print(f"Fizzy has {self.mana} mana left!")



    def regenerate_mana(self, mana_regen_amount):
        self.mana += mana_regen_amount 
        print(f"Mana Regeneration of {mana_regen_amount}! \nFizzy's mana is now {self.mana}!")

Fizzy = Wizard()  
cost = 5
Fizzy.cast_spell(cost)  
mana_regen_amount = 2

Fizzy.regenerate_mana(mana_regen_amount)



# Fizzy Wizard 
# A challenge from Boots on July 29, 2025
# Write a class called "Wizard" with an attribute called mana (start it at 50)
# Then, if you create a wizard and call cast_spell, the mana will decrease as intended!  

# A challenge from Boots: Add a regenerate mana method that increases Fizzy's mana by a certain
# amount.
# Now allow that regenerate mana amount to be changed.