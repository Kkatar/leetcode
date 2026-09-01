class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []

        for char in s:
            if char.isalnum():
                chars.append(char.lower())

        cleaned = ''.join(chars)

        return cleaned == cleaned[::-1]