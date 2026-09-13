def GuessNum(self, nums):
  for num in nums:
    if num in nums:
      return num
  return None
