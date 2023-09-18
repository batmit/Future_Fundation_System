import os
from datetime import date
from time import sleep
import time
import emoji
import requests
from bs4 import BeautifulSoup as bs
from apps import Notepad
from apps import calculadora
from apps import navegador
from games import jogo_da_velha
import pygame
from tkinter import *
#import sys
ask = 0
import random # random.sample escolhe um dos valores de uma lista
root = Tk()
with open("documento.txt", "r") as arquivo:
    global dados
    global acessos
    dados = arquivo.readlines()
    acessos = dados[2]
    print(acessos)
if acessos != '1':
    print("\033[1;32;40m Bem Vindo, esse é o Py_Operational_System, um sistema operacional totalmente desenvolvido em python.")
    print(emoji.emojize(" Esse projeto foi desenvolvido pela future fundation :thumbs_up: :snake: :smile: ", use_aliases=True))
    print("Antes de tudo lembre-se: com grandes poderes vem grandes responsabilidades.")
    sleep(1)
    usuário = str(input("Qual é o nome do seu usuário: "))
    senha = int(input("Qual vai ser a sua senha numérica: "))
    with open("documento.txt", "w") as arquivo:
        arquivo.write(f"""{usuário}
{senha}
1""")
else:
    usuário = dados[0]
    senha = int(dados[1])
    print(f"Bem Vindo de volta, {usuário}")
    ask = int(input("Qual a sua senha: "))


criação = '31/08/2021'
sleep(3)
while True:
    if ask != int(senha) and ask != 0:
        break
    data_atual = (f'{date.today().day}/{date.today().month}/{date.today().year}')
    agora = time.time()

    try:
        comando = str(input("Digite o comando(help para ajuda): ")).lower()
    except ValueError:
        print("Você deve digitar uma string")
        continue
    try:
        if comando == 'exit':
            break
        if comando == 'help':
            print("""Comandos possíveis: 
                games
                exit
                data
                notepad
                navegador
                relatar problema
                valor do bitcoin
                calculadora
                musicas
                star wars
                sortear
                criar txt
                ver txt
                criar html
                criar pasta
                ver conteúdo de uma pasta""")
            continue
        elif comando == 'games':
            jogo_selecionado = str(input("""Jogos disponíveis:
                jogo da velha
                : """)).lower()
            if jogo_selecionado == 'jogo da velha':
                jogo_da_velha.velha_game()
        elif comando == 'data':
            print(data_atual)
            print(time.ctime(agora))
        elif comando == 'notepad':
            print("Recomendamos salvar os dados na pasta files")
            Notepad.Notepad_start()
        elif comando == 'navegador':
            navegador.navegador_start()
        elif comando == 'relatar problema':
            print("e-mail: futurefundationbr@gmail.com")
            print("Qualquer crítica é muito bem vinda")
        elif comando == 'preço do bitcoin':
            url = 'https://www.bitcoinprice.com/'
            r = requests.get(url)
            soup = bs(r.content, "html.parser")
            price = soup.find("span", {"id": "price"})
            print("Bitcoin: ", price.text)  # print only the text
        elif comando == 'calculadora':
            calculadora.start_calculadora()
        elif comando == 'musicas':
            selecionada = str(input("""Músicas Disponíveis: 
                praise to the lord the almigthy
                just as i am
                    """)).lower()
            if 'praise to the lord' in selecionada:
                pygame.init()
                pygame.mixer.music.load('music/2001-01-0720-praise-to-the-lord-the-almighty-instrumental-192k-eng.mp3')
                pygame.mixer.music.play(0)
            if selecionada == 'just as i am':
                pygame.init()
                pygame.mixer.music.load('music/JustAsIAm.mp3')
                pygame.mixer.music.play(0)
        elif comando == "star wars":
            print("#Staréamelhorsaga")
            print("Que a força esteja com você, sempre!")
            imagem = PhotoImage(file="files/images/darth_Vader.png")

            lb = Label(root, image=imagem)

            lb.place(x=0, y=20)

            root.mainloop()
        elif comando == 'sortear':
            quantidade = int(input("Quantos valores você quer usar para o sortéio, o computador sorteará um deles: "))
            tipo = str(input("Digite se você quer sortear números(num) ou letras(letr): ")).lower()
            valores = []
            if tipo == 'letr':
                for c in quantidade:
                    valor = str(input("Digite a string: "))
                    valores.append(valor)
            else:
                for c in quantidade:
                    valor = int(input("Digite o número: "))
                    valores.append(valor)
            value = random.sample(valores)
            print(f"Valor sorteado: {value}")
        elif comando == "criar txt":
            nome = str(input("Digite o nome do arquivo, lembrando de colocar .txt no final: "))
            conteudo = str(input("Digite o conteúdo do documento: "))
            with open(f"./files/{nome}", "w") as arquivo:
                arquivo.write(conteudo)
            print("O arquivo só é salvo quando você encerra o programa, ele vai estar salvo na pasta files")
            break
        elif comando == "criar html":
            nome = str(input("Digite o nome do arquivo, lembrando de colocar .html no final: "))
            conteudo = str(input("Digite o conteúdo do html: "))
            título = str(input("Digite o título: "))
            with open(f"./files/{nome}", "w") as arquivo:
                arquivo.write(f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>{título}</title>
</head>
<body>
  {conteudo}
</body>
</html>""")
            print("O arquivo só é salvo quando você encerra o programa, ele vai estar salvo na pasta files")
        elif comando == 'ver txt':
            nome = str(input("Digite o nome do arquivo, lembrando de falar onde o arquivo está. exemplo: (./files/nome), o ./ representa a pasta atual: "))
            with open(f"{nome}", "r") as arquivo:
                print(arquivo.readlines())
        elif comando == "criar pasta":
            nome = str(input("Digite o nome da pasta: "))
            local = str(input("Digite o local que vai colocar a pasta, lembra de colocar . antes: "))
            os.chdir(f"{local}")
            os.mkdir(f"{nome}")
            print("Se não ficar salvo termine o programa.")
        elif comando == "ver conteúdo de uma pasta":
            local = str(input("Digite o local da pasta, lembrando de colocar ./ : "))
            print(os.listdir(f"{local}"))
        else:
            print("Confira o que você escreveu, ou digite help para ver os comandos possíveis")
            sleep(1)
    except Exception as e:
        print("Seu programa não funcionou porque: ", e)
print(emoji.emojize('Adeus! :broken_heart:'))
print("Remember: God is always faithful, God Bless you!")
