class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        i = 0
        
        while i < len(s):
           
            two_letters = s[i:i+2]
            
            # 1. Check the 6 special 2-letter pairs first
            if two_letters == "IV":
                total += 4
                i += 2  # Skip both letters
            elif two_letters == "IX":
                total += 9
                i += 2
            elif two_letters == "XL":
                total += 40
                i += 2
            elif two_letters == "XC":
                total += 90
                i += 2
            elif two_letters == "CD":
                total += 400
                i += 2
            elif two_letters == "CM":
                total += 900
                i += 2
                
            # 2. Otherwise, check the single letter
            else:
                one_letter = s[i]
                if one_letter == 'I':
                    total += 1
                elif one_letter == 'V':
                    total += 5
                elif one_letter == 'X':
                    total += 10
                elif one_letter == 'L':
                    total += 50
                elif one_letter == 'C':
                    total += 100
                elif one_letter == 'D':
                    total += 500
                elif one_letter == 'M':
                    total += 1000
                i += 1  # Move forward by 1 letter
                
        return total
