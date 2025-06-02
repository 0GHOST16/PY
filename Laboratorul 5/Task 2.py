for char in 'PYTHON STRING':
  if char == ' ':
      break
  print(char, end='')
  if char == 'O':
      continue
  print('*', end='')

''' Programul parcurge sirul de caractere si daca litera curenta este un spatiu gol iese din ciclu, daca caracterul este 'O', acesta este afisat, dar nu se afisa * dupa el '''
