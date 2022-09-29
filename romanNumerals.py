def romanToInt(s: str) -> int:
    hashMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    num = 0
    
    for i in range(len(s)):
        if i < len(s) - 1:
            if s[i] == 'I':
                # Case 1 and 2
                if s[i+1] == 'V' or s[i+1] == 'X':
                    num -= 1
                else:
                    num += hashMap[s[i]]
            elif s[i] == 'X':
                # Case 3 and 4
                if s[i+1] == 'L' or s[i+1] == 'C':
                    num -= 10
                else:
                    num += hashMap[s[i]]
            elif s[i] == 'C':
                # Case 5 and 6
                if s[i+1] == 'D' or s[i+1] == 'M':
                    num -= 100
                else:
                    num += hashMap[s[i]]
            else:
                num += hashMap[s[i]]
        else:
            num += hashMap[s[i]]
    
    return num

def intToRoman(num: int) -> str:
    """
    Converts integers in arabic numerals into Roman numerals
    
    Special cases:
    4 -> IIII -> IV
    9 -> VIIII -> IX
    40 -> XXXX -> XL
    90 -> LXXXX -> XC
    400 -> CCCC -> CD
    900 -> DCCCC -> CM
    """
    hashMap = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
    order = [1000, 500, 100, 50, 10, 5, 1]
    
    roman = ""
    lastEntry = ""
    
    while num != 0:
        
        for i in range(len(order)):
            if order[i] <= num:
                break
        
        # (num // order[i]) = the number of letters to add for this time
        
        if (num // order[i]) == 4:
            # Special cases
            
            if hashMap[order[i]] == "I":
                # "I" before "V" or "X" cases
                
                if lastEntry == "V":
                    # 9 case
                    roman = roman[:-1]
                    
                    roman += "IX"
                    lastEntry = "IX"
                else:
                    # 4 case
                    roman += "IV"
                    lastEntry = "IV"
                
                num -= 4
            elif hashMap[order[i]] == "X":
                # "X" before "L" or "C" cases
                
                if lastEntry == "L":
                    # 90 case
                    roman = roman[:-1]
                    
                    roman += "XC"
                    lastEntry = "XC"
                else:
                    # 40 case
                    roman += "XL"
                    lastEntry = "XL"
                
                num -= 40
            else:
                # "C" before "D" or "M" cases
                
                if lastEntry == "D":
                    # 900 case
                    roman = roman[:-1]
                    
                    roman += "CM"
                    lastEntry = "CM"
                else:
                    # 400 case
                    roman += "CD"
                    lastEntry = "CD"
                
                num -= 400
        else:
            # Standard case
            roman += hashMap[order[i]] * (num // order[i])
            lastEntry = hashMap[order[i]] * (num // order[i])

            num %= order[i]
    
    return roman

if __name__ == '__main__':
    passed = True
    errors = []
    for i in range(1, 4000):
        romanNumeral = intToRoman(i)

        arabicNumeral = romanToInt(romanNumeral)

        if i != arabicNumeral:
            passed = False
            errors.append(i)
    
    if passed:
        print("All tests: PASSED")
    else:
        print("All tests: FAILED")
        print("errors for integer(s):", errors)