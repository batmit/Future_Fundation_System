def velha_game():
    while True:
        jogadas = 0
        velha = {
            "1": [' ', 1],
            "2": [' ', 2],
            "3": [' ', 3],
            "4": [' ', 4],
            "5": [' ', 5],
            "6": [' ', 6],
            "7": [' ', 7],
            "8": [' ', 8],
            "9": [' ', 9]
        }
        jogador = 18
        print('Digite o número correspondente ao local que você quer jogar')
        while jogadas < 9:
            print("-"*100)
            print(f"""
             1 | 2 | 3                               {velha["1"][0]} | {velha["2"][0]} | {velha["3"][0]}
            ---+---+---                             ---|---|---
             4 | 5 | 6                               {velha["4"][0]} | {velha["5"][0]} | {velha["6"][0]}
            ---+---+---                             ---|---|---
             7 | 8 | 9                               {velha["7"][0]} | {velha["8"][0]} | {velha["9"][0]}
        """)
            if jogador % 2 == 0:
                sinal = "X"
            else:
                sinal = "O"
            jogadanow = input(f"Quem joga é o jogador de {sinal}. Número: ")
            if velha[jogadanow][1] == "X" or velha[jogadanow][1] == "O":
                print("jogada invalida, tente novamente")
                continue # o continue volta para lÃ¡ em cima da repetiÃ§Ã£o, para o while
            else:
                velha[jogadanow][0] = sinal
                velha[jogadanow][1] = sinal
                jogadas += 1
                jogador -= 1
                lele = velha["1"][1] == velha["2"][1] and velha["2"][1] == velha["3"][1]
                dede = velha["1"][1] == velha["5"][1] and velha["5"][1] == velha["9"][1]
                luiz = velha["3"][1] == velha["5"][1] and velha["5"][1] == velha["7"][1]
                hugo = velha["1"][1] == velha["4"][1] and velha["4"][1] == velha["7"][1]
                joao = velha["2"][1] == velha["5"][1] and velha["5"][1] == velha["8"][1]
                bartolomeu = velha["3"][1] == velha["6"][1] and velha["6"][1] == velha["9"][1]
                zaqueu = velha["7"][1] == velha["8"][1] and velha["8"][1] == velha["9"][1]
                estevao = velha["4"][1] == velha["5"][1] and velha["5"][1] == velha["6"][1]
                if lele or dede or luiz or hugo or joao or bartolomeu or zaqueu or estevao:
                    print(f"""
                                          {velha["1"][0]} | {velha["2"][0]} | {velha["3"][0]}
                                         ---|---|---
                                          {velha["4"][0]} | {velha["5"][0]} | {velha["6"][0]}
                                         ---|---|---
                                          {velha["7"][0]} | {velha["8"][0]} | {velha["9"][0]}
                    """)
                    print(f"Parabens, {sinal} venceu")
                    break
        if jogadas == 9:
            print('Empate!')
        again = input("Deseja jogar novamente? ")
        if again[0] == "N" or again[0] == 'n':
            return sinal
            break