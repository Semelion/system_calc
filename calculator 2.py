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

def perform_operation(operation, num_bas1, num1, num_bas2, num2, res_bas):
    if operation == '+':
        result = int(convert_to(num1, num_bas1, 10)) + int(convert_to(num2, num_bas2, 10))
    elif operation == '-':
        result = int(convert_to(num1, num_bas1, 10)) - int(convert_to(num2, num_bas2, 10))
    elif operation == '*':
        result = int(convert_to(num1, num_bas1, 10)) * int(convert_to(num2, num_bas2, 10))
    elif operation == ':':
        result = int(convert_to(num1, num_bas1, 10)) / int(convert_to(num2, num_bas2, 10))
    else:
        return "Invalid operation"

    return convert_to(result, 10, res_bas)

def num_systems(operation, num_bas1, num1, num_bas2, num2, res_bas):
    result = perform_operation(operation, int(num_bas1), num1, int(num_bas2), num2, int(res_bas))
    return result

# екзампле
operation = "+"
num_bas1 = "10"
num1 = "10"
num_bas2 = "10"
num2 = "5"
res_bas = "2"

result = num_systems(operation, num_bas1, num1, num_bas2, num2, res_bas)
