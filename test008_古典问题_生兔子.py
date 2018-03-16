momRabbit = [1]
month = 1

while(month <=42):
    print(len(momRabbit))
    month += 1
    for i in range(0,len(momRabbit)):
        momRabbit[i] += 1
    for j in range(0,len(momRabbit)):
        if(momRabbit[j]>=3):
            momRabbit.append(1)
            
    
            
