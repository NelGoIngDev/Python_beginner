user_option = input('piedra, papel o tijera => ')
user_option = user_option.lower()
computer_option = 'papel'

if user_option == computer_option:
  print('Empate!')
elif user_option == 'piedra':
  if computer_option == 'tijera':
    print('Piedra gana a tijera')
    print('User ganó!')
  else:
    print('Papel gana a piedra')
    print('Computer ganó!')
elif user_option ==  'papel':
  if computer_option == 'piedra':
    print('Papel gana a piedra')
    print('User ganó!')
  else:
    print('Tijera gana a papel')
    print('Computer ganó!')
elif user_option == 'tijera':
  if computer_option == 'papel':
    print('Tijera gana a papel')
    print('User ganó!')
  else:
    print('Piedra gana a tijera')
    print('Computer ganó')