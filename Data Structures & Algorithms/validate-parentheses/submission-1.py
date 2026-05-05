class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hm = {'}':'{', ']':'[', ')':'('}

        for elem in s:
            if elem in hm:
                if not stack:
                    return False
                if stack.pop() != hm[elem]:
                    return False
            else:
                stack.append(elem)
        if stack:
            return False
        return True