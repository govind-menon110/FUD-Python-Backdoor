# FUD-Python-Backdoor
### Note: The developer does not take responsibility for any actions undertaken by the individual using this application

## <a id="introduction" style="color: rgb(0,0,0)"><u> Introduction</u></a>:
Imagine you're a burglar casing a house for a potential robbery. You see a "Protected by…" security sign staked in the front lawn and Ring doorbell camera. Being the crafty cat burglar that you are, you hop the fence leading to the back of the house. You see there's a backdoor, cross your fingers, and try the knob—it's unlocked. To the casual observer, there are no external signs of a burglary. In fact, there's no reason you couldn't rob this house through the same backdoor again, assuming you don't ransack the place.

Computer backdoors work in much the same way.

In the world of cybersecurity, a backdoor refers to any method by which authorized and unauthorized users are able to get around normal security measures and gain high level user access (aka root access) on a computer system, network, or software application. Once they're in, cybercriminals can use a backdoor to steal personal and financial data, install additional malware, and hijack devices.

Read more here: <a href="https://www.malwarebytes.com/backdoor/"> Malwarebytes Blog </a>

## How to use it?
The files provided in the repo are raw python coded files. The most important one for you is the `data.py` file.

### <a id="preparation" style="color: rgb(0,0,0)"><u> Preparation</u></a>:
Before we use the backdoor, we need the following things:
1. A host that you control having a static IP or a subscription service with a dynamic DNS client. You can also use a tunnelling service such as `ngrok`.
Find the links in the <a href="#references">references</a> section.
2. Now that you have the public IP/dynamic DNS configured, setup the firewall to allow a port that you want the traffic to be received to (on the host you control)
3. Open the `data.py` file and put these values in the respective fields.
Note that there are other data values but you do not need to change them
4. Have a file that you want the victim to open ready - a pdf or a jpg etc. <u> Note the name and full path of the file</u> on the host computer where you will compile this backdoor
5. Input this file name in the double quotes given in `data.py`
6. If you want the keylogger to send you mails periodically, add your email and password in the `data.py`

### <a id="converting" style="color: rgb(0,0,0)"><u>Converting into an Executable</u></a>:
1. We will use the pyinstaller module for this. Make sure you have python3.7 installed on the host system you control

 `pip3 install pyinstaller`
2.
