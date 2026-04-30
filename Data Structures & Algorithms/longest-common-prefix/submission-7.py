class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 1. Very Complex way - Naive
        # lcp=""
        # i = len(strs[0])
        # prev = strs[0]
        # j = 0
        # str_count = 1
        # while str_count<len(strs):
        #     if j<len(strs[str_count]) and j < len(prev) and prev[j] == strs[str_count][j]:
        #         j+=1
        #     else:
        #         i=min(i, j)
        #         j=0
        #         prev=strs[str_count]
        #         str_count+=1
        # return prev[:i]

        prev = strs[0]
        for elem in strs[1:]:
            while not elem.startswith(prev):
                prev = prev[:-1]
        return prev