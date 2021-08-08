import os
def stealer():
    port = int(input('port>>>'))
    os.system(f'nc -lvp {port}')