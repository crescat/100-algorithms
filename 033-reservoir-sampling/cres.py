# Day 33: Reservoir sampling

import random

def reservoir_sampling(i, size, sample, data):
    i += 1
    if len(sample) < size:
        sample.append(data)
    else:
        random_num = random.randint(1, i)
        if random_num <= len(sample):
            removal_index = random.randint(0, len(sample)-1)
            sample = sample[:removal_index] + sample[removal_index+1:]
            sample.append(data)
    return i, sample

i = 0
sample = []
for _ in range(1000):
    random_data = random.randint(0, 100)
    i, sample = reservoir_sampling(i, 10, sample, random_data)
    if i % 100 == 0:
        print(i, sample)

'''
result:
100 [14, 51, 44, 44, 94, 9, 85, 60, 99, 74]
200 [14, 51, 44, 94, 9, 99, 67, 8, 77, 73]
300 [14, 51, 9, 99, 67, 8, 77, 73, 93, 32]
400 [9, 99, 8, 77, 73, 93, 32, 13, 87, 67]
500 [9, 99, 77, 73, 93, 32, 13, 29, 14, 43]
600 [9, 73, 93, 29, 14, 43, 64, 51, 95, 6]
700 [9, 93, 14, 43, 64, 51, 95, 6, 61, 19]
800 [9, 93, 14, 43, 64, 95, 6, 61, 19, 69]
900 [93, 14, 43, 64, 95, 6, 19, 69, 94, 97]
1000 [93, 14, 43, 64, 95, 6, 19, 69, 97, 57]
'''

def avg(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    avg_num = avg(nums[1:])
    return avg_num + (nums[0] - avg_num) / len(nums)

print(avg(list(range(100))))
