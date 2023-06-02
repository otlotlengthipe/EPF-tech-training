count = 0
n1 = 0
n2 = 1
sum = 0 


while count < 4000000 :

    count = n1 + n2 
    n1 = n2 
    n2 = count 
 
    if count%2 == 0:
        sum+= count
        
print(sum)
