'''
print("# read 이용")
with open("new.txt", 'r') as f:
    data = f.read()    #f.read는 ""안 데이터를 전부 읽는 것
    print(data)

print("# readline 이용")
with open("new.txt", 'r') as f:
    while True:
        line = f.readline()
        if not line: break
        print(line)

print("# readline 이용")
with open("new.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
       print(line)
'''

print("# readline 이용")
with open("new.txt", 'r') as f:
    lines = f.readlines()
    print(type(lines))
    print(lines)