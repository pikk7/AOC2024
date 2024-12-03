filename="./input.txt"

def increase_list(a,b):
    a=int(a)
    b=int(b)
    if(abs(a-b)>3):
        return False
    if(b>=a):
        return False
    return True

def descrease_list(a,b):
    a=int(a)
    b=int(b)
    if(abs(a-b)>3):
        return False
    if(b<=a):
        return False
    return True

def good_row(my_list):
    i=1
    desc=1
    inc=1
    while(i<len(my_list)):
        if(descrease_list(my_list[i-1],my_list[i])):
            desc=desc+1
        elif(increase_list(my_list[i-1],my_list[i])):
            inc=inc+1
        else:
            return False
        i=i+1
    return desc==len(my_list) or inc==len(my_list)
 

data=[]
with open(filename) as my_file:
    tmp=my_file.readlines()
    for element in tmp:
        data.append((element.split()))

result=0    

#Task1
for element in data:
    if(good_row(element)):
        result=result+1
print(result)

#Task2
i=0
not_dampered=True
result=0
while(i<len(data) and not_dampered):
    if(good_row(data[i])):
        result=result+1
    i=i+1


print(result)
print("end")
