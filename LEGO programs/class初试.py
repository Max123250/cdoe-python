class Hero():
    hp = 100
    atk = 20
    shield = 50
    def atk(self):
        return self.atk
    def be_atk(self,num = 0):
        if self.shield != 0:
            if self.shield > num:
                self.shield -= num
            else:
                last_num = num - self.shield
                self.shield = 0
                self.hp -= last_num
        else:
            self.hp -= num
        if self.hp <= 0:
            return True
        else:
            return [self.shield,self.hp]
class Tank(Hero):
    hp = 500
    shield = 100
    atk = 10
hero = Hero()
tank = Tank()
hp = hero.be_atk(100)
thp = tank.be_atk(100)
print(hp)
print(thp)
