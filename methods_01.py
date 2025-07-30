class Wizard:
    mana = 50

    def cast_spell(self, cost):
        self.mana = self.mana - cost
        print(f"Fizzy has {self.mana} mana left!")

Fizzy = Wizard()  
cost = 5
Fizzy.cast_spell(cost)   



