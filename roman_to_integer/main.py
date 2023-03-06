roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def roman_to_int(roman_num: str) -> int:
    _sum = 0
    
    for x in range(len(roman_num)):
        if x != len(roman_num) - 1:
            if roman[roman_num[x]] < roman[roman_num[x + 1]]:
                _sum -= roman[roman_num[x]]
            else:
                _sum += roman[roman_num[x]]
        else:
            _sum += roman[roman_num[x]]
          
    return _sum

    

print(roman_to_int("MCMXCIV"))