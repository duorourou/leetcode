from typing import List


class Solution:

	def countBits(self, num: int) -> List[int]:
		result = [0] * num
		for i in range(1, num):
			result[i] = result[i & (i - 1)] + 1
		return result


if __name__ == '__main__':
	print(Solution().countBits(5))
