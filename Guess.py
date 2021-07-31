from random import randrange
random_number = randrange(10)
while True:
    guess = int(input('guess a number : '))
    if guess == random_number:
        print ('You Won! ')
        break
    print ('guess higher values' if ( guess < random_number) else 'guess lower values')
    
