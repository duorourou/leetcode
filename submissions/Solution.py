from typing import List


class Solution:
	def merge(self, intervals: List[List[int]]) -> List[List[int]]:
		if not intervals:
			return []
		intervals.sort(key=lambda it: it[0])
		print(intervals)
		result = [intervals[0]]
		for current in intervals:
			if self.mergeable(result[-1], current):
				self.mergeArray(result[-1], current)
			else:
				result.append(current)
		return result

	def mergeable(self, last: List[int], current: List[int]):
		return last and current and last[1] >= current[0]

	def mergeArray(self, last: List[int], current: List[int]):
		last[0] = last[0] if last[0] <= current[0] else current[0]
		last[1] = last[1] if last[1] >= current[1] else current[1]


if __name__ == '__main__':
	print(Solution().merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]))
