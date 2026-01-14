total_credit = 0.0
grade = 0.0

for _ in range(20):
    line = input().split()
    
    if line[2] == 'P': continue
    
    if line[2] == 'A+': grade += 4.5*float(line[1])
    elif line[2] == 'A0': grade += 4.0*float(line[1])
    elif line[2] == 'B+': grade += 3.5*float(line[1])
    elif line[2] == 'B0': grade += 3.0*float(line[1])
    elif line[2] == 'C+': grade += 2.5*float(line[1])
    elif line[2] == 'C0': grade += 2.0*float(line[1])
    elif line[2] == 'D+': grade += 1.5*float(line[1])
    elif line[2] == 'D0': grade += 1.0*float(line[1])
    else: grade += 0
    total_credit += float(line[1])
    
print('%.6f' %(grade/total_credit))