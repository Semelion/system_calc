def convert_to(num, num_bas, bas):
    numbers = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
               24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if num_bas == 10:
        n = ''
        num = int(num)
        while not num < bas:
            n += str(digits[num % bas])
            num //= bas
        n = str(num) + n[::-1]
    else:
        n = 0
        cnt = 0
        while num != '':
            if num[-1].isdigit():
                last_digit = int(num[-1])
            else:
                last_digit = numbers[digits.index(num[-1].upper()) - 10]
            n += int(last_digit) * num_bas ** cnt
            num = num[:-1]
            cnt += 1
    return str(n)


def convert_negative_number(number, source_base, target_base):
    number = int(str(number))
    positive_number = abs(number)
    converted_number = convert_positive_number(positive_number, source_base, target_base)
    return -converted_number

def convert_positive_number(number, source_base, target_base):
    decimal_number = int(str(number), source_base)
    converted_number = ""
    while decimal_number > 0:
        remainder = decimal_number % target_base
        converted_number = str(remainder) + converted_number
        decimal_number //= target_base
    return int(converted_number)


def perform_operation(operation, num_bas1, num1, num_bas2, num2, res_bas):
    if (int(num1) >= 0) and (int(num2) >= 0):
        if operation == '+':
            result = int(convert_to(num1, num_bas1, 10)) + int(convert_to(num2, num_bas2, 10))
        elif operation == '-':
            result = abs(int(convert_to(num1, num_bas1, 10)) - int(convert_to(num2, num_bas2, 10)))
        elif operation == '*':
            result = int(convert_to(num1, num_bas1, 10)) * int(convert_to(num2, num_bas2, 10))
        elif operation == ':':
            result = int(convert_to(num1, num_bas1, 10)) / int(convert_to(num2, num_bas2, 10))
        else:
            return "Invalid operation"
    else:
        if int(num1) < 0:
            num1 = convert_negative_number(num1, num_bas1, 10)
        else:
            num1 = convert_positive_number(num1, num_bas1, 10)
        if int(num2) < 0:
            num2 = convert_negative_number(num2, num_bas2, 10)
        else:
            num2 = convert_positive_number(num2, num_bas2, 10)
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = abs(num1 - num2)
        elif operation == '*':
            result = num1 * num2
        elif operation == ':':
            result = num1 / num2
    if result < 0:
        return convert_negative_number(result, 10, res_bas)
    else:
        return convert_to(result, 10, res_bas)

def num_systems(operation, num_bas1, num1, num_bas2, num2, res_bas):
    result = perform_operation(operation, int(num_bas1), num1, int(num_bas2), num2, int(res_bas))
    return result

# экзампл
# operation = "+"
#num_bas1 = "10"
#num1 = "-10"
#num_bas2 = "10"
#num2 = "-5"
#res_bas = "2"

#result = num_systems(operation, num_bas1, num1, num_bas2, num2, res_bas)
#print(result)
