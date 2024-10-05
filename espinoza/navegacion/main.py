import flet as ft
from flet import ControlEvent
from juego import AdivinaNumero
from widgets import EjemplosWidgets
from password import GeneradorPassword

def main(page: ft.Page):
    page.title = "FletApp"
    page.bgcolor = ft.colors.BLUE_GREY_900
    page.padding = 20
    page.window.resizable = False
    page.window.width = 600
    page.window.height = 700
    page.theme_mode = ft.ThemeMode.DARK

    # Inicialización de las clases de juego y widgets
    juego = AdivinaNumero(page)
    widgets = EjemplosWidgets(page)
    generador_password = GeneradorPassword(page)

    # Función para manejar los cambios en la barra de navegación
    def navegacion_change(e: ControlEvent):
        selected_index = e.data
        if selected_index == "0":
            vista_juego()
        elif selected_index == "1":
            vista_inicio()
        elif selected_index == "2":
            vista_widgets()
        page.update()

    # Función para mostrar la vista del juego
    def vista_juego():
        page.controls.clear()
        page.add(
            ft.Container(content=ft.Text("Juego Adivina el Número", size=24,
                         weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_200), margin=10),
            juego.get_view(),
            navegacion
        )

    # Función para mostrar la vista de widgets
    def vista_widgets():
        page.controls.clear()
        page.add(
            ft.Container(content=ft.Text("Ejemplos de Widgets", size=24,
                         weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_200), margin=10),
            widgets.get_view(),
            navegacion
        )

    # Función para mostrar la vista de inicio
    def vista_inicio():
        page.controls.clear()
        contenido_inicio = ft.Column([
            # Título de bienvenida
            ft.Container(
                content=ft.Text("Bienvenido a FletApp Showcase", size=28,
                                weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_200),
                margin=ft.margin.only(bottom=20), alignment=ft.alignment.center
            ),
            # Descripción de la aplicación
            ft.Container(
                content=ft.Text("Esta aplicación demuestra las capacidades de Flet para crear interfaces de usuario atractivas y funcionales.",
                                size=16, color=ft.colors.GREY_400),
                margin=ft.margin.only(bottom=30)
            ),
            # Tarjetas de características
            ft.Row([
                crear_tarjeta(
                    "Juego", "Prueba tus habilidades con 'Adivina el Número'", ft.icons.GAMES),
                crear_tarjeta(
                    "Widgets", "Explora ejemplos de widgets interactivos", ft.icons.WIDGETS)
            ])
        ])

        page.add(contenido_inicio, navegacion)

    # Función auxiliar para crear tarjetas de características
    def crear_tarjeta(titulo, descripcion, icono):
        return ft.Container(
            content=ft.Column([
                ft.Icon(icono, size=40, color=ft.colors.BLUE_400),
                ft.Text(titulo, weight=ft.FontWeight.BOLD, size=18),
                ft.Text(descripcion, size=14, color=ft.colors.GREY_400,
                        text_align=ft.TextAlign.JUSTIFY)
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
            width=250,
            height=200,
            border=ft.border.all(1, ft.colors.BLUE_200),
            border_radius=10,
            padding=20,
            margin=10
        )

    # Creación de la barra de navegación
    navegacion = ft.NavigationBar(
        selected_index=1,
        on_change=navegacion_change,
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.GAMES, label="Juego"),
            ft.NavigationBarDestination(icon=ft.icons.HOME, label="Inicio"),
            ft.NavigationBarDestination(icon=ft.icons.WIDGETS, label="Widgets")
        ],
        bgcolor=ft.colors.BLUE_800,
        indicator_color=ft.colors.AMBER
    )
    
    def mostrar_generador_password(e):
        generador_password.mostrar_dialogo()
    
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.PASSWORD,
        on_click=mostrar_generador_password,
        tooltip="Generar Contraseña"
    )

    # Iniciar la aplicación mostrando la vista de inicio
    vista_inicio()


ft.app(main)
