def sliding_window(nums, condition):
  left = 0
  res = 【ini】#根据问题选择合适的初始值
  current_window = 【ini】 #用于记录窗口内的某种状态
  for right in range(len(nums)):
    current_window = 【op】#加入右边界
    while condition(current_window):
       res = 【update】#更新结果
       current_window = 【op】#减去左边界
       left += 1
     # res = 【update】也有可能在这
  return res
