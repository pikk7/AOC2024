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

def different_version_of_array(my_list):
    return_list=[]
    
    i=0
    while(i<len(my_list)):
        tmp= my_list[0:i]+my_list[i+1:len(my_list)]
        
        return_list.append(tmp)
        i=i+1
    
    return return_list

def good_row(my_list,break_rule=False):
    i=1
    desc=1
    inc=1
    while(i<len(my_list)):
        if(descrease_list(my_list[i-1],my_list[i])and inc==1):
            desc=desc+1
        elif(increase_list(my_list[i-1],my_list[i])and desc==1):
            inc=inc+1
        else:
            if(break_rule):
                return False
            second_try_list=different_version_of_array(my_list)
            for e in second_try_list:
                if(good_row(e,True)):
                    return True
            
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
result=0
while(i<len(data) ):
    if(good_row(data[i],False)):
        result=result+1
    i=i+1


print(result)
print("end")
