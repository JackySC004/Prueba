class Tuvieja:
    def __init__(self,raza):
        self.raza=raza
    def cocinar(self):
        return "altas milanesas"
    
uff_tuvieja = Tuvieja(raza="el amor de mi vida xd")

print(uff_tuvieja.raza)
print(uff_tuvieja.cocinar())