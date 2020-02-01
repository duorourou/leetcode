from typing import List


class Solution:

	def countBits(self, num: int) -> List[int]:
		result = [0] * (num + 1)
		for i in range(1, num):
			result[i + 1] = result[(i + 1) & i] + 1
		result.remove(0)
		return result


if __name__ == '__main__':
	print(Solution().countBits(5))
