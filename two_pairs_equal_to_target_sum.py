num_to_list=int(input('Enter numbers like this (123451510) to add number to list:'))
numbers=[]
for x in range(num_to_list):
    numbers.append(x)
target_sum=int(input('Enter target number:'))
pair_equal_to_target_sum=False

for i in range(0,num_to_list-1):
    for j in range(i+1,num_to_list):
        if numbers[i]+numbers[j]==target_sum:
            print('Pair found:'+str(numbers[i])+' and '+str(numbers[j]))
            pair_equal_to_target_sum=True
            break
    if pair_equal_to_target_sum:
        break
if not pair_equal_to_target_sum:
    print('No pair in the list adds to target sum.')