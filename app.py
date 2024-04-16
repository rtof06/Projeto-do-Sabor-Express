import os

restaurantes = []

def exibir_nome_programa():
  print('''
🇸​​​​​🇦​​​​​🇧​​​​​🇴​​​​​🇷​​​​​ 🇪​​​​​🇽​​​​​🇵​​​​​🇷​​​​​🇪​​​​​🇸​​​​​🇸​​​​​
''')

def exibir_opcoes():
  print('1. Cadastrar Restaurante')
  print('2. Listar Restaurante')
  print('3. Ativar Restaurante')
  print('4. Sair do app\n')

def subtitulo(texto):
  os.system('cls')
  print(texto)
  print()

def finalizar_app():
  subtitulo('Finalizando app...')
  os.system('exit')

def voltar_menu():
  #You will come back to the main just if you press Enter.
  #Você voltará ao menu apenas se apertar a tecla Enter.
  while True:
    voltar_menu = input('\nAperte ENTER para voltar ao menu principal ')
    
    if voltar_menu == '':
      break
    else:
      opcao_invalida()
  main() 

def opcao_invalida():
  #You will come back to the main just if you press Enter.
  #Você voltará ao menu apenas se apertar a tecla Enter.
  os.system('cls')
  while True:
    print('Opção inválida\n')
    voltar_menu()

def cadastrar_restaurante():
  subtitulo('Cadastro de novos restaurantes')
  nome_restaurante = input('Nome do restaurante: ')
  
  #If on the input don't have the word "restaurante", the output will return "the restaurant <name>" automatically.
  #Se no input não tiver a palavra "restaurante", no output retornará como "o restaurante <nome>" automaticamente.
  if nome_restaurante.lower().startswith('restaurante'):
    restaurantes.append(nome_restaurante)
    nome = nome_restaurante.split(' ', 1)[1]
    print(f'O restaurante {nome} foi cadastrado!\n')
  else: 
    nome_simples = 'restaurante ' + nome_restaurante
    restaurantes.append(nome_restaurante)
    print(f'O {nome_simples} foi cadastrado!\n')

  voltar_menu()
  
def listar_restaurante():
  subtitulo('Lista de restaurantes cadastrados')
  
  for restaurante in restaurantes:
    print(f'. {restaurante}')
  
  voltar_menu()
  
def escolher_opcao():
  try:
    opcao_escolhida = int(input('Escolha uma opção: '))
    print(f'Voçê escolheu a opção {opcao_escolhida}\n')

    if opcao_escolhida == 1:
      cadastrar_restaurante()
    elif opcao_escolhida == 2:
      listar_restaurante()
    elif opcao_escolhida == 3:
      input('Ativar restaurante: ')
    elif opcao_escolhida == 4:
      finalizar_app()
    else:
      opcao_invalida()
  except:
    opcao_invalida()

def main():
  os.system('cls')
  exibir_nome_programa()
  exibir_opcoes()
  escolher_opcao()

if __name__ == '__main__':
  main()