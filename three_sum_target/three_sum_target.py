# given a array of int and a target, check if there exist 3 numbers' sum equals the target

a = [2, 1,3,4,5,6]

def three_sum(nums, target):
  # dic = {}
  # for i,n in enumerate(nums):
  #   dic[n] = i
  
  # for i in range(len(nums)-1):
  #   for j in range(i+1, len(nums)):
  #     last = target-nums[i]-nums[j]
  #     if last in dic and dic[last] not in (i, j):
  #       print(nums[i])
  #       print(nums[j])
  #       print(last)
  #       return True
  # return False
  
  nums.sort()
  for i in range(len(nums)):
    l = i+1
    r = len(nums)-1

    while l<r:
      three_sum = nums[i]+nums[l]+nums[r]
      if three_sum == target:
        return True
      
      if three_sum < target:
        l+=1
      else:
        r-=1
    
  return False
    
    




  


print(three_sum(a, 6))