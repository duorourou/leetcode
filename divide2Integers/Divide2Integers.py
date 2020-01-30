class Divider:
	MAX: int = (2 ** 31) - 1
	MIN: int = -2 ** 31

	def divide(self, dividend: int, divisor: int) -> int:
		if divisor == 0 or dividend > Divider.MAX or divisor > Divider.MAX or dividend < Divider.MIN or divisor < Divider.MIN:
			return Divider.MAX
		if dividend == 0:
			return 0
		if divisor == 1:
			return dividend if Divider.MIN <= dividend <= Divider.MAX else Divider.MAX
		if divisor == -1:
			return -dividend if Divider.MIN <= -dividend <= Divider.MAX else Divider.MAX
		if abs(dividend) < abs(divisor):
			return 0
		if abs(dividend) == abs(divisor):
			if dividend + divisor != 0:
				return 1
			else:
				return -1
		absDividend = abs(dividend)
		absDivisor = abs(divisor)
		current: int = 0 + absDivisor
		result: int = 1
		while result < Divider.MAX:
			if current < (absDividend - current - current):
				current += current
				result += result
			elif (absDividend - current) > current > (absDividend - current - current) > 0:
				result += result
				absDividend = absDividend - current - current
				result += self.divide(absDividend, absDivisor)
			else:
				absDividend = absDividend - current
				if absDividend > 0:
					result += self.divide(absDividend, absDivisor)
				break
		if abs(divisor) != divisor and abs(dividend) == dividend:
			return -result
		elif abs(divisor) == divisor and abs(dividend) != dividend:
			return -result
		else:
			return result


if __name__ == '__main__':
	# print(Divider().divide(10, 1))
	# print(Divider().divide(10, -1))
	# print(Divider().divide(10, 2))
	# print(Divider().divide(10, 3))
	# print(Divider().divide(10, 4))
	# print(Divider().divide(10, 5))
	# print(Divider().divide(10, 6))
	# print(Divider().divide(-10, 6))
	# print(Divider().divide(-100, 6))
	# print(Divider().divide(-666666108, 6))
	# print(Divider().divide(7, -3))
	# print(Divider().divide(-2147483648, 1))
	print(Divider().divide(-2147483648, -1))
# print(Divider().divide(4294967295, 1))
