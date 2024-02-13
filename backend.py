def toBASEint(num, base):
    alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = abs(num)
    b = alpha[n % base]
    while n >= base:
        n = n // base
        b += alpha[n % base]
    return ('' if num >= 0 else '-') + b[::-1]


def toBaseFrac(frac, base, n=16):
    alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b = ''
    while n:
        frac *= base
        frac = round(frac, n)
        b += str(alpha[int(frac)])
        frac -= int(frac)
        n -= 1
    return b

def convert(Number, Basein, Baseout):
    alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if '.' in Number:
        num, frac = map(str, Number.split('.'))
        num = int(num, Basein)
        a = toBASEint(num, Baseout)
        b = 0
        k = Basein
        for i in frac:
            b += alpha.index(i) / k
            k *= Basein
        b = str(toBaseFrac(b, Baseout)).rstrip('0')
        return(a + '.' + b)
    else:
        return(toBASEint(int(Number, Basein), Baseout))

def perform_operation(operation, num_bas1, num1, num_bas2, num2, res_bas):
    if operation == '+':
        return str( float(convert(num1, num_bas1, 10)) + float(convert(num2, num_bas2, 10)) )
    elif operation == '-':
        return str( float(convert(num1, num_bas1, 10)) + float(convert(num2, num_bas2, 10)) )
    elif operation == '*':
        return str( float(convert(num1, num_bas1, 10)) * float(convert(num2, num_bas2, 10)) )
    elif operation == ':':
        return str( float(convert(num1, num_bas1, 10)) / float(convert(num2, num_bas2, 10)) )

def num_systems(operation, num_bas1, num1, num_bas2, num2, res_bas):
    result = perform_operation(operation, int(num_bas1), num1, int(num_bas2), num2, int(res_bas))
    print(result)
    return convert(result, 10, int(res_bas))
