# 클래스에 두 개의 객체(공격,방어)를 만들어 '캐릭터 싸움'을 구현해주세요.
class char_game():
    def __init__(self,job,hp):
        self.job = job
        self.hp = int(hp)
    def attack(self,enemy):
        enemy.hp -= 10
        print('상대 %s에게 10만큼 피해를 입혔습니다' %enemy.job)
        print('%s : %d  %s : %d'%(self.job,self.hp,enemy.job,enemy.hp))
    # def attack(self):                   #ver2
    #     self.hp = self.hp - 10
    #     print('상대 %s에게 10만큼 피해를 입혔습니다' % self.job)

    def defense(self):
        self.hp -= 5
        print('%s는 5만큼 피해를 입었습니다' %self.job)
        print('%s : %d'%(self.job,self.hp))

soo = char_game('witch',100)
monster = char_game('wizard', 100)
soo.attack(monster)
# monster.attack()
soo.defense()