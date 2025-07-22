import flet as ft
from core.state import estado
from db.database import conectar
from components.entradas import *
from components.mensagens import *
from components.icons import *
from utils.funcoes import *
from core.customButtons import *
from core.customContainers import *
from core.customTexts import *
from core.user_manager import UserManager
from PIL import Image
import io
import base64
import time

def mostrar_tela_edicao_perfil(page: ft.Page, imagem_base64: str):
    page.controls.clear()

    import core.menu as menu

    u = estado.usuario_logado
    nome_perfil.value = u.nome
    email_perfil.value = u.email

    icon_eyeoff_senha_perfil.on_click = lambda e: toggle_password_perfil(page, senha_perfil, container_senha_perfil)
    icon_eyeon_senha_perfil.on_click = lambda e: toggle_password_perfil(page, senha_perfil, container_senha_perfil)
    icon_eyeoff_nova_senha_perfil.on_click = lambda e: toggle_password_perfil(page, senha_nova_perfil, container_senha_nova_perfil)
    icon_eyeon_nova_senha_perfil.on_click = lambda e: toggle_password_perfil(page, senha_nova_perfil, container_senha_nova_perfil)

    nome_perfil.on_change = lambda e: validar_nome(page, nome_perfil, container_nome_perfil, nome_perfil_msg, icon_name_perfil, icon_red_name_perfil)
    email_perfil.on_change = lambda e: validar_email(page, email_perfil, container_email_perfil, email_perfil_msg, icon_email_perfil, icon_red_email_perfil)
    senha_perfil.on_change = lambda e: validar_senha_atual(page, senha_perfil, container_senha_perfil, senha_perfil_msg, icon_eyeon_senha_perfil, icon_eyeoff_senha_perfil, icon_red_eyeon_senha_perfil, icon_red_eyeoff_senha_perfil)
    senha_nova_perfil.on_change = lambda e: validar_nova_senha(page, senha_perfil, senha_nova_perfil, container_senha_nova_perfil, nova_senha_perfil_msg, icon_eyeoff_nova_senha_perfil, icon_eyeon_nova_senha_perfil, icon_red_eyeon_nova_senha_perfil, icon_red_eyeoff_nova_senha_perfil)

    def voltar(e):
        nome_perfil_msg.visible = False
        email_perfil_msg.visible = False
        senha_perfil_msg.visible = False
        nova_senha_perfil_msg.visible = False
        geral_perfil_msg.visible = False
        nome_perfil_msg.value = ""
        email_perfil_msg.value = ""
        senha_perfil_msg.value = ""
        nova_senha_perfil_msg.value = ""
        geral_perfil_msg.value = ""

        from telas.perfil import mostrar_perfil
        mostrar_perfil(page, menu)
        page.update()

    def salvar(e):
        nome = nome_perfil.value.title().strip()
        email = email_perfil.value.lower().strip()
        senha = senha_perfil.value.strip()
        nova_senha = senha_nova_perfil.value.strip()

        sucesso, resultado = UserManager.validar_campos_cadastro(nome, email, senha, None, nova_senha)

        if sucesso:
            nome_perfil_msg.visible = False
            email_perfil_msg.visible = False
            senha_perfil_msg.visible = False
            nova_senha_perfil_msg.visible = False
            geral_perfil_msg.visible = True
            geral_perfil_msg.value = "Atualizando dados..."
            geral_perfil_msg.color = ft.Colors.BLUE_700
            page.update()
            time.sleep(2)
            mostrar_perfil(page, menu)
        else:
            try:
                conn = conectar()
                cursor = conn.cursor()
                cursor.execute("UPDATE usuarios SET nome = ?, email = ?, senha = ? WHERE id = ?", (nome, email, senha, u.id))
                conn.commit()
            except:
                geral_perfil_msg.value = "Erro ao atualizar dados."
                geral_perfil_msg.color = ft.Colors.RED
                geral_perfil_msg.visible = True
                page.update()
            finally:
                conn.close()

            u.nome = nome
            u.email = email
            if nova_senha is not None:
                u.senha = nova_senha
            else:
                u.senha = senha
            geral_perfil_msg.value = resultado
            geral_perfil_msg.color = ft.Colors.BLUE_700
            geral_perfil_msg.visible = True
            page.update()

    dialog_image_preview = ft.Image(src_base64=imagem_base64 if imagem_base64 else None, src="src/assets/profile.svg" if not imagem_base64 else None, width=200, height=200, fit="cover", border_radius=10)
    selected_image_bytes = None
    rotation_angle = 0 

    def rotate_image(e):
        nonlocal selected_image_bytes, rotation_angle
        if selected_image_bytes:
            rotation_angle += 90
            img = Image.open(io.BytesIO(selected_image_bytes)).rotate(rotation_angle, expand=True)
            buf = io.BytesIO()
            img.save(buf, format="JPEG")
            rotated_bytes = buf.getvalue()
            dialog_image_preview.src_base64 = base64.b64encode(rotated_bytes).decode("utf-8")
            selected_image_bytes = rotated_bytes
            page.update()

    def on_file_selected(e: ft.FilePickerResultEvent):
        nonlocal selected_image_bytes, rotation_angle
        if e.files:
            rotation_angle = 0
            file = e.files[0]
            img = Image.open(file.path)
            buf = io.BytesIO()
            img.save(buf, format="JPEG")
            selected_image_bytes = buf.getvalue()
            dialog_image_preview.src_base64 = base64.b64encode(selected_image_bytes).decode("utf-8")
            page.update()

    def save_and_close(e):
        from telas.perfil import mostrar_perfil
        nonlocal selected_image_bytes
        if selected_image_bytes:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("UPDATE usuarios SET imagem_perfil = ? WHERE id = ?", (selected_image_bytes, u.id))
            conn.commit()
            conn.close()
            page.close(dialog)
            mostrar_perfil(page, menu)
            
    file_picker = ft.FilePicker(on_result=on_file_selected)
    page.overlay.append(file_picker)

    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text(
            value="Alterar imagem de perfil", 
            font_family="InstrumentSans Bold", 
            color="#006A71", size=18
        ),
        content=ft.Column(
            [
                ft.Container(
                    content=dialog_image_preview,
                    alignment=ft.alignment.center
                ),
                ft.Row(
                    [
                        TransparentButton(
                            text="Selecionar", 
                            on_click=lambda e: file_picker.pick_files(
                                allowed_extensions=["jpg", "jpeg", "png"], 
                                file_type=ft.FilePickerFileType.IMAGE
                            )
                        ),
                        TransparentButton(
                            text="Rotacionar", 
                            on_click=rotate_image
                        ),
                    ], 
                    alignment="center"
                )
            ], 
            alignment=ft.MainAxisAlignment.CENTER, tight=True
        ),
        actions=[
            TransparentButton(
                text="Cancelar", 
                on_click=lambda e: page.close(dialog)
            ),
            PrimaryButton(
                text="Salvar", width=100, height=35,
                on_click=save_and_close,
            )
        ],
        bgcolor="white", alignment=ft.alignment.center,
        actions_alignment="end"
    )

    page.overlay.append(dialog)

    page.add(
        ft.Container(
            content=TransparentButton(
                content=ft.Row(
                    [
                        icon_back,
                        ft.Text(
                            "Voltar", text_align="center", size=16, 
                            font_family="InstrumentSans Medium", 
                            color="#AEAEAE"
                        )
                    ], 
                    alignment=ft.alignment.center, spacing=5,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                ),
                overlay_color="#EAFBFF", width=100, height=35,
                on_click=voltar
            ),
            padding=ft.padding.only(top=25), alignment=ft.alignment.center_left
        ),
        ft.Column(
            [
                ft.Text("Editar Perfil", size=22, font_family="InstrumentSans Bold", color="#006A71"), 
                ft.Container(
                    content=ft.Stack(
                        [
                            ft.Container(
                                width=170, height=170, border_radius=170,
                                alignment=ft.alignment.center,
                                gradient=ft.LinearGradient(
                                    begin=ft.alignment.top_left, 
                                    end=ft.alignment.bottom_right, 
                                    colors=["#006A71", "#01C6D3"]
                                )
                            ),
                            ft.Image(
                                width=160, height=160,
                                src_base64=imagem_base64 if imagem_base64 else None,
                                src="src/assets/profile.svg" if not imagem_base64 else None,
                                border_radius=160, fit="cover"
                            ),
                            ft.Container(
                                content=icon_edit_photo, offset=ft.Offset(1.4, -1.4),
                                width=40, height=40, border_radius=20,
                                alignment=ft.alignment.center, 
                                on_click=lambda e: page.open(dialog),
                                gradient=ft.LinearGradient(
                                    colors=["#006A71", "#01C6D3"]
                                )
                            )
                        ], 
                        alignment=ft.alignment.center
                    ),
                    alignment=ft.alignment.center, padding=ft.padding.only(top=25, bottom=25)
                ),
                ft.Container(
                    ft.Column(
                        [
                            InputLabel("Nome"),
                            container_nome_perfil,
                            MessageContainer(content=nome_perfil_msg)
                        ], 
                        alignment="center", horizontal_alignment="center", spacing=7
                    )
                ),
                ft.Container(
                    ft.Column(
                        [
                            InputLabel("Email"),
                            container_email_perfil,
                            MessageContainer(content=email_perfil_msg)
                        ], 
                        alignment="center", horizontal_alignment="center", spacing=7
                    )
                ),
                ft.Container(
                    InputLabel(
                        value="Senha", font_family="InstrumentSans SemiBold", 
                        size=20, color="#006A71"
                    ),
                    padding=ft.padding.only(top=20, bottom=20)
                ),
                ft.Container(
                    ft.Column(
                        [
                            InputLabel("Senha Atual"),
                            container_senha_perfil,
                            MessageContainer(content=senha_perfil_msg)
                        ], 
                        alignment="center", horizontal_alignment="center", spacing=7
                    )
                ),
                ft.Container(
                    ft.Column(
                        [
                            InputLabel("Nova Senha"),
                            container_senha_nova_perfil,
                            MessageContainer(content=nova_senha_perfil_msg)
                        ], 
                        alignment="center", horizontal_alignment="center", spacing=7
                    )
                ),
                MessageContainer(content=geral_perfil_msg)
            ],
            alignment=ft.alignment.center, 
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand_loose=True, tight=True, scroll="auto", height=725
        ),
        ft.Container(
            content=PrimaryButton(text="Salvar", on_click=salvar),
            padding=ft.padding.only(bottom=20), alignment=ft.alignment.center
        )
    )
    page.update()

