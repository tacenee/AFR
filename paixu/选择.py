def xuanze(nums):

    for i in range(len(nums)):
        right = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[right]:
                right = j
        nums[i], nums[right] = nums[right], nums[i]

    return nums

# def xuanze(nums):
# 	for i in range(len(nums)):
# 		index = i
# 		for j in range(len(nums)-i-1):
# 			if nums[j+i]<nums[index]:
# 				index = j + i
# 		nums[i], nums[index] = nums[index], nums[i]
# 	return nums


if __name__ == '__main__':
    nums = [1,3,8,5,6,7,2,9,16,12,14]
    print(xuanze(nums))