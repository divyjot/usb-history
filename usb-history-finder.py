import subprocess

def yes():
    print("collecting details...........\n\n")
    process=subprocess.Popen(["powershell","Get-ItemProperty -Path 'HKLM:\\SYSTEM\\CurrentControlSet\\Enum\\USBSTOR\\*\\*' | Select FriendlyName,PSChildname"],stdout=subprocess.PIPE,shell=True);
    result=str(process.communicate())
    result=result.replace("\\r","")
    result=result.replace("&0","")
    result=result.replace("(b'","")
    result=result.replace("', None)","")
    result=result.replace("PSChildName","PSChildName(SERIAL NO.)")
    result=result.replace("\\n","\n")
    return result

def no():
    return "\npreparing to exit.......\n"

def start():
    print("""
+-+-+-+ +-+-+-+-+-+-+-+ +-+-+-+-+-+-+
|U|S|B| |H|i|s|t|o|r|y| |F|i|n|d|e|r|
+-+-+-+ +-+-+-+-+-+-+-+ +-+-+-+-+-+-+

USB-History-Finder-1.0


Extract USB information (y/n): 
""")
#arg=input()
def switch(arg):
    if(arg == 'Y' or arg=='y' or arg=='yes'):
        print(yes())
    elif (arg == 'N' or arg=='n' or arg=='no'):
        print(no())
    else:
        print('Invalid')
        exit
start()
switch(input())
