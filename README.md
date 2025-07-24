<h1>Projeto Handtalk</h1>

**Universidade Federal Rural de Pernambuco** <br>
**Departamento de Estatística e Informática** <br>
**Bacharelado em Sistemas de Informação** <br>
**Disciplina: Projeto Interdisciplinar para Sistemas de Informação** <br>

<h2>⚙️ Funcionalidades:</h2>

° Cadastro de Usuário (CRUD completo) <br>
° Validador de Cadastro/Login <br>
° Menu Interagível <br>
° Quiz de Verificação de Conteúdo <br>
° Sistema de pontuação (XP) <br>
° Gráfico de Desempenho do Usuário <br>
° Banco de dados pelo sqlite3 <br>

<h3>Tecnologias Utilizadas</h3>

**Python 3**<br>

**bibliotecas principais**: <br>
- ``os`` para puxar os dados do arquivo cadastro.env <br>
- ``re``para verificar os campos <br>
- ``random``para gerar código de verificação de e-mail <br>
- ``flet`` para interface gráfica <br>
- ``sqlite3`` para o banco de dados <br>
- ``email.mime`` para construir o corpo do e-mail que será enviado para o usuário <br>
- ``smtplib`` para enviar o e-mail ao usuário <br>
- ``datetime`` registar o dia que o usuário fez o quiz

💾 Como Executar o Projeto 
---
1. Certifique-se de ter o **Python 3** instalado em seu sistema.
2. Salve o projeto em um arquivo Python (ex.: ``handtalk.py``)
3. execute o programa no terminal ou prompt de comando

Estrutura Principal do Projeto
---
```
defs.py   #Arquivo contendo as funções do código.
usuario.txt  #Arquivo contendo os dados de cadastro do usuário inseridos manualmente.
verificar.py #Arquivo contendo as restrições necessárias que verificam possiveis erros de entrada inseridas pelo usuário.
main.py   #Arquivo contendo o ponto de entrada do programa (menu).
```

🖥️ Interfaces
-----------
- Terminal:
  
![interface handtalk](https://github.com/user-attachments/assets/1a32e308-84f5-4b31-a88a-7ab3ef35e04b)


- Interface Gráfica do Usuário (GUI):

  ![WhatsApp Image 2025-07-23 at 21 50 58](https://github.com/user-attachments/assets/95e6286c-8b03-4bc2-a82a-6b95c48a1784)
![WhatsApp Image 2025-07-23 at 21 50 59](https://github.com/user-attachments/assets/c325b7f5-4d06-4e0c-82a0-61eddfd96e42)


Melhorias Futuras:
---
Melhorar visualmente a tela de Ranking <br>
Adicionar tela de recuperação da senha <br>
Implementar a lógica para armazenar as conquistas de cada usuário do banco de dados <br>
Adicionar os vídeos de suporte para o quiz <br>
Usar o FireBase para armazenar os dados <br>
Dividir e organizar o código <br>








