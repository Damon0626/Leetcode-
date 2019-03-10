# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-3-10 下午4:54
# @Email : wwymsn@163.com
# @Software: PyCharm


class Solution:
	def minimumTotal(self, triangle):

		'''
		从上至下，不正确
		:param triangle:
		:return:
		'''
		# if not triangle:
		# 	return 0
		# if len(triangle) == 1:
		# 	return triangle[0][0]
		#
		# min_value = triangle[0][0]
		# index = int(0)
		# for level in range(1, len(triangle)):
		# 	result = min(triangle[level][index+0], triangle[level][index+1])
		# 	print(result)
		# 	if result == triangle[level][index+0]:
		# 		index = index
		# 	else:
		# 		index += 1
		# 	min_value += result
		# return min_value
		h = [0]*(len(triangel)+1)

		for row in triangel[::-1]:
			for i in range(len(row)):
				h[i] = row[i] + min(h[i], h[i+1])
		return h[0]


if __name__ == "__main__":
	test = Solution()
	triangel = [[-1], [2, 3], [1, -1, -3]]
	print(test.minimumTotal(triangel))
