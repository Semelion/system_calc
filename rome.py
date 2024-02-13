coding = zip(
    [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1],
    ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
)


def to_rome(num):
    global coding
    if num <= 0 or num >= 4000 or int(num) != num:
        return "err format"
    result = []
    for d, r in coding:
        while num >= d:
            result.append(r)
            num -= d
    coding = zip(
        [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1],
        ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    )
    return ''.join(result)

def to_arabic(roman):
    roman_numerals = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
    }
    arabic = 0
    prev_value = 0
    for numeral in reversed(roman):
        value = roman_numerals[numeral]
        if value < prev_value:
            arabic -= value
        else:
            arabic += value
        prev_value = value
    return arabic



def perform_operation(operation, num1, num2):
    if operation == '+':
        result = to_arabic(num1) + to_arabic(num2)
    elif operation == '-':
        result = abs(to_arabic(num1) - to_arabic(num2))
    elif operation == '*':
        result = to_arabic(num1) * to_arabic(num2)
    elif operation == ':':
        result = to_arabic(num1) / to_arabic(num2)
    if result < 4000:
        return (to_rome(result))
    else:
        return ('err big,', result)

#example:

# a = 'MCMLIV' # 1954
# b = 'MMXX'   #2020

# c = perform_operation('+', a, b)
# c = 'MMMCMLXXIV' - это 3974
