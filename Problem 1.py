

def problem_1(n):
    mysum = 0
    for i in range(n):
        
        if (i%10 ==0) and (i%15 ==0):
        
            mysum += i

    return mysum

print(problem_1(2))