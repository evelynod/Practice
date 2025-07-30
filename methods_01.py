class Wizard:
    mana = 50

    def cast_spell(self, cost):
        self.mana = self.mana - cost
        print(f"Fizzy has {self.mana} mana left!")



    def regenerate_mana(self):
        self.mana += 1      #increases mana by 1
        print(f"Mana Regeneration! Fizzy's mana is now {self.mana}!")

Fizzy = Wizard()  
cost = 5
Fizzy.cast_spell(cost)  

Fizzy.regenerate_mana()



# Fizzy Wizard 
# A challenge from Boots on July 29, 2025
# Write a class called "Wizard" with an attribute called mana (start it at 50)
# Then, if you create a wizard and call cast_spell, the mana will decrease as intended!  