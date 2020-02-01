class Solution:
	def canMeasureWater(self, x: int, y: int, z: int) -> bool:
		if x == z or y == z:
			return True
		elif x == 0 or y == 0 or x + y < z:
			return False
		else:
			hcf = self.hcf(x, y)
			return hcf != 0 and z % hcf == 0

	def hcf(self, x: int, y: int):
		hcf: int = 0
		if x > y:
			smaller = y
		else:
			smaller = x
		for i in range(1, smaller + 1):
			if (x % i == 0) and (y % i == 0):
				hcf = i
		return hcf


if __name__ == '__main__':
	# print(Solution().canMeasureWater(3, 5, 4))
	# print(Solution().canMeasureWater(2, 6, 5))
	# print(Solution().canMeasureWater(0, 0, 0))
	# print(Solution().canMeasureWater(0, 1, 0))
	# print(Solution().canMeasureWater(1, 0, 0))
	# print(Solution().canMeasureWater(1, 1, 0))
	# print(Solution().canMeasureWater(0, 0, 1))
	# print(Solution().canMeasureWater(34, 5, 6))
	print(Solution().canMeasureWater(22003, 31237, 1))
