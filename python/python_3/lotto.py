import random

numbers = range(1, 46) #1~45의 정수

#random, sample(a, n): a에서 랜덤한 n개의 데이터를 추출하는 함수
lotto = random. sample(numbers, 6)
print(lotto)
print(f'오늘의 행운의 로또는 {sorted(lotto)}입니다')