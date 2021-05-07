class food:

    def __init__(self, name, kcal, price, flavor):
        self.name = name
        self.kcal = kcal
        self.price = price
        self.flavor = flavor

    def info(self):
        print(f"이름 : {self.name}")
        print(f"칼로리 : {self.kcal}")
        print(f"가격 : {self.price}")
        print(f"맛 : {self.flavor}")
        print()

    def choice(self, num):
        print(self.flavor[num])


food1 = food('치킨', 2300, 18000, ['후라이드', '시즈닝', '양념'])
food2 = food('피자', 3080, 18000 , ['불고기', '페퍼로니', '하와이안'])
food3 = food('햄버거', 1100, 6000, ['불고기', '새우', '치킨'])

food1.info()
food2.info()
food3.info()

food1.choice(1)
food2.choice(2)
food3.choice(0)
