import flet as ft
import calculator2
import re

last_valid_value = ["",""]
last_sys = ["","",""]
regex = "^[0-9A-Z.]+$"
pattern = re.compile(regex)

def validate_numbers(field, pagee, id):
    global last_valid_value

    digits = field.value.upper()
    field.value = digits
    pagee.update()
    # print(digits.replace(",", "."))
    if digits == "":
        last_valid_value[id] = ""
    else:
        if(digits != "-" and pattern.search(digits) is not None):
            # float(digits)
            last_valid_value[id] = digits
        else:
            field.value = last_valid_value[id]
            pagee.update()

def validate_int(field, pagee, id):
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
def check_num(num_val, sys):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in num_val:
        if (digits.find(i, 0, len(digits) - 1) + 1) > int(sys):
            return False
    return True

#############################
def main(page: ft.Page):
    page.update()
    ####function#####
    def close_banner(e):
        page.banner.open = False
        page.update()

    def get_result(e):
        # check_num(num1.value, system1.value)
        chek = validate_data()
        if chek == True:
            if sw_language.value == True:
                out.value = "Answer: " + str(calculator2.num_systems(operator_dropdown.value, system1.value, num1.value,
                    system2.value, num2.value, system_out.value))
                page.update()
            else:
                out.value = "Ответ: " + str(calculator2.num_systems(operator_dropdown.value, system1.value, num1.value,
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

    def validate_data():
        # print(lang)
        if system1.value != "" and system2.value != "" and system_out.value != "" and num1.value != "" and num2.value != "":
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

    def lang_change(e):
        if page.banner is not None:
            page.banner.open = False
        if sw_language.value == True:
            page.title = "Calculator number systems"
            num1.label = "first num"
            num2.label = "second num"
            system1.label = "not 1"
            system2.label = "not 2"
            system_out.label = "not out"
            calculate.text = "Calculate"
            if out.value is not None:
                out.value = "Answer: " + str(out.value)[6:]
            page.update()
        else:
            page.title = "Калькулятор систем счисления"
            num1.label = "Первое число"
            num2.label = "Второе число"
            system1.label = "С.С. 1"
            system2.label = "С.С. 2"
            system_out.label = "С.С. вых."
            calculate.text = "Посчитать"
            if out.value is not None:
                out.value = "Ответ: " + str(out.value)[7:]
            page.update()
        # print("chabge:" + str(lang))

    def changetab(e):
        # GET INDEX TAB
        my_index = e.control.selected_index
        tab_1.visible = True if my_index == 0 else False
        tab_2.visible = True if my_index == 1 else False
        page.update()

    ####visible components####
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

    ###TAB1####
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

    ###TAB2####

    tab_1 = ft.Column([ft.Row([num1, system1]), operator_dropdown, ft.Row([num2, system2]), ft.Row([system_out, calculate]), out])

    tab_2 = ft.Text("test")

    page.add(ft.Row([ru_, sw_language]), tab_1, tab_2)

ft.app(target=main)
