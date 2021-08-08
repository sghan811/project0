import os
def stealer():
    port = int(input('port>>>'))
    os.system('nc -lvp '+port)