line = input()

test = False

for i in range(len(line)//2):
    if line[i] == line[-(i+1)]:
        test = True
    else:
        test = False
        break
    
if test or len(line) == 1:
    print(1)
else:
    print(0)