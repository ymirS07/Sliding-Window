def sliding_window(nums, k):
 
  window = []
  res = []
  left = 0
  
  for right in range(len(nums)):
    window.append(nums[right])
    if right - left + 1 == k:
      res.append(some_operation(window))
      window.pop()
      left += 1
  
  return res
