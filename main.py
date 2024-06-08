import flet as ft

def main(page: ft.Page):
    page.bgcolor=ft.colors.BLACK
    page.scroll=ft.ScrollMode.ALWAYS


    product_images = ft.Container(
        content=ft.Column(      
            controls=[
                ft.Image(
                    src='https://lojasbecker.vteximg.com.br/arquivos/ids/2786124-1000-1000/1-cadeira-sala-de-jantar-dj-serena-freij.jpg?v=638527730690930000',
                ),
                ft.Row(
                    controls=[
                        ft.Container(
                            image_src='https://lojasbecker.vteximg.com.br/arquivos/ids/2786124-1000-1000/1-cadeira-sala-de-jantar-dj-serena-freij.jpg?v=638527730690930000',
                            width=80,
                            height=80,
                        ),
                        ft.Container(
                            image_src='https://lojasbecker.vteximg.com.br/arquivos/ids/2786124-1000-1000/1-cadeira-sala-de-jantar-dj-serena-freij.jpg?v=638527730690930000',
                            width=80,
                            height=80,
                        ),
                
                    ]
                )
                
            ]
        )
    )
    product_details = ft.Container()

    layout = ft.Container(
        width=900,
        margin=ft.margin.all(30),
        shadow=ft.BoxShadow(blur_radius=300, color=ft.colors.CYAN),
        content=ft.ResponsiveRow(
            columns=12,
            spacing=0,
            run_spacing=0,
            controls=[
                product_images,
                product_details
            ]
        )
    )

    center = ft.Container(
        alignment=ft.alignment.center,
        content=layout
    )



    page.add(center)
if __name__ == '__main__':
    ft.app(target=main)