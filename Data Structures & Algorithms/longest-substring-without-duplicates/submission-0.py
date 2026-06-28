class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str=''
        c=0
        max=0
        for i in range(len(s)):
            if s[i] in str:
                str=str[str.index(s[i])+1:]
            str=str+s[i]
            c=len(str)
            if c>max:
                max=c
        return max

                

            