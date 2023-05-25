import random
option = ('piedra', 'papel', 'tijera')

# Para que el juego copntinue despues de finalizar la ronda.
keep_playing = True

while keep_playing:
# Variables para contar victorias de cada jugador.
  user_wins = 0
  computer_wins = 0

  while user_wins < 3 and computer_wins < 3:
    
    user_option = input('Por favor escriba una opción entre piedra, papel o tijera => ')
    user_option = user_option.lower()
    if not user_option in option:
      print('No está dentro de las opciones, por favor vuelva a escribir')
      continue
    computer_option = random.choice(option)

    print('Usuario eligió => ', user_option)
    print('Consola eligió =>', computer_option)

    if user_option == computer_option:
      print(f'Empate!, Usuario: {user_wins}, Consola: {computer_wins}')

    elif user_option == 'piedra':
      if computer_option == 'tijera':
        print('Piedra gana a tijera')
        # Incrementa las victorias del User
        user_wins += 1
        print(f'Usuario ganó!, Usuario: {user_wins}, Consola: {computer_wins}')
      else:
        print('Papel gana a piedra')
        # Incrementa las victorias del Computer
        computer_wins += 1
        print(f'Consola ganó!, Usuario: {user_wins}, Consola: {computer_wins}')
        
    elif user_option ==  'papel':
      if computer_option == 'piedra':
        print('Papel gana a piedra')
        user_wins += 1  
        print(f'Usuario ganó!, Usuario: {user_wins}, Consola: {computer_wins}')
      else:
        print('Tijera gana a papel')
        computer_wins += 1
        print(f'Consola ganó!, Usuario: {user_wins}, Consola: {computer_wins}')
    
    elif user_option == 'tijera':
      if computer_option == 'papel':
        print('Tijera gana a papel')
        user_wins += 1
        print(f'Usuario ganó!, Usuario: {user_wins}, Consola: {computer_wins}')
      else:
        print('Piedra gana a tijera')
        computer_wins += 1
        print(f'¡Consola ganó!, Usuario: {user_wins}, Consola: {computer_wins}')

  if user_wins > computer_wins:
    print(f'¡El Usuario ganó la ronda! Marcador final Usuario: {user_wins} Consola: {computer_wins}')
  else:
    print(f'¡La consola ganó la ronda! Marcador final Usuario: {user_wins} Consola: {computer_wins}')

  play_again = input('¿Quiere seguir jugando?, por favor responda (si/no) => ')
  if play_again.lower() != "si":
    keep_playing = False