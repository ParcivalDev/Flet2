import flet as ft
import random


def main(page: ft.Page):
    page.title = "Adivina el número"
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    titulo = ft.Text("Cards, Divider y VerticalDivider en Flet",
                     size=30, weight=ft.FontWeight.BOLD)

    numero_secreto = random.randint(1, 10)
    intentos = 0

    def verificar_intento(e):
        nonlocal intentos
        try:
            intento = int(input_numero.value)
            intentos += 1
            if intento == numero_secreto:
                resultado.value = f"¡Correcto! Lo adivinaste en {intentos} intentos"
                resultado.color = ft.colors.GREEN
                verificar_btn.disabled = True
            elif intento < numero_secreto:
                resultado.value = "Demasiado bajo, inténtalo de nuevo."
                resultado.color = ft.colors.ORANGE
            else:
                resultado.value = "Demasiado alto, inténtalo de nuevo."
                resultado.color = ft.colors.ORANGE
            intentos_text.value = f"Intentos: {intentos}"
            page.update()
        except ValueError:
            resultado.value = "Por favor, ingresa un número válido."
            resultado.color = ft.colors.RED
            page.update()

    def reiniciar_juego(e):
        nonlocal numero_secreto, intentos
        numero_secreto = random.randint(1, 10)
        intentos = 0
        resultado.value = "Adivina el número entre 1 y 10"
        resultado.color = ft.colors.WHITE
        intentos_text.value = "Intentos: 0"
        input_numero.value = ""
        verificar_btn.disabled = False
        page.update()

    titulo_juego = ft.Text("Adivina el número", size=20,
                           weight=ft.FontWeight.BOLD)
    input_numero = ft.TextField(label="Tu intento", width=100)
    verificar_btn = ft.ElevatedButton("Verificar", on_click=verificar_intento)
    resultado = ft.Text("Adivina el número entre 1 y 10")
    intentos_text = ft.Text("Intentos: 0")
    reiniciar_btn = ft.ElevatedButton(
        "Reiniciar juego", on_click=reiniciar_juego)

    divisor_hor = ft.Divider(height=1, color=ft.colors.BLUE_300)
    divisor_ver = ft.VerticalDivider(width=1, color=ft.colors.BLUE_300)

    card_uno = ft.Card(
        content=ft.Container(
            content=ft.Column([titulo_juego, input_numero, verificar_btn, resultado, intentos_text,
                               reiniciar_btn], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
            padding=10
        ),
        width=300,
        height=400
    )

    def cambiar_tema(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            tema_btn.text = "Modo oscuro"
        else:
            page.theme_mode = ft.ThemeMode.DARK
            tema_btn.text = "Modo claro"
        page.update()

    titulo_tema = ft.Text("Cambiar tema", size=20, weight=ft.FontWeight.BOLD)
    tema_btn = ft.ElevatedButton("Modo Claro", on_click=cambiar_tema)

    columna_tema = ft.Column(
        controls=[titulo_tema, tema_btn],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    card_dos = ft.Card(
        content=ft.Container(
            content=columna_tema,
            padding=10
        ),
        width=250,
        height=150
    )

    fila = ft.Row(
        controls=[card_uno, divisor_ver, card_dos],
        alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(titulo, divisor_hor, fila)


ft.app(target=main)
