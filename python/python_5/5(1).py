#1번 예제
#f = open( "new.txt", 'w')
#f.close()

#2번 예제
f = open("new.txt", 'w')
for i in range(10):
    data = "피카츄는 푹 쉬었다! 체력이 %d가 되었다" %i
    f.write(data)
    f.write("\n")
f.close()