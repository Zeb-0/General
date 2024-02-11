def peak(nums):
    for i in range(len(nums)):
        # check if current element is geater or equal to neighbors
        if (i == 0 or nums[i] >= nums[i - 1]) and (i == len(nums) - 1 or nums[i] >= nums[i + 1]):
            return nums[i]  # found peak
        
    return None # no peak found

'''Use binary search'''
def find_peak(mylist):
    '''check if list is empty'''
    if not mylist:
        return None
    
    '''binary algorithm'''
    left = 0
    right = len(mylist) - 1

    while left < right:
        mid = (left + right) // 2
        if (mylist[mid] < mylist[mid + 1]):
            left = mid + 1
        else:
            right = mid

    return mylist[left]


my_list = [23, 45, 67, 54, 87, 13]
print("The Peak is: ", peak(my_list))
print()
print("Binary Peak is: ", find_peak(my_list))
print()