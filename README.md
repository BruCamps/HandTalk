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

  ![SplashScreen](https://github.com/user-attachments/assets/3cc604b8-0614-4ce3-be10-5fcf54256d35)    ![Home](https://github.com/user-attachments/assets/589141b9-dd81-4ff2-b8a0-43e193831372)


Melhorias Futuras:
---
Melhorar visualmente a tela de Ranking 
Adicionar tela de recuperação da senha
Implementar a lógica para armazenar as conquistas de cada usuário do banco de dados
Adicionar os vídeos de suporte para o quiz 
Usar o FireBase para armazenar os dados
Dividir e organizar o código











