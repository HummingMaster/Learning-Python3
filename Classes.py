class Enemy:
    life = 5

    def __init__(self, hp):
        self.hp = hp

    def get_energy(self):
        print(self.hp)

    def attack(self):
        print("Ouch! I'm gonna get you back...")
        self.life -= 1

    def check_life(self):
        if self.life <= 0:
            print("You killed the enemy")
        else:
            print(str(self.life) + " life points left in enemy")

# enemy1 = Enemy(5)
# enemy_boss = Enemy(20)

# enemy1.get_energy()
# enemy_boss.get_energy()


class Girl:
    gender = 'Female'

    def __init__(self, name):
        self.name = name

girl1 = Girl('Rachel')
girl2 = Girl('Rain')

# print(girl1.gender)
# print(girl2.name)


