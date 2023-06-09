def problem_3(m):       #defining problem function
    n = m               #the value to be returned
    i = 2               # the value used for the remainder calculation


    while (n != 1) :                #while loop condition is set and will execute if true, when n is not equal to 1

        rem = n%i     #the value of n must be divisible by 2, result will be remainder
        if (rem==0):  #if function, will execute if the remainder is equal to 0
            n = n/i   #reinitialise the value of n with the new n which is m from the initial initialization and divide it by i(2)
            print(i)  # print out the value of i if the condition is true
        else:         #if condition is false then execute next step
            i =+ 1 # the initial value will add 1 to it        
    
    return n                        #returning the value of n
print(problem_3(600851475143))      #calling the function 