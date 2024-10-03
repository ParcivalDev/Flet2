import flet as ft


def main(page: ft.Page):
    page.bgcolor = ft.colors.BLUE_GREY_900
    page.title = "Ejemplo vídeo 8"
    page.theme_mode = ft.ThemeMode.DARK
    # Añadimos un relleno de 20 píxeles alrededor de toda la página
    page.padding = 20
    # Alineamos horizontalmente el contenido al centro
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ADAPTIVE

    # Definimos una función para crear ejemplos de widgets
    # def create_widget_example(title, description, content):
    def create_widget_example(title: str, description: str, content: ft.Control) -> ft.Container:
        # Retornamos un contenedor con un diseño específico para cada ejemplo
        return ft.Container(
            # El contenido es una columna con título, descripción y el widget de ejemplo
            content=ft.Column([
                ft.Text(title, size=24, weight=ft.FontWeight.BOLD,
                        color=ft.colors.BLUE_200),
                ft.Text(description, color=ft.colors.GREY_300, size=16),
                # Contenedor para el widget de ejemplo
                ft.Container(
                    content=content,
                    padding=20,
                    border_radius=10,
                    bgcolor=ft.colors.BLUE_GREY_800,
                ),
            ], spacing=10),
            width=page.width,
            margin=ft.margin.only(bottom=30),
            padding=20,
            border_radius=15,
            bgcolor=ft.colors.BLUE_GREY_700,
            # Añadimos una sombra para dar profundidad
            shadow=ft.BoxShadow(
                spread_radius=1, # Determina cuánto se expande la sombra
                blur_radius=10, # Define qué tan difusa o borrosa es la sombra
                color=ft.colors.BLACK54,
                offset=ft.Offset(20, 10), # El offset determina la posición de la sombra en relación con el contenedor
            )
        )

    # Creamos un ejemplo de Stack (apilamiento de widgets)
    stack_demo = ft.Stack([
        # Contenedor verde de fondo
        ft.Container(width=200, height=200,
                     bgcolor=ft.colors.GREEN_400, border_radius=10),
        # Contenedor ámbar superpuesto
        ft.Container(width=150, height=150, bgcolor=ft.colors.AMBER_400,
                     left=25, top=25, border_radius=10),
        # Contenedor azul con texto superpuesto
        ft.Container(
            content=ft.Text("Stack", color=ft.colors.WHITE,
                            size=16, weight=ft.FontWeight.BOLD),
            width=100, height=100, bgcolor=ft.colors.BLUE_400,
            left=50, top=50, alignment=ft.alignment.center, border_radius=10
        ),
    ])

    stack_example = create_widget_example(
        "Stack", "Stack permite superponer widgets unos encima de otros", stack_demo
    )

    # Creamos ejemplos de Image
    # Imagen desde URL
    image_url = ft.Image(src="https://picsum.photos/200/200",
                         width=200, border_radius=10)
    # Imagen local
    image_local = ft.Image(
        src="espinoza/stack/images/imagen.png", width=200, border_radius=10)


    # Creamos una fila para mostrar ambas imágenes con un texto por encima
    row_image = ft.Row([
        ft.Column([ft.Text("Imagen desde URL", size=14,
                  color=ft.colors.GREY_300), image_url]),
        ft.Column([ft.Text("Imagen local", size=14,
                  color=ft.colors.GREY_300), image_local]),
    ], alignment=ft.MainAxisAlignment.SPACE_AROUND)

    # Creamos el ejemplo de Image usando nuestra función personalizada
    image_example = create_widget_example(
        "Image", "Comparación de imagen de Internet e imagen local", row_image
    )


    # Creamos ejemplos de CircleAvatar
    # Avatar con imagen
    avatar_with_image = ft.CircleAvatar(
        foreground_image_src="https://avatars.githubusercontent.com/u/173951868",
        radius=50
    )
    # Avatar con texto
    avatar_with_text = ft.CircleAvatar(
        content=ft.Text("PD", size=30, weight=ft.FontWeight.BOLD,
                        color=ft.colors.WHITE),
        radius=50,
        bgcolor=ft.colors.BLUE_400
    )

    # Creamos una fila para mostrar ambos avatares
    row_avatar = ft.Row([
        ft.Column(
            [ft.Text("Con imagen", size=14, color=ft.colors.GREY_300), avatar_with_image]),
        ft.Column(
            [ft.Text("Con texto", size=14, color=ft.colors.GREY_300), avatar_with_text]),
    ], alignment=ft.MainAxisAlignment.SPACE_AROUND, spacing=20)


    avatar_example = create_widget_example(
        "CircleAvatar", "Ejemplos de CircleAvatar con imagen y texto", row_avatar
    )

    # Título principal de la página
    title = ft.Text(
        "Stack, Image y CircleAvatar",
        size=40,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.BLUE_200,
        text_align=ft.TextAlign.CENTER
    )

    # Creamos un divisor con márgenes
    divider_with_margin = ft.Container(
        content=ft.Divider(color=ft.colors.BLUE_200, height=2),
        # 20 píxeles de margen arriba y abajo
        margin=ft.margin.symmetric(vertical=20)
    )

    page.add(
        title,
        divider_with_margin,
        stack_example,
        image_example,
        avatar_example,
    )

ft.app(main)
