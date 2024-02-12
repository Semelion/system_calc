def num_systems():
    def greeting():
        questions()

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

    def addition():
        while True:
            num_bas_1 = input('СС первого числа')
            if num_bas_1.isdigit() and 1 < int(num_bas_1) < 37:
                num_bas_1 = int(num_bas_1)
                break
            elif num_bas_1.isdigit() and int(num_bas_1) > 37:
                print('ошибка: основание больше 36')
                continue
            elif num_bas_1.isdigit() and int(num_bas_1) < 2:
                print('ошибка: основание меньше 2')
                continue
            else:
                print('нецелое')
                continue
        while True:
            num_1 = input('1 слагаемое')
            num_1 = num_1.strip()
            flag = True
            for i in num_1:
                res = convert_to(i, num_bas_1, 10)
                if int(res) >= num_bas_1:
                    flag = False
                elif not i.isdigit() and not i.isalpha():
                    flag = False
            if not flag:
                print('число содержит недопустимые для исходной системы счисления символы')
                continue
            else:
                break
        while True:
            num_bas_2 = input('СС второго слагаемого')
            if num_bas_2.isdigit() and 1 < int(num_bas_2) < 37:
                num_bas_2 = int(num_bas_2)
                break
            elif num_bas_2.isdigit() and int(num_bas_2) > 37:
                print('оошибка: основание больше 36')
                continue
            elif num_bas_2.isdigit() and int(num_bas_2) < 2:
                print('ошибка: основание меньше 2')
                continue
            else:
                print('нецелое')
                continue
        while True:
            num_2 = input('второе слагаемое: ')
            num_2 = num_2.strip()
            flag = True
            for i in num_2:
                res = convert_to(i, num_bas_2, 10)
                if int(res) >= num_bas_2:
                    flag = False
                elif not i.isdigit() and not i.isalpha():
                    flag = False
            if not flag:
                print('недопустимые для исходной системы счисления символы')
                continue
            else:
                break
        while True:
            res_bas = input('СС результата')
            if res_bas.isdigit() and 1 < int(res_bas) < 37:
                res_bas = int(res_bas)
                break
            elif res_bas.isdigit() and int(res_bas) > 37:
                print('ошибка: основание больше 36')
                continue
            elif res_bas.isdigit() and int(res_bas) < 2:
                print('ошибка: основание меньше 2')
                continue
            else:
                print('нецелое')
                continue
        print(convert_to(int(convert_to(num_1, num_bas_1, 10)) + int(convert_to(num_2, num_bas_2, 10)), 10, res_bas))

    def subtraction():
        while True:
            num_bas_1 = input('СС первого числа ')
            if num_bas_1.isdigit() and 1 < int(num_bas_1) < 37:
                num_bas_1 = int(num_bas_1)
                break
            elif num_bas_1.isdigit() and int(num_bas_1) > 37:
                print('ошибка: основание больше 36')
                continue
            elif num_bas_1.isdigit() and int(num_bas_1) < 2:
                print('ошибка: основание меньше 2')
                continue
            else:
                print('нецелое')
                continue
        while True:
            num_1 = input('1 слагаемое')
            num_1 = num_1.strip()
            flag = True
            for i in num_1:
                res = convert_to(i, num_bas_1, 10)
                if int(res) >= num_bas_1:
                    flag = False
                elif not i.isdigit() and not i.isalpha():
                    flag = False
            if not flag:
                print('недопустимые для исходной системы счисления символы')
                continue
            else:
                break
        while True:
            num_bas_2 = input('СС вычитаемого')
            if num_bas_2.isdigit() and 1 < int(num_bas_2) < 37:
                num_bas_2 = int(num_bas_2)
                break
            elif num_bas_2.isdigit() and int(num_bas_2) > 37:
                print('ошибка: основание больше 36')
                continue
            elif num_bas_2.isdigit() and int(num_bas_2) < 2:
                print('ошибка: основание меньше 2')
                continue
            else:
                print('нецелое')
                continue
        while True:
            num_2 = input('вычитаемое: ')
            num_2 = num_2.strip()
            flag = True
            for i in num_2:
                res = convert_to(i, num_bas_2, 10)
                if int(res) >= num_bas_2:
                    flag = False
                elif not i.isdigit() and not i.isalpha():
                    flag = False
            if not flag:
                print('недопустимые для исходной системы счисления символы')
                continue
            else:
                break
        while True:
            res_bas = input('СС итога ')
            if res_bas.isdigit() and 1 < int(res_bas) < 37:
                res_bas = int(res_bas)
                break
            elif res_bas.isdigit() and int(res_bas) > 37:
                print('ошибка: основание больше 36')
                continue
            elif res_bas.isdigit() and int(res_bas) < 2:
                print('ошибка: основание меньше 2')
                continue
            else:
                print('нецелое')
                continue
        print(convert_to(int(convert_to(num_1, num_bas_1, 10)) - int(convert_to(num_2, num_bas_2, 10)), 10, res_bas))

    def multiplication():
        while True:
            num_bas_1 = input('СС 1 множителя')
            if num_bas_1.isdigit() and 1 < int(num_bas_1) < 37:
                num_bas_1 = int(num_bas_1)
                break
            elif num_bas_1.isdigit() and int(num_bas_1) > 37:
                print('ошибка: основание больше 36')
                continue
            elif num_bas_1.isdigit() and int(num_bas_1) < 2:
                print('ошибка: основание меньше 2')
                continue
            else:
                print('нецелое')
                continue
        while True:
            num_1 = input('1 множитель')
            num_1 = num_1.strip()
            flag = True
            for i in num_1:
                res = convert_to(i, num_bas_1, 10)
                if int(res) >= num_bas_1:
                    flag = False
                elif not i.isdigit() and not i.isalpha():
                    flag = False
            if not flag:
                print('недопустимые для исходной системы счисления символы')
                continue
            else:
                break
        while True:
            num_bas_2 = input('СС 2 множителя')
            if num_bas_2.isdigit() and 1 < int(num_bas_2) < 37:
                num_bas_2 = int(num_bas_2)
                break
            elif num_bas_2.isdigit() and int(num_bas_2) > 37:
                print('ошибка: основание больше 36')
                continue
            elif num_bas_2.isdigit() and int(num_bas_2) < 2:
                print('ошибка: основание меньше 2')
                continue
            else:
                print('нецелое')
                continue
        while True:
            num_2 = input('2 множитель')
            num_2 = num_2.strip()
            flag = True
            for i in num_2:
                res = convert_to(i, num_bas_2, 10)
                if int(res) >= num_bas_2:
                    flag = False
                elif not i.isdigit() and not i.isalpha():
                    flag = False
            if not flag:
                print('недопустимые для исходной системы счисления символы')
                continue
            else:
                break
        while True:
            res_bas = input('СС результата ')
            if res_bas.isdigit() and 1 < int(res_bas) < 37:
                res_bas = int(res_bas)
                break
            elif res_bas.isdigit() and int(res_bas) > 37:
                print('ошибка: основание больше 36')
                continue
            elif res_bas.isdigit() and int(res_bas) < 2:
                print('ошибка: основание больше 36')
                continue
            else:
                print('нецелое')
                continue
        print(convert_to(int(convert_to(num_1, num_bas_1, 10)) * int(convert_to(num_2, num_bas_2, 10)), 10, res_bas))

    def division():
        while True:
            num_bas_1 = input('СС делимого')
            if num_bas_1.isdigit() and 1 < int(num_bas_1) < 37:
                num_bas_1 = int(num_bas_1)
                break
            elif num_bas_1.isdigit() and int(num_bas_1) > 37:
                print('ошибка: основание больше 36')
                continue
            elif num_bas_1.isdigit() and int(num_bas_1) < 2:
                print('ошибка: основание меньше 2')
                continue
            else:
                print('нецелое')
                continue
        while True:
            num_1 = input('делимое')
            num_1 = num_1.strip()
            flag = True
            for i in num_1:
                res = convert_to(i, num_bas_1, 10)
                if int(res) >= num_bas_1:
                    flag = False
                elif not i.isdigit() and not i.isalpha():
                    flag = False
            if not flag:
                print('недопустимые для исходной системы счисления символы')
                continue
            else:
                break
        while True:
            num_bas_2 = input('СС делителя')
            if num_bas_2.isdigit() and 1 < int(num_bas_2) < 37:
                num_bas_2 = int(num_bas_2)
                break
            elif num_bas_2.isdigit() and int(num_bas_2) > 37:
                print('ошибка: основание больше 36')
                continue
            elif num_bas_2.isdigit() and int(num_bas_2) < 2:
                print('ошибка: основание меньше 2')
                continue
            else:
                print('нецелое')
                continue
        while True:
            num_2 = input('делитель: ')
            num_2 = num_2.strip()
            flag = True
            for i in num_2:
                res = convert_to(i, num_bas_2, 10)
                if int(res) >= num_bas_2:
                    flag = False
                elif not i.isdigit() and not i.isalpha():
                    flag = False
            if not flag:
                print('недопустимые для исходной системы счисления символы')
                continue
            else:
                break
        while True:
            res_bas = input('СС частного')
            if res_bas.isdigit() and 1 < int(res_bas) < 37:
                res_bas = int(res_bas)
                break
            elif res_bas.isdigit() and int(res_bas) > 37:
                print('ошибка: основание больше 36')
                continue
            elif res_bas.isdigit() and int(res_bas) < 2:
                print('ошибка: основание меньше 2')
                continue
            else:
                print('нецелое')
                continue
        print(convert_to(int(convert_to(num_1, num_bas_1, 10)) / int(convert_to(num_2, num_bas_2, 10)), 10, res_bas))

    def questions():
        print('Ниже будут представлены все возможные операции с числами различных систем счисления')
        print('Выберите необходимую вам ')
        print('2. Сложение. Введите "+" ')
        print('3. Вычитание. Введите "-" ')
        print('4. Умножение. Введите "*" ')
        print('5. Деление. Введите ":" ')
        while True:
            operation = input().strip().lower()
            if operation == "+" or operation == "-" or operation == "*" or operation == ":":
                if operation == '+':
                    addition()
                    break
                elif operation == '-':
                    subtraction()
                    break
                elif operation == '*':
                    multiplication()
                    break
                elif operation == ':':
                    division()
                    break
    greeting()
num_systems()