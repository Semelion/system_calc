import flet as ft
import calculator2
import re

lang = False
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


def main(page: ft.Page):
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

    def get_result(e):
        if lang == True:
            out.value = "Answer: " + str(calculator2.num_systems(operator_dropdown.value, system1.value, num1.value,
                system2.value, num2.value, system_out.value))
            page.update()
        else:
            out.value = "Ответ: " + str(calculator2.num_systems(operator_dropdown.value, system1.value, num1.value,
                system2.value, num2.value, system_out.value))
            page.update()


    calculate = ft.FilledButton("Посчитать", on_click=get_result)

    out = ft.Text(size=20, selectable=True)

    def lang_change(e):
        if sw_language.value == True:
            num1.label = "first num"
            num2.label = "second num"
            system1.label = "not 1"
            system2.label = "not 2"
            system_out.label = "not out"
            out.value = "Answer: " + str(out.value)[6:]
            lang = True
            page.update()
        else:
            num1.label = "Первое число"
            num2.label = "Второе число"
            system1.label = "С.С. 1"
            system2.label = "С.С. 2"
            system_out.label = "С.С. вых."
            out.value = "Ответ: " + str(out.value)[7:]
            lang = True
            page.update()


    ru_ = ft.Text("ru")
    sw_language = ft.Switch(label="eng", value=False, on_change=lang_change)

    page.add(ft.Row([ru_, sw_language]),
        ft.Row([num1, system1]),
        operator_dropdown,
        ft.Row([num2, system2]),
        ft.Row([system_out, calculate]),
        out
        )
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # txt_number = ft.TextField(value="0", text_align="right", width=100)

    # def minus_click(e):
    #     txt_number.value = str(int(txt_number.value) - 1)
    #     page.update()
    #
    # def plus_click(e):
    #     txt_number.value = str(int(txt_number.value) + 1)
    #     page.update()
    #
    # page.add(
    #     ft.Row(
    #         [
    #             ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
    #             txt_number,
    #             ft.IconButton(ft.icons.ADD, on_click=plus_click),
    #         ],
    #         alignment=ft.MainAxisAlignment.CENTER,
    #     )
    # )

    # first_name = ft.TextField(label="Первое число", autofocus=True)
    # last_name = ft.TextField(label="Второе число")
    # greetings = ft.Column()
    #
    # def btn_click(e):
    #
    #     greetings.controls.append(ft.Text(f"Hello, {first_name.value} {last_name.value}!"))
    #     first_name.value = ""
    #     last_name.value = ""
    #     page.update()
    #     first_name.focus()
    #
    # page.add(
    #     first_name,
    #     last_name,
    #     ft.ElevatedButton("Посчитать", on_click=btn_click),
    #     greetings,
    # )

ft.app(target=main)
