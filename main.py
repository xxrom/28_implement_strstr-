class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
    if len(needle) == 0:
      return 0

    index = 0
    firstIndex = -1

    while index <= len(haystack) - len(needle) and firstIndex == -1:
      if haystack[index] == needle[0]:
        found = True
        innerIndex = 1

        while found and innerIndex < len(needle) :

          if haystack[index + innerIndex] != needle[innerIndex]:
            found = False

          innerIndex += 1

        if found:
          firstIndex = index

      index += 1

    return firstIndex

my = Solution()
n = 'hellee'
l = 'llee'
rightAns = 2

ans = my.strStr(n, l)
print("ans", ans, ans == rightAns)

# Runtime: 32 ms, faster than 71.09% of Python3 online submissions for Implement strStr().
# Memory Usage: 13.8 MB, less than 90.15% of Python3 online submissions for Implement strStr().