import time, pyautogui as pg

text = str(input('\nMessage : '))
number = int(input('Number of Messages : '))

print("Press Enter to Start the Attack !")
input()

print('\tAttack Will Start in 15 Secoends, Click on the Target Input Box and Relax !')
time.sleep(15)

for i in range(number):
    pg.typewrite(f'{text}\n')
    time.sleep(0.0001)

print(f'\n\n\tDone ! "{number}" "{text}" Mesages Sent Successfully !!')