class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s) == 0):
            return 0

        char_set = set()
        il = ir = max_length = 0
        while (ir < len(s)):
            if s[ir] not in char_set:
                char_set.add(s[ir])
                ir += 1
                max_length = max(max_length, ir - il)
            else:
                char_set.remove(s[il])
                il += 1
        return max_length
