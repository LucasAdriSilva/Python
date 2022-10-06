import os
import win32com.client as a

try:
    # os.mkdir('wee')
    print(os.cpu_count())
    print(os.getlogin())

    a.Moniker

except Exception as e:
    print(e)
    