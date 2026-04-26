class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([f"{len(s)}#{s}"for s in strs])

    def decode(self, s: str) -> List[str]:
        i=0
        result=[]

        while i < len(s):
            j = s.find("#", i)
            s_len = int(s[i:j])
            result.append(s[j+1:j+1+s_len])
            i = j+1+s_len
        return result