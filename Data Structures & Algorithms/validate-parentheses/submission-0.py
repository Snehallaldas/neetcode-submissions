class Solution:
    def isValid(self, s):
        stack = []

        mapping = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for ch in s:
            if ch in mapping:
                stack.append(mapping[ch])  # expected closing bracket
            else:
                if not stack or stack.pop() != ch:
                    return False

        return not stack