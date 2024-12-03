filename="./input1.txt"
left=[]
right=[]
with open(filename) as my_file:
    data=my_file.readlines()
    
    for element in data:
        tmp=element.split()
        left.append(int(tmp[0]))
        right.append(int(tmp[1].strip()))

left.sort()
right.sort()

i=0
sumresult=0
multiplyresult=0
while(i<len(left)):
    sumresult=sumresult+abs(left[i]-right[i])
    tmp=right.count(left[i])
    multiplyresult=multiplyresult+left[i]*tmp
    i=i+1

print(sumresult)
print(multiplyresult)


print("end")
