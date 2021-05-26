from random import randint

print("로켓단이 나타났다! '피카츄'로 로켓단을 무찌르자!")
pi_hp = 10 #피카츄, 로켓단의 HP
ro_hp = 10

while True:

    if pi_hp <= 0:
        print("'피카츄'가 쓰러졌다!")
        break

    elif ro_hp <= 0:
        print("'로켓단'이 쓰러졌다!")
        break

    else:
        print("'피카츄'가 시도할 공격을 선택하세요.")
        num1 = int(input("1.몸통박치기 2.아이언테일 3.백만볼트 : "))
        num2 = randint(1, 3)
        print(f"피카츄가 공격했다! 로켓단은 -{num1}의 데미지를 입었다.")
        ro_hp -= num1
        print(f"로켓단이 공격했다! 피카츄는 -{num2}의 데미지를 입었다.")
        pi_hp -= num2
        #continue