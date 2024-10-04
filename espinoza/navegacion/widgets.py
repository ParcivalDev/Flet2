import flet as ft

class EjemplosWidgets:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.padding = 20
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.scroll = ft.ScrollMode.ADAPTIVE

    def create_widget_example(self, title: str, description: str, content: ft.Control) -> ft.Container:
        return ft.Container(
            content=ft.Column([
                ft.Text(title, size=24, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_200),
                ft.Text(description, color=ft.colors.GREY_300, size=16),
                ft.Container(
                    content=content,
                    padding=20,
                    border_radius=10,
                    bgcolor=ft.colors.BLUE_GREY_800,
                ),
            ], spacing=10),
            width=self.page.width,
            margin=ft.margin.only(bottom=30),
            padding=20,
            border_radius=15,
            bgcolor=ft.colors.BLUE_GREY_700,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=10,
                color=ft.colors.BLACK54,
                offset=ft.Offset(20, 10),
            )
        )

    def create_stack_example(self):
        stack_demo = ft.Stack([
            ft.Container(width=200, height=200, bgcolor=ft.colors.GREEN_400, border_radius=10),
            ft.Container(width=150, height=150, bgcolor=ft.colors.AMBER_400, left=25, top=25, border_radius=10),
            ft.Container(
                content=ft.Text("Stack", color=ft.colors.WHITE, size=16, weight=ft.FontWeight.BOLD),
                width=100, height=100, bgcolor=ft.colors.BLUE_400,
                left=50, top=50, alignment=ft.alignment.center, border_radius=10
            ),
        ])
        return self.create_widget_example(
            "Stack", "Stack permite superponer widgets unos encima de otros", stack_demo
        )

    def create_image_example(self):
        image_url = ft.Image(src="https://picsum.photos/200/200", width=200, border_radius=10)
        image_local = ft.Image(src="espinoza/stack_img_avatar/images/imagen.png", width=200, border_radius=10)
        row_image = ft.Row([
            ft.Column([ft.Text("Imagen desde URL", size=14, color=ft.colors.GREY_300), image_url]),
            ft.Column([ft.Text("Imagen local", size=14, color=ft.colors.GREY_300), image_local]),
        ], alignment=ft.MainAxisAlignment.SPACE_AROUND)
        return self.create_widget_example(
            "Image", "Comparación de imagen de Internet e imagen local", row_image
        )

    def create_avatar_example(self):
        avatar_with_image = ft.CircleAvatar(
            foreground_image_src="https://avatars.githubusercontent.com/u/173951868",
            radius=50
        )
        avatar_with_text = ft.CircleAvatar(
            content=ft.Text("PD", size=30, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
            radius=50,
            bgcolor=ft.colors.BLUE_400
        )
        row_avatar = ft.Row([
            ft.Column([ft.Text("Con imagen", size=14, color=ft.colors.GREY_300), avatar_with_image]),
            ft.Column([ft.Text("Con texto", size=14, color=ft.colors.GREY_300), avatar_with_text]),
        ], alignment=ft.MainAxisAlignment.SPACE_AROUND, spacing=20)
        return self.create_widget_example(
            "CircleAvatar", "Ejemplos de CircleAvatar con imagen y texto", row_avatar
        )

    def get_view(self):
        title = ft.Text(
            "Stack, Image y CircleAvatar",
            size=40,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.BLUE_200,
            text_align=ft.TextAlign.CENTER
        )
        divider_with_margin = ft.Container(
            content=ft.Divider(color=ft.colors.BLUE_200, height=2),
            margin=ft.margin.symmetric(vertical=20)
        )
        return ft.Column([
            title,
            divider_with_margin,
            self.create_stack_example(),
            self.create_image_example(),
            self.create_avatar_example(),
        ])