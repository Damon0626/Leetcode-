# Leetcode
数据结构与算法学习
## 1.Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.  
You may assume that each input would have **exactly** one solution, and you **may not use the same element twice**.  
  
**For example:**
```python
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```  
  
**自己** 
时间复杂度较高，比较出差距
```python
lenNums = len(nums)
for i in range(lenNums):
    if (target - nums[i]) in nums[i+1:]:
        return [i, nums[i+1:].index(target-nums[i])+i+1]
```
  
**大神**
```python
compliments = {}
for i in range(len(nums)):
    if nums[i] in compliments:
        return [compliments[nums[i]], i]
    comp = target - nums[i]
    compliments[comp] = i
```
-----------------------------------------------------------------------------------------------  
## 2.Add Two Numbers   
