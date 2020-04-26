import win32gui as w
import win32console


class Hide:
    def window(self):
        topbar = win32console.GetConsoleWindow()
        w.ShowWindow(topbar, 20)
        return True


class Title:
    def title(self):
        current = w.GetWindowText(w.GetForegroundWindow())
        return str(current)
