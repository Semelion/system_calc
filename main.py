import flet as ft
import re

import backend
import rome

last_valid_value = ["","","","",""] # листы для соранения предыдущего значения текстовых полей
last_sys = ["","",""]

regex = "^[0-9A-Z.]+$" # регулярные выражения для проверки введённого в текстовые поля
regex_R = "^[MCDXLVI]+$"
pattern = re.compile(regex)
pattern_R = re.compile(regex_R)

def validate_numbers(field, pagee, id): # функция для проверки текстовых полей
    global last_valid_value

    digits = field.value.upper()
    field.value = digits
    pagee.update()
    # print(digits.replace(",", "."))
    if digits == "":
        last_valid_value[id] = ""
    else:
        if id < 2:
            if(digits != "-" and pattern.search(digits) is not None): # проверка для обычных с.с.
                last_valid_value[id] = digits
            else:
                field.value = last_valid_value[id]
                pagee.update()
        else:
            if(pattern_R.search(digits) is not None): # проверка для римской системы
                last_valid_value[id] = digits
            else:
                field.value = last_valid_value[id]
                pagee.update()

def validate_int(field, pagee, id): # проверка полей для систем счисления
    global last_sys

    digits = field.value
    if digits == "":
        last_sys[id] = ""
    else:
        try:
            int(digits)
            if(int(digits) > 36):
                last_sys[id] = 36
            else:
                last_sys[id] = digits
            field.value = last_sys[id]
            pagee.update()

            # print(float(digits))
        except ValueError:
            field.value = last_sys[id]
            pagee.update()

def check_num(num_val, sys): # функция проверки соответсвия числа его системе счисления
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in num_val:
        if (digits.find(i, 0, len(digits) - 1) + 1) > int(sys):
            return False
    return True

#############################
def main(page: ft.Page): # функция отрисовки окна
    page.update()
    ####function##### функции
    def close_banner(e): # реакция на кнопку ок в банере для его закрытия
        page.banner.open = False
        page.update()

    def get_result(e): # получение результата для обычных с.с.
        # check_num(num1.value, system1.value)
        chek = validate_data()
        if chek == True:
            if page.banner is not None:
                page.banner.open = False
            if sw_language.value == True:
                out.value = "Answer: " + str(backend.num_systems(operator_dropdown.value, system1.value, num1.value,
                    system2.value, num2.value, system_out.value))
                page.update()
            else:
                out.value = "Ответ: " + str(backend.num_systems(operator_dropdown.value, system1.value, num1.value,
                    system2.value, num2.value, system_out.value))
                page.update()
        else:
            page.banner = ft.Banner(
                # bgcolor=ft.colors.AMBER_100,
                leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
                content=ft.Text(chek),
                actions=[ft.TextButton("Ok", on_click=close_banner)]
                )
            page.banner.open = True
            page.update()

    def get_result_R(e): # получение результата для Римской системы
        # check_num(num1.value, system1.value)
        if num1_R.value != "" and num2_R.value != "" and operator_dropdown.value is not None:
            if page.banner is not None:
                page.banner.open = False
            if sw_language.value == True:
                answ = str(rome.perform_operation(operator_dropdown.value, num1_R.value, num2_R.value))
                if answ.find("err big,", 0, len(answ)) != -1:
                    out_R.value = "Answer in arabic (big number): " + answ[:7]
                else:
                    out_R.value = "Answer: " + answ
                page.update()
            else:
                answ = str(rome.perform_operation(operator_dropdown.value, num1_R.value, num2_R.value))
                print(answ)
                if answ.find("err big,", 0, len(answ)) != -1:
                    out_R.value = "Ответ в арабских цифрах (ответ слишком большой): " + answ[:7]
                else:
                    out_R.value = "Ответ: " + answ
                page.update()
        else:
            if sw_language.value == True:
                page.banner = ft.Banner(
                    # bgcolor=ft.colors.AMBER_100,
                    leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
                    content=ft.Text("not all fields are filled in"),
                    actions=[ft.TextButton("Ok", on_click=close_banner)]
                    )
                page.banner.open = True
                page.update()
            else:
                page.banner = ft.Banner(
                    # bgcolor=ft.colors.AMBER_100,
                    leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
                    content=ft.Text("Не все поля заполнены"),
                    actions=[ft.TextButton("Ok", on_click=close_banner)]
                    )
                page.banner.open = True
                page.update()

    def validate_data(): # функция проверки полей
        # print(lang)
        if system1.value != "" and system2.value != "" and system_out.value != "" and num1.value != "" and num2.value != "" and operator_dropdown.value is not None:
            if int(system1.value) >= 2 and int(system1.value) <= 36:
                if int(system2.value) >= 2 and int(system2.value) <= 36:
                    if int(system_out.value) >= 2 and int(system_out.value) <= 36:
                        if check_num(num1.value, system1.value) == True:
                            if check_num(num2.value, system2.value) == True:
                                return True
                            else:
                                if sw_language.value == True:
                                    return "The number 2 has digits outside the digits for its number system"
                                else:
                                    return "Число 2 имеет цифры вне цифр для его системы счисления"
                        else:
                            if sw_language.value == True:
                                return "The number 1 has digits outside the digits for its number system"
                            else:
                                return "Число 1 имеет цифры вне цифр для его системы счисления"
                    else:
                        if sw_language.value == True:
                            return "The number system of answer is not in the range [2;36]"
                        else:
                            return "Система счисления ответа не в диапозоне [2;36]"
                else:
                    if sw_language.value == True:
                        return "The number system of 2 number is not in the range [2;36]"
                    else:
                        return "Система счисления 2 числа не в диапозоне [2;36]"
            else:
                if sw_language.value == True:
                    return "The number system of 1 number is not in the range [2;36]"
                else:
                    return "Система счисления 1 числа не в диапозоне [2;36]"
        else:
            if sw_language.value == True:
                return "not all fields are filled in"
            else:
                return "Не все поля заполнены"

    def lang_change(e): # функция для переключателя языка, меняет имена полей и кнопок на экране
        if page.banner is not None:
            page.banner.open = False
        if sw_language.value == True:
            page.title = "Calculator number systems"
            num1.label = "first num"
            num2.label = "second num"
            num1_R.label = "first num"
            num2_R.label = "second num"
            system1.label = "not 1"
            system2.label = "not 2"
            system_out.label = "not out"
            calculate.text = "Calculate"
            calculate_R.text = "Calculate"

            page.navigation_bar.destinations[0].label = "systems calc"
            page.navigation_bar.destinations[1].label = "rome sys"

            if out.value is not None:
                out.value = "Answer: " + str(out.value)[6:]
            if out_R.value is not None:
                out_R.value = ""

            page.update()
        else:
            page.title = "Калькулятор систем счисления"
            num1.label = "Первое число"
            num2.label = "Второе число"
            num1_R.label = "Первое число"
            num2_R.label = "Второе число"
            system1.label = "С.С. 1"
            system2.label = "С.С. 2"
            system_out.label = "С.С. вых."
            calculate.text = "Посчитать"
            calculate_R.text = "Посчитать"

            page.navigation_bar.destinations[0].label = "Калькулятор"
            page.navigation_bar.destinations[1].label = "Римская"

            if out.value is not None:
                out.value = "Ответ: " + str(out.value)[7:]
            if out_R.value is not None:
                out_.value = ""
            page.update()
        # print("chabge:" + str(lang))

    def changetab(e): # функция смены вкладок
        # GET INDEX TAB
        my_index = e.control.selected_index
        tab_1.visible = True if my_index == 0 else False
        tab_2.visible = True if my_index == 1 else False
        page.update()

    ####visible components#### Сами визуальные компоненты
    page.title = "Калькулятор систем счисления"
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.colors.GREEN,
            primary_container=ft.colors.GREEN_200
        ),
    )
    page.window_width = 350
    page.window_height = 500
    page.window_resizable = False

    page.navigation_bar = ft.NavigationBar(
    	on_change=changetab,
    	selected_index = 0,
        destinations=[
            ft.NavigationDestination(icon=ft.icons.CALCULATE_ROUNDED, label="Калькулятор"),
            ft.NavigationDestination(icon=ft.icons.TRANSFORM_ROUNDED, label="Римская")
        ], adaptive=True
    )

    ###TAB1#### 1 страница
    num1 = ft.TextField(label="Первое число", on_change=lambda e: validate_numbers(num1, page, id=0),
        border_radius=10, border_width=2, width=200)
    num2 = ft.TextField(label="Второе число", on_change=lambda e: validate_numbers(num2, page, id=1),
        border_radius=10, border_width=2, width=200)

    operator_dropdown = ft.Dropdown(
        width=100, border_radius=10, border_width=2,
        options=[
            ft.dropdown.Option("+"),
            ft.dropdown.Option("-"),
            ft.dropdown.Option("*"),
            ft.dropdown.Option("/")
        ]
    )

    system1 = ft.TextField(label="С.С. 1", on_change=lambda e: validate_int(system1, page, id=0),
        border_radius=10, border_width=2, width=100)
    system2 = ft.TextField(label="С.С. 2", on_change=lambda e: validate_int(system2, page, id=1),
        border_radius=10, border_width=2, width=100)
    system_out = ft.TextField(label="С.С. вых.", on_change=lambda e: validate_int(system_out, page, id=2),
        border_radius=10, border_width=2, width=100)

    calculate = ft.FilledButton("Посчитать", on_click=get_result)

    out = ft.Text(size=20, selectable=True)

    ru_ = ft.Text("ru")
    sw_language = ft.Switch(label="eng", value=False, on_change=lang_change)

    ###TAB2#### 2 страница
    num1_R = ft.TextField(label="Первое число", on_change=lambda e: validate_numbers(num1_R, page, id=2),
        border_radius=10, border_width=2, width=200)
    num2_R = ft.TextField(label="Второе число", on_change=lambda e: validate_numbers(num2_R, page, id=3),
        border_radius=10, border_width=2, width=200)
    calculate_R = ft.FilledButton("Посчитать", on_click=get_result_R)
    out_R = ft.Text(size=20, selectable=True)

    ########## добавление компонентов на страницу приложения

    tab_1 = ft.Column([ft.Row([num1, system1]), operator_dropdown, ft.Row([num2, system2]), ft.Row([system_out, calculate]), out])

    tab_2 = ft.Column([num1_R, operator_dropdown, num2_R, calculate_R, out_R])
    tab_2.visible = False
    page.add(ft.Row([ru_, sw_language]), tab_1, tab_2)

ft.app(target=main)
