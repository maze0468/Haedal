pokemons = ['파이리', '꼬북이', '이상해씨', '피카츄']
print("여기는 태초마을! 함께 여정을 떠날 첫번째 포켓몬을 선택하자")
num = int(input("1.불 2.물 3.풀 4.전기 : "))
if (num<=0) or (num >=5):
    print("숫자를 잘못 입력했습니다.")
else:
    print("당신과 여정을 떠날 포켓몬은 " +pokemons[num-1] +"입니다.")