import flet as ft 

def main(page: ft.Page):
    # page.add(ft.Text("Hello world"))
    page.title = 'Мое первое приложение на Flet'

    greeting_text = ft.Text("Привет, мир!")

    name_input = ft.TextField(label="Введите имя:")

    def on_button_click(_):
        name = name_input.value.strip()

        if name:
            greeting_text.value = f"Привет, {name}!"
        else:
            greeting_text.value = "Пожалуйте, введите имя!" 
        
        print(greeting_text.value)
        page.update()

    greet_button = ft.ElevatedButton("Отправить", on_click=on_button_click)

    page.add(greeting_text, name_input, greet_button)


ft.app(target=main)