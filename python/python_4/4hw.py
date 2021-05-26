

#다이아몬드 만들기

#방법 1

star = "*"
for i in range(5):  #0,1,2,3,4
    print(" "*(5-(i+1)),star*(2*i+1)," "*(5-(i+1)))

for j in range(5):  #0,1,2,3,4
    print(" "*(1+j),star*(7-2*j)," "*(1+j))


#방법 2

#star = "*"
#for i in range(1,10,2):  #1,3,5,7,9
#    print(" "*(4-(i-1)//2),star*i," "*(4-(i-1)//2))

#for j in range(7,0,-2): #7,5,3,1
#    print(" " *(1+(7-j)//2), star*j, " "*(1+(7-j)//2))




