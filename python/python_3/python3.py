#input+print

#a = 2+3
#print(a)
#print(2+3)

#my_pocketmon = input("당신이 가진 포켓몬은?")
#print(my_pocketmon)


#########


#function

def catch():
    print("잡았다!")

catch() #함수 호출(정리해놓은 함수 호출)

#매개변수 사용하는 함수
#매개변수: 함수 내에서 사용, 인자: 함수를 호출할 때 사용
def add(num1, num2):
    return num1 + num2  #num1, num2는 매개변수
print(add(1,2))  #1, 2는 인자

def add_mul(num1,num2):
    return num1 + num2, num1 * num2
print(add_mul(1,2))

def attack(name):
    print(name, "100만 볼트")
    print(name, "전광석화")
    print(name, "번개")

attack("피카츄")
attack("라이츄")
attack("피츄")