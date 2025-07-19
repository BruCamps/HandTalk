import flet as ft
from src.components.entradas import *
from src.components.utils.funcoes import *
from telas.verificacao_codigo import gerar_codigo
from src.components.mensagens import *
from db.database import conectar


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
                    <p>Olá, <b>{nome}</b>! 👋<br>
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

def mostrar_recuperar_senha(page: ft.Page):
    page.controls.clear()

    def verificar_email_db(email: str):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
        usuario = cursor.fetchone()
        conn.close()
        return usuario

    def nome_usuario_db(email: str):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT nome FROM usuarios WHERE email = ?", (email,))
        nome = cursor.fetchone()
        conn.close()
        return nome
    
    def enviar_codigo_email(email: str):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("UPDATE usuarios SET codigo_verificacao = ? WHERE email = ?", (gerar_codigo(), email))
        conn.commit()
        conn.close()
        return True

    def enviar_codigo(e=None):
        destinatario = email_recuperacao.value

        if not destinatario:
            mensagem.value = "Digite um email válido para receber o código."
            mensagem.color = ft.Colors.RED
        elif verificar_email_db(destinatario) is None:
            mensagem.value = "Email não cadastrado."
            mensagem.color = ft.Colors.RED
        else:
            codigo = gerar_codigo()
            nome = nome_usuario_db(destinatario)
            sucesso = enviar_codigo_email(destinatario, nome, codigo)
            if sucesso:
                codigo_enviado[destinatario] = codigo
                codigo_expiracao[destinatario] = datetime.now() + timedelta(minutes=5)
            else:
                mensagem.value = "Erro ao enviar o código. Verifique seu email."
                mensagem.color = ft.Colors.RED
        page.update()

    page.add(
        ft.Container(
            ft.Column([
                ft.Text("Email", text_align="left", size=18, font_family="InstrumentSans Medium", color="#636262", width=343),
                container_recuperacao_email,
                rec_email_msg
            ], 
            alignment="top", horizontal_alignment="center", spacing=10)
        )
    )

