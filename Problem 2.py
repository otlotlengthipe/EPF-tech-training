def problem_2(n): #defining function
        
    next_value = 0           #count initialised to 0 as count begins at 0
    n1 = 0              #n1 is the first number
    n2 = 1              #n2 is the second number
    sum = 0             #sum is initially 0


    while next_value < n:       #while loop condition is set and will execute if true, counter is less than n which is the input value

        next_value = n1 + n2     #counter will add n1 and n2 to get the next value
        n1 = n2             #re-initialise n1 to the next value which is n2
        n2 = next_value          #n2 will take the value of count which is the last value
    
        if next_value%2 == 0:    #if condition expression will be true if count modulus 2 is equal to 0
            sum+= next_value     # the value of count will be added to sum as the code runs

    return sum          #return the sum' 
  
#print(sum)          #print the results(sum)
print(problem_2(4000000))   #calling the function
