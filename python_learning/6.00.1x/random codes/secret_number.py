low=0
high=100
guess=(high+low)/2
reply=''
print('Please think of a number between 0 and 100!')
while(reply!='c'):
  print('Is your secret number ' + str(guess) +'?')
  reply=raw_input("Enter 'h' to indicate the guess is too high\
  .Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
  if reply not in 'hlc':
      print('Sorry, I did not understand your input.')
  elif reply=='l':
      low=guess
      guess=(low+high)/2
  elif reply=='h':
      high=guess
      guess=(low+high)/2
print('Game over. Your secret number was: ' +str(guess))      

          
