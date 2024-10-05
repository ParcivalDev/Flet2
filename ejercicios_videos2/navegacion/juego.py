import flet as ft
import random

class AdivinaNumero:
    def __init__(self, page: ft.Page):
        self.page = page
        self.MAX_INTENTOS = 10
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0
        self.mejor_puntuacion = int('0')

        self.titulo = ft.Text("Adivina el Número", size=30, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE)
        self.input_numero = ft.TextField(label="Tu intento (1-100)", width=200, text_align=ft.TextAlign.CENTER, keyboard_type=ft.KeyboardType.NUMBER, on_submit=self.verificar_intento)
        self.verificar_btn = ft.ElevatedButton("Verificar", on_click=self.verificar_intento)
        self.resultado = ft.Text("Adivina el número entre 1 y 100", size=18)
        self.intentos_text = ft.Text("Intentos: 0", size=16)
        self.mejor_puntuacion_text = ft.Text(f"Mejor puntuación: {self.mejor_puntuacion}", size=16)
        self.barra_progreso = ft.ProgressBar(width=400, value=0, color=ft.colors.YELLOW)
        self.reiniciar_btn = ft.ElevatedButton("Reiniciar juego", on_click=self.reiniciar_juego)

        self.contenido_juego = ft.Column([
            self.titulo,
            self.input_numero,
            self.verificar_btn,
            self.resultado,
            self.intentos_text,
            self.mejor_puntuacion_text,
            self.barra_progreso,
            self.reiniciar_btn
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=30)

    def verificar_intento(self, e):
        self.input_numero.focus()
        try:
            intento = int(self.input_numero.value)
            if 1 <= intento <= 100:
                self.intentos += 1
                if intento == self.numero_secreto:
                    self.fin_del_juego(True)
                elif self.intentos >= self.MAX_INTENTOS:
                    self.fin_del_juego(False)
                elif intento < self.numero_secreto:
                    self.resultado.value = "Demasiado bajo, inténtalo de nuevo."
                    self.resultado.color = ft.colors.ORANGE
                else:
                    self.resultado.value = "Demasiado alto, inténtalo de nuevo."
                    self.resultado.color = ft.colors.ORANGE
                self.intentos_text.value = f"Intentos: {self.intentos}"
                self.barra_progreso.value = self.intentos / self.MAX_INTENTOS
            else:
                self.resultado.value = "Por favor, ingresa un número entre 1 y 100."
                self.resultado.color = ft.colors.RED
            self.input_numero.value = ""
            self.page.update()
        except ValueError:
            self.resultado.value = "Por favor, ingresa un número válido."
            self.resultado.color = ft.colors.RED
            self.page.update()

    def reiniciar_juego(self, e):
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0
        self.input_numero.disabled = False
        self.resultado.value = "Adivina el número entre 1 y 100"
        self.resultado.color = ft.colors.WHITE
        self.intentos_text.value = "Intentos: 0"
        self.input_numero.value = ""
        self.verificar_btn.disabled = False
        self.barra_progreso.value = 0
        self.page.update()

    def fin_del_juego(self, victoria):
        self.input_numero.disabled = True
        self.verificar_btn.disabled = True
        if victoria:
            self.resultado.value = f"¡Correcto! Lo adivinaste en {self.intentos} intentos"
            self.resultado.color = ft.colors.GREEN
            if self.intentos < self.mejor_puntuacion or self.mejor_puntuacion == 0:
                self.mejor_puntuacion = self.intentos
                self.mejor_puntuacion_text.value = f"Mejor puntuación: {self.mejor_puntuacion}"
        else:
            self.resultado.value = f"¡Se acabaron los intentos! El número era {self.numero_secreto}"
            self.resultado.color = ft.colors.RED
        self.page.update()

    def get_view(self):
        return ft.Container(
            content=self.contenido_juego,
            padding=20,
            border_radius=10,
            border=ft.border.all(2, ft.colors.BLUE_200),
            expand=True
        )

