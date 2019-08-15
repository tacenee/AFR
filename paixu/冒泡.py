def maopao(nums):

    for i in range(1,len(nums)):
        for j in range(0,len(nums)-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums
# def maopao(nums):
# 	for i in range(len(nums)-1):
# 		for j in range(len(nums)-i-1):
# 			if nums[j] > nums[j+1]:
# 				nums[j], nums[j+1] = nums[j+1], nums[j]
# 	return nums



if __name__ == '__main__':
    nums = [1,3,8,5,6,7,2,9,16,12,14]
    print(maopao(nums))