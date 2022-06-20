import random
print('para jogar você deve escrever a jogada EX: pedra')
modo = int(input('selecione seu modo de jogo, JogadorxMáquina(1), JogadorxJogador(2), MáquinaxMáquina(3)'))
jogadas = ['pedra','papel','tesoura']
if modo == 1:
    while True:
        comandoJogador= (str(input('digite 0 para parar ou digite uma jogada')))
        correcao = comandoJogador.strip()
        if correcao != '0':
            maquina = random.choice(jogadas)
            if maquina == 'pedra':
                if correcao == 'pedra':
                    print('_-'*11)
                    print('a máquina jogou',maquina)
                    print('-'*6)
                    print('empate')
                    print('_-'*11)
                elif correcao == 'tesoura':
                    print('_-'*11)
                    print('a máquina jogou',maquina)
                    print('-'*6)
                    print('você perdeu')
                    print('_-'*11)
                elif correcao == 'papel':
                    print('_-'*11)
                    print('a máquina jogou',maquina)
                    print('-'*6)
                    print('você ganhou')
                    print('_-'*11)
            if maquina == 'papel':
                if correcao == 'pedra':
                    print('_-'*11)
                    print('a máquina jogou',maquina)
                    print('-'*6)
                    print('você perdeu')
                    print('_-'*11)
                elif correcao == 'tesoura':
                    print('_-'*11)
                    print('a máquina jogou',maquina)
                    print('-'*6)
                    print('você ganhou')
                    print('_-'*11)
                elif correcao == 'papel':
                    print('_-'*11)
                    print('a máquina jogou',maquina)
                    print('-'*6)
                    print('empate')
                    print('_-'*11)
            if maquina == 'tesoura':
                if correcao == 'pedra':
                    print('_-'*11)
                    print('a máquina jogou',maquina)
                    print('-'*6)
                    print('você ganhou')
                    print('_-'*11)
                elif correcao == 'tesoura':
                    print('_-'*11)
                    print('a máquina jogou',maquina)
                    print('-'*6)
                    print('empate')
                    print('_-'*11)
                elif correcao == 'papel':
                    print('_-'*11)
                    print('a máquina jogou',maquina)
                    print('-'*6)
                    print('você perdeu')
                    print('_-'*11)
        else:
            break

if modo == 2:
    while True:
        comandoJogador1 = str(input('Jogador 1 -- digite 0 para parar ou digite uma jogada (os dois jogadores precisam digitar para parar'))
        comandoJogador2 = str(input('Jogador 2 -- digite 0 para parar ou digite uma jogada (os dois jogadores precisam digitar para parar'))
        correcao1 = comandoJogador1.strip()
        correcao2 = comandoJogador2.strip()
        if correcao1 == 'pedra':
            if correcao2 == 'pedra':
                print('_-'*11)
                print('jogador 1 --- {}\nJogador 2 --- {}'.format(comandoJogador1,comandoJogador2))
                print('empate')
                print('_-'*11)
            elif correcao2 == 'tesoura':
                print('_-'*11)
                print('jogador 1 --- {}\nJogador 2 --- {}'.format(comandoJogador1,comandoJogador2))
                print('Jogador 1 venceu')
                print('_-'*11)
            elif correcao2 == 'papel':
                print('_-'*11)
                print('jogador 1 --- {}\nJogador 2 --- {}'.format(comandoJogador1,comandoJogador2))
                print('Jogador 2 venceu')
                print('_-'*11)
            if correcao1 == 'papel':
                if correcao2 == 'papel':
                    print('_-'*11)
                    print('jogador 1 --- {}\nJogador 2 --- {}'.format(comandoJogador1,comandoJogador2))
                    print('empate')
                    print('_-'*11)
                elif correcao2 == 'pedra':
                    print('_-'*11)
                    print('jogador 1 --- {}\nJogador 2 --- {}'.format(comandoJogador1,comandoJogador2))
                    print('jogador 1 venceu')
                    print('_-'*11)
                elif correcao2 == 'tesoura':
                    print('_-'*11)
                    print('jogador 1 --- {}\nJogador 2 --- {}'.format(comandoJogador1,comandoJogador2))
                    print('Jogador 1 venceu')
                    print('_-'*11)
            if correcao1 == 'tesoura':
                if correcao2 == 'pedra':
                    print('_-'*11)
                    print('jogador 1 --- {}\nJogador 2 --- {}'.format(comandoJogador1,comandoJogador2))
                    print('jogador 2 venceu')
                    print('_-'*11)
                elif correcao2 == 'tesoura':
                    print('_-'*11)
                    print('jogador 1 --- {}\nJogador 2 --- {}'.format(comandoJogador1,comandoJogador2))
                    print('empate')
                    print('_-'*11)
                elif correcao2 == 'papel':
                    print('_-'*11)
                    print('jogador 1 --- {}\nJogador 2 --- {}'.format(comandoJogador1,comandoJogador2))
                    print('jogador 1 venceu')
                    print('_-'*11)
        if correcao1 == '0' and correcao2 =='0':
            break

if modo == 3:
    while True:
        maquina1 = random.choice(jogadas)
        maquina2 = random.choice(jogadas)
        corremaq1 = maquina1.strip()
        corremaq2 = maquina2.strip()
        continuar = int(input('1 para continuar e 0 para parar'))
        if continuar == 1:
            if corremaq1 == 'pedra':
                if corremaq2 == 'pedra':
                    print('_-'*11)
                    print('máquina 1 --- {}\nmáquina 2 --- {}'.format(corremaq1,corremaq2))
                    print('empate')
                elif corremaq2 == 'tesoura':
                        print('_-'*11)
                        print('jogador 1 --- {}\nJogador 2 --- {}'.format(corremaq1,corremaq2))
                        print('máquina 1 venceu')
                elif corremaq2 == 'papel':
                        print('_-'*11)
                        print('jogador 1 --- {}\nJogador 2 --- {}'.format(corremaq1,corremaq2))
                        print('máquina 2 venceu')
            if corremaq1 == 'papel':
                    if corremaq2 == 'papel':
                        print('_-'*11)
                        print('máquina 1 --- {}\nmáquina 2 --- {}'.format(corremaq1,corremaq2))
                        print('empate')
                    elif corremaq2 == 'pedra':
                        print('_-'*11)
                        print('máquina 1 --- {}\nmáquina 2 --- {}'.format(corremaq1,corremaq2))
                        print('máquina 1 venceu')
                    elif corremaq2 == 'tesoura':
                        print('_-'*11)
                        print('máquina 1 --- {}\nmáquina 2 --- {}'.format(corremaq1,corremaq2))
                        print('máquina 2 venceu')
            if corremaq1 == 'tesoura':
                    if corremaq2 == 'pedra':
                        print('_-'*11)
                        print('máquina 1 --- {}\nmáquina 2 --- {}'.format(corremaq1,corremaq2))
                        print('máquina 2 venceu')
                    elif corremaq2 == 'tesoura':
                        print('_-'*11)
                        print('máquina 1 --- {}\nmáquina 2 --- {}'.format(corremaq1,corremaq2))
                        print('empate')
                    elif corremaq2 == 'papel':
                        print('_-'*11)
                        print('máquina 1 --- {}\nmáquina 2 --- {}'.format(corremaq1,corremaq2))
                        print('máquina 1 venceu')
        if continuar == 0:
            break