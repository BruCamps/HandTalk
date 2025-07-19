import smtplib
from db.database import conectar
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import random
import flet as ft
import os
from core.user import User
from dotenv import load_dotenv
from datetime import datetime, timedelta
import asyncio
import time

load_dotenv('cadastro.env')

SENDER_NAME = os.getenv("SENDER_NAME")
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))

codigo_expiracao = {}  # salva expiracao do código
codigo_enviado = {}


def gerar_codigo():
    return str(random.randint(100000, 999999))

def enviar_codigo_email(destinatario, nome, codigo):
    try:
        msg = MIMEMultipart('related')  # 'related' para imagens
        msg['Subject'] = 'Código de Verificação - HandTalk'
        msg['From'] = f'{SENDER_NAME} <{EMAIL_SENDER}>'
        msg['To'] = destinatario

        html = f"""
            <html>
                <body>
                    <img src="cid:banner_image">
                    <p>Olá, <b>{nome}</b>! Seja bem-vindo(a) ao <b>HandTalk</b> 👋<br>
                    Seu código de verificação é: <b>{codigo}</b><br><br>
                    Este código é válido por 5 minutos.</>
                </body>
            </html>
        """

        # Corpo alternativo (HTML)
        msg_alternative = MIMEMultipart('alternative')
        msg.attach(msg_alternative)

        msg_html = MIMEText(html, 'html')
        msg_alternative.attach(msg_html)

        # Adiciona a imagem com Content-ID correto
        with open('src/assets/HandTalk-Banner.png', 'rb') as image_file:
            msg_image = MIMEImage(image_file.read(), 'png')
            msg_image.add_header('Content-ID', '<banner_image>')  # com <>
            msg_image.add_header('Content-Disposition', 'inline', filename='HandTalk-Banner.png')
            msg.attach(msg_image)


        # Envio do e-mail
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, destinatario, msg.as_string())

        return True
    except Exception as e:
        print(f"Erro ao enviar email: {e}")
        return False


def mostrar_codigo_verificacao_email(page: ft.Page, email=None, nome=None, senha=None):
    page.theme = ft.Theme(font_family="InstrumentSans")
    mensagem = ft.Text("", color=ft.Colors.RED, visible=False)

    reenviar_segundos_restantes = 0
    reenviar_label = ft.Text("Não recebi meu código", size=16, color="#898989", font_family="InstrumentSans SemiBold")
    reenviar_botao = ft.TextButton(content=reenviar_label, on_click=None)

    campo_codigo = ft.TextField(
        max_length=6,
        text_style={"color": "#006A71", "font_family": "InstrumentSans Medium", "size": 16},
        hint_style={"color": "#5DA6AB", "font_family": "InstrumentSans Medium", "size": 16},
        hint_text="Cole ou digite seu código aqui",
        bgcolor="#E7F9FD",
        border="none",
        text_align=ft.TextAlign.CENTER,
        keyboard_type=ft.KeyboardType.NUMBER
    )
    container_codigo = ft.Container(
        content=campo_codigo, bgcolor="#E7F9FD", border_radius=15,
        alignment=ft.alignment.center,
        padding=ft.padding.only(top=5, bottom=5),
        width=330
    )

    from telas.login import mostrar_login

    def enviar_codigo(e=None):
        destinatario = email
        if not destinatario:
            mensagem.value = "Digite um email válido para receber o código."
            mensagem.color = ft.Colors.RED
        else:
            codigo = gerar_codigo()
            sucesso = enviar_codigo_email(destinatario, nome, codigo)
            if sucesso:
                codigo_enviado[destinatario] = codigo
                codigo_expiracao[destinatario] = datetime.now() + timedelta(minutes=5)
            else:
                mensagem.value = "Erro ao enviar o código. Verifique seu email."
                mensagem.color = ft.Colors.RED
        page.run_task(iniciar_contagem_regressiva)
        page.update()

    import core.menu as menu
    def verificar(e):
        destinatario = email
        codigo_digitado = campo_codigo.value.strip()

        from db.database import conectar
        from core.user_manager import UserManager

        if not codigo_digitado.isdigit() or len(codigo_digitado) != 6:
            mensagem.value = "Código inválido. Deve conter 6 dígitos."
            mensagem.color = ft.Colors.RED
            page.update()
            return

        if destinatario not in codigo_expiracao or datetime.now() > codigo_expiracao[destinatario]:
            mensagem.value = "Código expirado. Solicite um novo."
            mensagem.color = ft.Colors.RED
            page.update()
            return


        if codigo_enviado.get(destinatario) == codigo_digitado:
            sucesso, retorno = UserManager.cadastrar(nome, email, senha)
            
            if not sucesso:
                mensagem.value = f"Erro ao cadastrar: {retorno}"
                mensagem.color = ft.Colors.RED
                page.update()
                return

            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("SELECT id, nome, email, senha_hash, xp FROM usuarios WHERE email = ?", (destinatario,))
            user_data = cursor.fetchone()
            cursor.execute("UPDATE usuarios SET verificado = 1 WHERE email = ?", (destinatario,))
            conn.commit()
            conn.close()

            from core.state import estado
            from core.user import User
            from telas.trilhas import mostrar_trilhas

            estado.usuario_logado = User(*user_data)
            mensagem.visible = True
            mensagem.value = "Verificado com sucesso! Redirecionando..."
            mensagem.color = ft.Colors.GREEN
            time.sleep(2)
            mostrar_trilhas(page, menu)
        else:
            mensagem.value = "Código incorreto. Tente novamente."
            mensagem.color = ft.Colors.RED
        page.update()

    def reenviar(e):
        destinatario = email
        if destinatario:
            enviar_codigo()
        else:
            mensagem.value = "Erro ao reenviar o código."
            mensagem.color = ft.Colors.RED
        page.update()

    async def iniciar_contagem_regressiva():
        reenviar_botao.on_click = None  # desativa o botão
        for i in range(40, 0, -1):
            reenviar_label.value = f"Não recebi meu código ({i}s)"
            page.update()
            await asyncio.sleep(1)
        reenviar_label.value = "Reenviar Código"
        reenviar_label.color = "#006A71"
        reenviar_botao.on_click = reenviar
        page.update()

    page.controls.clear()
    page.add(
        ft.Container(
            content=ft.Column([
                    ft.Container(
                        content=ft.Text("Verifique seu Email", color="#006A71", size=32, text_align="center", font_family="InstrumentSans SemiBold"),
                        padding=ft.padding.only(top=50),
                        width=340,
                        alignment=ft.alignment.center
                    ),
                    ft.Container(
                        content=ft.Text(
                            spans=[
                                ft.TextSpan(
                                    "Enviamos um email com um código para ",
                                    style=ft.TextStyle(color="#898989", font_family="InstrumentSans Medium", size=16),
                                ),
                                ft.TextSpan(
                                    email,
                                    style=ft.TextStyle(color="#049FA9", font_family="InstrumentSans SemiBold", size=16),
                                ),
                            ],
                            selectable=True,
                            text_align="center",
                        ),
                        alignment=ft.alignment.center,
                        padding=ft.padding.only(top=5, bottom=10),
                        width=340,
                    ),
                    container_codigo,
                    ft.Container(
                        content=ft.ElevatedButton(
                            "Verificar", 
                            width=330,
                            height=40,
                            style=ft.ButtonStyle(
                                bgcolor="#01C6D3", color="white", shape=ft.RoundedRectangleBorder(radius=10), 
                                shadow_color="transparent", overlay_color="#0ED2E0",
                                text_style=ft.TextStyle(font_family="InstrumentSans Medium", size=20, color="white")
                            ), on_click=verificar),
                        padding=ft.padding.only(top=40)
                    ),
                    reenviar_botao,
                    mensagem
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            width=340,
            alignment=ft.alignment.center
        )
    )

    if email:
        enviar_codigo()