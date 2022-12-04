a=input("Enter the elements of list:(comma separated):")
b=a.split(",")   #used to  make list with input values
b=list(map(float,b))   #make every element as integer

c=b[0]   #its ist element as greatest
for i in b:  #take every element of list named b
    if i>=c:  #check weather value of i is greater than c or not
        c=i   #if i greater than c ,it will make value of c as i
print("maximum value is:",c)
count=-1
for i in b:
    count=count+1  #gives index value to elements of list
    if c==i:   #when max value is found in list ,print its count value
        print("Index of the max value is :",count)
