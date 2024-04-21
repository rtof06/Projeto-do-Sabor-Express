import os

restaurantes = []

def exibir_nome_programa():
  print('''
----------------------🇸​​​​​🇦​​​​​🇧​​​​​🇴​​​​​🇷​​​​​ 🇪​​​​​🇽​​​​​🇵​​​​​🇷​​​​​🇪​​​​​🇸​​​​​🇸​​​​----------------------
''')

def exibir_opcoes():
  print('1. Cadastrar Restaurante')
  print('2. Listar Restaurante')
  print('3. Alterar status do Restaurante')
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
  print('Opção inválida\n')
  voltar_menu()

def cadastrar_restaurante():
  subtitulo('--- Cadastro de novos restaurantes ---')
  nome_restaurante = input('Nome do restaurante: ')
  
  #If on the input don't have the word "restaurante", the output will return "the restaurant <name>" automatically.
  #Se no input não tiver a palavra "restaurante", no output retornará como "o restaurante <nome>" automaticamente.
  if nome_restaurante.lower().startswith('restaurante'):
    nome = nome_restaurante.split(' ', 1)[1]
    categoria = input(f'Digite a categoria do restaurante {nome}: ')
    dados_restaurante = {'nome':nome_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_restaurante)
    print(f'\nMuito bem! "{nome_restaurante}" foi cadastrado com sucesso.\n')
  else: 
    nome_simples = 'restaurante ' + nome_restaurante
    categoria = input(f'Digite a categoria do {nome_simples}: ')
    dados_restaurante = {'nome':nome_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_restaurante)
    print(f'\nMuito bem! "{nome_restaurante}" foi cadastrado com sucesso.\n')
  voltar_menu()
  
def listar_restaurante():
  subtitulo('--- Lista de restaurantes cadastrados ---')
  
  if restaurantes == []:
    print('Nenhum restaurante cadastrado!')
    voltar_menu()
  else:
    print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | Status\n')
    for restaurante in restaurantes:
      nomes_restaurante = restaurante['nome']
      categoria = restaurante['categoria']
      ativo = 'ativado' if restaurante['ativo'] else 'desativado'
      print(f'- {nomes_restaurante.ljust(25)} | {categoria.ljust(25)} | {ativo}')
  
  voltar_menu()
  
def ativar_restaurante():
  subtitulo('--- Alterar o estado do restaurante ---\n')
  
  nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
  restaurante_encontrado = False
  
  for restaurante in restaurantes:
    if nome_restaurante == restaurante['nome']:
      restaurante_encontrado = True
      restaurante['ativo'] = not restaurante['ativo']
      print('Alterando...\n')
      mensagem = f' "{nome_restaurante}" foi ativado com sucesso' if restaurante['ativo'] else f' "{nome_restaurante}" foi desativado com sucesso'
      print(mensagem)
  if not restaurante_encontrado:
    print(f'O restaurante "{nome_restaurante}" não foi encontrado.')
      
  voltar_menu()
  
def escolher_opcao():
  try:
    opcao_escolhida = int(input('Escolha uma opção: '))
    print(f'Você escolheu a opção {opcao_escolhida}\n')
    if opcao_escolhida == 1:
      cadastrar_restaurante()
    elif opcao_escolhida == 2:
      listar_restaurante()
    elif opcao_escolhida == 3:
      ativar_restaurante()
    elif opcao_escolhida == 4:
      finalizar_app()
    else:
      opcao_invalida()
  except ValueError:
    opcao_invalida()

def main():
  os.system('cls')
  exibir_nome_programa()
  exibir_opcoes()
  escolher_opcao()

if __name__ == '__main__':
  main()