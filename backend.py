def toBASEint(num, base):
    alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = abs(num)
    b = alpha[n % base]
    while n >= base :
        n = n // base
        b += alpha[n % base]
    return ('' if num >= 0 else '-') + b[::-1]

def toBaseFrac(frac, base, n = 16) :
    alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b = ''
    while n :
        frac *= base
        frac = round(frac,n)
        b += str(alpha[int(frac)])
        frac -= int(frac)
        n -= 1
    return b

Number = input()
Basein = int(input())
Baseout = int(input())
alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if '.' in Number :
    num, frac = map(str,Number.split('.'))
    num = int(num,Basein)
    a = toBASEint(num,Baseout)
    b = 0
    k = Basein
    for i in frac :
        b += alpha.index(i) / k
        k *= Basein
    b = str(toBaseFrac(b, Baseout)).rstrip('0')
    print(a+'.'+b)
else :
    print(toBASEint(int(Number,Basein),Baseout))

print("end")
