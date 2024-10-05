import flet as ft
import random


def main(page: ft.Page):
    page.title = "Adivina el Número"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 50  # Añade un espacio de 50 píxeles alrededor del contenido
    page.window.width = 600
    page.window.height = 700

    MAX_INTENTOS = 10  # Define el número máximo de intentos permitidos

    # Inicializamos las variables del juego
    # Genera un número aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)
    intentos = 0  # Contador de intentos, inicializado en 0
    mejor_puntuacion = int('0')  # Mejor puntuación, inicializada en 0

    # Función que se ejecuta cada vez que el jugador hace un intento
    def verificar_intento(e):
        nonlocal intentos, mejor_puntuacion
        input_numero.focus()  # Mantiene el foco en el campo de entrada
        try:
            intento = int(input_numero.value)
            if 1 <= intento <= 100:
                intentos += 1
                if intento == numero_secreto:
                    fin_del_juego(True)
                elif intentos >= MAX_INTENTOS:
                    fin_del_juego(False)
                elif intento < numero_secreto:
                    resultado.value = "Demasiado bajo, inténtalo de nuevo."
                    resultado.color = ft.colors.ORANGE
                else:
                    resultado.value = "Demasiado alto, inténtalo de nuevo."
                    resultado.color = ft.colors.ORANGE
                intentos_text.value = f"Intentos: {intentos}"
                barra_progreso.value = intentos / MAX_INTENTOS  # Actualiza la barra de progreso
            else:
                resultado.value = "Por favor, ingresa un número entre 1 y 100."
                resultado.color = ft.colors.RED
            input_numero.value = ""
            page.update()
        except ValueError:
            resultado.value = "Por favor, ingresa un número válido."
            resultado.color = ft.colors.RED
            page.update()

    # Función para reiniciar el juego
    def reiniciar_juego(e):
        nonlocal numero_secreto, intentos
        # Genera un nuevo número secreto
        numero_secreto = random.randint(1, 100)
        intentos = 0  # Reinicia el contador de intentos
        input_numero.disabled = False  # Habilita el campo de entrada
        resultado.value = "Adivina el número entre 1 y 100"
        resultado.color = ft.colors.WHITE
        intentos_text.value = "Intentos: 0"
        input_numero.value = ""
        verificar_btn.disabled = False
        barra_progreso.value = 0  # Reinicia la barra de progreso
        page.update()

    # Función que se llama cuando el juego termina
    def fin_del_juego(victoria):
        input_numero.disabled = True  # Deshabilita el campo de entrada
        verificar_btn.disabled = True  # Deshabilita el botón de verificar
        if victoria:
            resultado.value = f"¡Correcto! Lo adivinaste en {intentos} intentos"
            resultado.color = ft.colors.GREEN
            if intentos < mejor_puntuacion or mejor_puntuacion == 0:
                mejor_puntuacion = intentos
                mejor_puntuacion_text.value = f"Mejor puntuación: {mejor_puntuacion}"
        else:
            resultado.value = f"¡Se acabaron los intentos! El número era {numero_secreto}"
            resultado.color = ft.colors.RED
        page.update()

    titulo = ft.Text("Adivina el Número", size=30,
                     weight=ft.FontWeight.BOLD, color=ft.colors.BLUE)

    input_numero = ft.TextField(
        label="Tu intento (1-100)",
        width=200,
        text_align=ft.TextAlign.CENTER,
        keyboard_type=ft.KeyboardType.NUMBER,
        on_submit=verificar_intento  # Llama a verificar_intento cuando se presiona Enter
    )

    verificar_btn = ft.ElevatedButton(
        "Verificar",
        on_click=verificar_intento,
        style=ft.ButtonStyle(
            color={
                ft.ControlState.DEFAULT: ft.colors.WHITE,
                ft.ControlState.DISABLED: ft.colors.GREY_300
            },
            bgcolor={
                ft.ControlState.DEFAULT: ft.colors.BLUE,
                ft.ControlState.DISABLED: ft.colors.GREY_700
            }
        )
    )

    resultado = ft.Text("Adivina el número entre 1 y 100", size=18)
    intentos_text = ft.Text("Intentos: 0", size=16)
    mejor_puntuacion_text = ft.Text(
        f"Mejor puntuación: {mejor_puntuacion}", size=16)

    barra_progreso = ft.ProgressBar(width=400, value=0, color=ft.colors.YELLOW)

    reiniciar_btn = ft.ElevatedButton(
        "Reiniciar juego",
        on_click=reiniciar_juego,
        style=ft.ButtonStyle(
            color={ft.ControlState.DEFAULT: ft.colors.WHITE},
            bgcolor={ft.ControlState.DEFAULT: ft.colors.RED}
        )
    )

    # Función para cambiar entre tema claro y oscuro
    def cambiar_tema(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            tema_btn.text = "Modo oscuro"
        else:
            page.theme_mode = ft.ThemeMode.DARK
            tema_btn.text = "Modo claro"
        page.update()

    tema_btn = ft.ElevatedButton(
        "Modo claro",
        on_click=cambiar_tema,
        style=ft.ButtonStyle(
            color={ft.ControlState.DEFAULT: ft.colors.BLACK},
            bgcolor={ft.ControlState.DEFAULT: ft.colors.YELLOW}
        )
    )

    # Organización de los elementos en la interfaz
    contenido_juego = ft.Column([
        titulo,
        input_numero,
        verificar_btn,
        intentos_text,
        mejor_puntuacion_text,
        barra_progreso,
        reiniciar_btn,
        tema_btn
    ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=30)

    page.add(
        ft.Container(
            content=contenido_juego,
            padding=20,
            border_radius=10,
            border=ft.border.all(2, ft.colors.BLUE_200),
            expand=True
        )
    )


ft.app(target=main)


