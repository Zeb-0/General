def peak(nums):
    for i in range(len(nums)):
        # check if current element is geater or equal to neighbors
        if (i == 0 or nums[i] >= nums[i - 1]) and (i == len(nums[i] - 1) or nums[i] >= nums[i + 1])
        return nums[i]  # found peak
    return None # no peak found

my_list = [23, 45, 67, 54, 87, 13]
print("The Peak is: ", peak(my_list))