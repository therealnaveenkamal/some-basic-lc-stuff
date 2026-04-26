class Solution:
    def isPalindrome(self, s: str) -> bool:
        fil = ""
        for st in s.lower():
            if st.isalnum():
                fil+=st

        return fil[::] == fil[::-1]