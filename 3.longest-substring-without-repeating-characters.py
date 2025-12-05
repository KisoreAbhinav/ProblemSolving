#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {}
        l=0
        output = 0
        for r in range (len(s)):
            if s[r] not in seen:
                output=max(output, r-l+1)
            else:
                if(seen[s[r]]<l):
                    output=max(output, r-l+1)
                else:
                    l=seen[s[r]]+1
            seen[s[r]]=r
        return output
# @lc code=end

