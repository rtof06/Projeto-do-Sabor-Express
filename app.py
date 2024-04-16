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

def finalizar_app():
  os.system('cls')
  print('Finalizando app\n')

def voltar_menu():
  while True:
    voltar_menu = input('\nAperte ENTER para voltar ao menu principal ')
    
    if voltar_menu == '':
      break
  main() 

def opcao_invalida():
  while True:
    os.system('cls')
    print('Opção inválida\n')
    voltar_menu = input('Aperte ENTER para voltar ao menu principal ')
    
    if voltar_menu == '':
      break
  main()  

def cadastrar_restaurante():
  print('Cadastro dos restaurantes\n')
  nome_restaurante = input('Nome do restaurante: ')
  
  if nome_restaurante.lower().startswith('restaurante'):
    restaurantes.append(nome_restaurante)
    nome = nome_restaurante.split(' ', 1)[1]
    print(f'O "Restaurante {nome}" foi cadastrado!\n')
  else: 
    nome_simples = 'Restaurante ' + nome_restaurante
    restaurantes.append(nome_simples)
    print(f'O "{nome_simples}" foi cadastrado!\n')

  while True:
    voltar_menu = input('Aperte ENTER para voltar ao menu principal ')
    
    if voltar_menu == '':
      break
  main()
  
def listar_restaurante():
  os.system('cls')
  print('Lista de todos os restuarantes cadastrados:')
  
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