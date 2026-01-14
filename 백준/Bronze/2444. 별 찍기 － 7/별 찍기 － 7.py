s = int(input())

# top
space = s-1
start = 1

while space >= 0:
    line = ''
    line += ' '*space
    line += '*'*start  
    space-=1
    start+=2
    print(line)
    
# bottom
space = 1
start = 1+2*(s-2)

while space < s:
    line = ''
    line += ' '*space
    line += '*'*start  
    space+=1
    start-=2
    print(line)