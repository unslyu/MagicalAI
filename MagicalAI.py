import time

print('Welcome to the Magical AI that remembers your happiness!')

time.sleep(2.5)

Option = input('What do you want to do today? 1: Rate you happy you are. or 2: Remember how happy you were.')
if Option=="1":
    y = input('Rate your happiness out of 1 through 10!')
    with open ('MagicalAIoutput.txt', 'w') as Magic:
        Magic.write(y)
        if y <= '5':
            print('Sorry to hear that! This will make your day better: https://www.youtube.com/watch?v=dQw4w9WgXcQ. Thank you for your answer.')
        else:
            time.sleep(0.5)
            print('Thats great! Thank you for your answer.')
elif Option=="2":
    with open ('MagicalAIoutput.txt', 'r') as Magic:
        x = Magic.read()
    print('Last time you were here, You rated your happiness a', x)
    time.sleep(0.5)
else:
    print('Sorry, that was in invaild command.')


