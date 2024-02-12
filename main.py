import flet as ft
# import calculator.py

last_valid_value = ["",""]
last_sys = ["","",""]

def validate_numbers(field, pagee, id):
    global last_valid_value

    digits = field.value
    # print(digits.replace(",", "."))
    if digits == "":
        last_valid_value[id] = ""
    else:
        try:
            if(digits != "-"):
                float(digits)
                last_valid_value[id] = digits.replace(",", ".")
            # print(float(digits))
        except ValueError:
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
    page.window_width = 500
    page.window_height = 500

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


    def get_result(num1_, system1_,
        operator_dropdown_, num2_, system2_, system_out_):
        pass
    calculate = ft.ElevatedButton("Посчитать", on_click=get_result(num1, system1,
        operator_dropdown, num2, system2, system_out))



    page.add(ft.Row([num1, system1]),
        operator_dropdown,
        ft.Row([num2, system2]),
        ft.Row([system_out, calculate]))
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
