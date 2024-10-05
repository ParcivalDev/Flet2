import flet as ft  
import random 
import string  # Importa el módulo string para acceder a conjuntos de caracteres predefinidos

def main(page: ft.Page):  
    page.title = "Generador de contraseñas"  
    page.padding = 20  
    page.bgcolor = ft.colors.GREY_900  


    # Define una función para generar contraseñas
    def genera_pass(tamanho, mayuscula, numeros, simbolos):  
        caracteres = string.ascii_lowercase 
        if mayuscula:
            caracteres += string.ascii_uppercase  
        if numeros:
            caracteres += string.digits  
        if simbolos:
            caracteres += string.punctuation  
        return ''.join(random.choice(caracteres) for _ in range(tamanho))  


    # Define una función para calcular la fuerza de la contraseña
    def calcula_fuerza(password):
        longitud = len(password)
        if longitud < 10 and numeros_switch.value == False:
            return "Débil"
        elif longitud < 14:
            return "Moderada"
        else:
            return "Fuerte"


    # Define una función para actualizar la contraseña
    def actualiza_pass(e):  
        nueva_pass = genera_pass(
            int(slider_pass.value),
            mayusculas_switch.value,
            numeros_switch.value,
            simbolos_switch.value
        )
        etiqueta_password.value = nueva_pass  # Actualiza el campo de texto con la nueva contraseña
        fuerza = calcula_fuerza(nueva_pass)  # Calcula la fuerza de la nueva contraseña
        etiqueta_fuerza.value = f"Fuerza: {fuerza}"
        etiqueta_fuerza.color = {
            "Débil": ft.colors.RED,
            "Moderada": ft.colors.ORANGE,
            "Fuerte": ft.colors.GREEN
        }.get(fuerza, ft.colors.BLACK)
        page.update()


    # Define una función para copiar la contraseña al portapapeles
    def copiar_password(e):
        page.set_clipboard(etiqueta_password.value)  # Copia la contraseña al portapapeles
        notificacion = ft.SnackBar(ft.Text("Contraseña copiada al portapapeles"))  # Crea un mensaje de notificación
        page.overlay.append(notificacion)
        notificacion.open = True  # Muestra el mensaje de notificación
        page.update()  # Actualiza la página



    titulo = ft.Text("Generador de contraseñas", size=32, weight=ft.FontWeight.BOLD)
    
    etiqueta_password = ft.TextField(
        read_only=True,
        width=400,
        text_align=ft.TextAlign.CENTER,
        text_style=ft.TextStyle(size=20, weight=ft.FontWeight.BOLD)
    )

    etiqueta_fuerza = ft.Text("", size=16)

    slider_pass = ft.Slider(
        min=6, max=24, divisions=18,
        label="{value}", value=12, on_change=actualiza_pass
    )

    boton_generador = ft.ElevatedButton(
        "Generar contraseña", on_click=actualiza_pass, icon=ft.icons.REFRESH_ROUNDED
    )

    boton_copiar = ft.ElevatedButton(
        "Copiar contraseña", on_click=copiar_password, icon=ft.icons.COPY
    )


    mayusculas_switch = ft.Switch(label="Incluir mayúsculas", value=True, on_change=actualiza_pass)
    numeros_switch = ft.Switch(label="Incluir números", value=True, on_change=actualiza_pass)
    simbolos_switch = ft.Switch(label="Incluir símbolos", value=True, on_change=actualiza_pass)


    contenedor_principal = ft.Container(
        content=ft.Column([
            ft.Container(titulo, alignment=ft.alignment.center),
            ft.Container(etiqueta_password, alignment=ft.alignment.center),
            ft.Container(etiqueta_fuerza, alignment=ft.alignment.center),
            slider_pass,
            mayusculas_switch,
            numeros_switch,
            simbolos_switch,
            ft.Row([boton_generador, boton_copiar], alignment=ft.MainAxisAlignment.CENTER)
        ], spacing=20, alignment=ft.MainAxisAlignment.CENTER),
        padding=20,
        bgcolor=ft.colors.GREY_800,
        border_radius=20
    )

    page.add(contenedor_principal)

    actualiza_pass(None)  # Muestra una contraseña al iniciar la app

ft.app(main)