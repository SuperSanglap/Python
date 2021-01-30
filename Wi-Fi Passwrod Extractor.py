from colored import fg,attr
import subprocess

data = subprocess.check_output(["netsh","wlan","show","profiles"]).decode('utf-8').split('\n')
wifis = [line.split(':')[1][1:-1] for line in data if "All User Profile" in line]

green = fg('green')
red = fg('red')
yellow = fg('yellow')
blue = fg('blue')

for wifi in wifis:
    results = subprocess.check_output(['netsh','wlan','show','profile',wifi,'key=clear']).decode('utf-8').split('\n')
    results = [line.split(':')[1][1:-1] for line in results if "Key Content" in line]
    try:
        print(f'{yellow}Name: {blue}{wifi}, {yellow}Password: {green}{results[0]}')
    except IndexError:
        print(f'{yellow}Name: {blue}{wifi}, {yellow}Password: {red}Cannot be Read!')