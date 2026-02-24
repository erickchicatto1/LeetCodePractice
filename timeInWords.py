def timeInWords(h, m):
    numbers = {
        1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
        15: "quarter", 16: "sixteen", 17: "seventeen", 18: "eighteen",
        19: "nineteen", 20: "twenty", 21: "twenty one",
        22: "twenty two", 23: "twenty three", 24: "twenty four",
        25: "twenty five", 26: "twenty six", 27: "twenty seven",
        28: "twenty eight", 29: "twenty nine", 30: "half"
    }
    
    if m == 0:
        return f"{numbers[h]} o' clock"
    
    elif m == 15:
        return f"quarter past {numbers[h]}"
    
    elif m == 30:
        return f"half past {numbers[h]}"
    
    elif m == 45:
        return f"quarter to {numbers[h+1]}"
    
    elif m < 30:
        if m == 1:
            return f"one minute past {numbers[h]}"
        else:
            return f"{numbers[m]} minutes past {numbers[h]}"
    
    else:
        remaining = 60 - m
        if remaining == 1:
            return f"one minute to {numbers[h+1]}"
        else:
            return f"{numbers[remaining]} minutes to {numbers[h+1]}"
