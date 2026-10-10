numbers = [12, 45, 8, 23, 17, 36, 4, 29, 50, 11]
sum = 0
count =0
for i in range(0, 10, 1): 

        sum+=numbers[i]
        count+=1
        average = sum/count
print("Average indexes: ", average)
