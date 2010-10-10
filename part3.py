from itertools import combinations
nums=[3, 4, 9, 14, 15, 19, 28, 37, 47, 50, 54, 56, 59, 61, 70, 73, 78, 81, 92, 95, 97, 99]
count=0
for index in range(len(nums)):
	for i in range(1, len(nums[:-(index+1)])):
		for combination in combinations(nums[:-(index+1)], i):
			if sum(combination)==nums[-(index+1)]:
				count=count+1
print(count)
