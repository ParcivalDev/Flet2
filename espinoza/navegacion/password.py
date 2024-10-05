import flet as ft
import random
import string


class GeneradorPassword:

    def __init__(self, page: ft.Page):
        self.page = page
        self.init_components()

    def init_components(self):
        self.titulo = ft.Text("Generador de contraseñas",
                              size=32, weight=ft.FontWeight.BOLD)
        self.etiqueta_password = ft.TextField(
            read_only=True,
            width=400,
            text_align=ft.TextAlign.CENTER,
            text_style=ft.TextStyle(size=20, weight=ft.FontWeight.BOLD)
        )
        self.etiqueta_fuerza = ft.Text("", size=16)
        self.slider_pass = ft.Slider(
            min=6, max=24, divisions=18,
            label="{value}", value=12, on_change=self.actualiza_pass
        )

        self.boton_generador = ft.ElevatedButton(
            "Generar contraseña", on_click=self.actualiza_pass, icon=ft.icons.REFRESH_ROUNDED
        )

        self.boton_copiar = ft.ElevatedButton(
            "Copiar contraseña", on_click=self.copiar_password, icon=ft.icons.COPY
        )

        self.mayusculas_switch = ft.Switch(
            label="Incluir mayúsculas", value=True, on_change=self.actualiza_pass)
        self.numeros_switch = ft.Switch(
            label="Incluir números", value=True, on_change=self.actualiza_pass)
        self.simbolos_switch = ft.Switch(
            label="Incluir símbolos", value=True, on_change=self.actualiza_pass)

        self.contenedor_principal = ft.Container(
            content=ft.Column([
                ft.Container(self.titulo, alignment=ft.alignment.center),
                ft.Container(self.etiqueta_password,
                             alignment=ft.alignment.center),
                ft.Container(self.etiqueta_fuerza,
                             alignment=ft.alignment.center),
                self.slider_pass,
                self.mayusculas_switch,
                self.numeros_switch,
                self.simbolos_switch,
                ft.Row([self.boton_generador, self.boton_copiar],
                       alignment=ft.MainAxisAlignment.CENTER)
            ], spacing=20, alignment=ft.MainAxisAlignment.CENTER),
            padding=20,
            bgcolor=ft.colors.GREY_800,
            border_radius=20
        )

        # Define una función para generar contraseñas
    def genera_pass(self, tamanho, mayuscula, numeros, simbolos):
        caracteres = string.ascii_lowercase
        if mayuscula:
            caracteres += string.ascii_uppercase
        if numeros:
            caracteres += string.digits
        if simbolos:
            caracteres += string.punctuation
        return ''.join(random.choice(caracteres) for _ in range(tamanho))

    # Define una función para calcular la fuerza de la contraseña
    def calcula_fuerza(self, password):
        longitud = len(password)
        if longitud < 10 and self.numeros_switch.value == False:
            return "Débil"
        elif longitud < 14:
            return "Moderada"
        else:
            return "Fuerte"

    # Define una función para actualizar la contraseña
    def actualiza_pass(self, e):
        nueva_pass = self.genera_pass(
            int(self.slider_pass.value),
            self.mayusculas_switch.value,
            self.numeros_switch.value,
            self.simbolos_switch.value
        )
        # Actualiza el campo de texto con la nueva contraseña
        self.etiqueta_password.value = nueva_pass
        # Calcula la fuerza de la nueva contraseña
        fuerza = self.calcula_fuerza(nueva_pass)
        self.etiqueta_fuerza.value = f"Fuerza: {fuerza}"
        self.etiqueta_fuerza.color = {
            "Débil": ft.colors.RED,
            "Moderada": ft.colors.ORANGE,
            "Fuerte": ft.colors.GREEN
        }.get(fuerza, ft.colors.BLACK)
        self.page.update()

    # Define una función para copiar la contraseña al portapapeles
    def copiar_password(self, e):
        # Copia la contraseña al portapapeles
        self.page.set_clipboard(self.etiqueta_password.value)
        # Crea un mensaje de notificación
        notificacion = ft.SnackBar(
            ft.Text("Contraseña copiada al portapapeles"))
        self.page.overlay.append(notificacion)
        notificacion.open = True  # Muestra el mensaje de notificación
        self.page.update()  # Actualiza la página

    def mostrar_dialogo(self):
        dialog = ft.AlertDialog(
            content=self.contenedor_principal,
            actions=[
                ft.TextButton(
                    "Cerrar", on_click=lambda _: self.cerrar_dialogo(dialog))
            ],
        )
        self.page.overlay.append(dialog)
        dialog.open = True
        self.actualiza_pass(None)
        self.page.update()

    def cerrar_dialogo(self, dialog):
        dialog.open = False
        self.page.update()
