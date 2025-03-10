import os,platform
os.system('git pull --quiet 2>/dev/null')
os.system("clear")
bit = platform.architecture()[0]
if bit == '64bit':
    import ighunting
elif bit == '32bit':
    print("\033[0m\033[91m Sorry Your Device Is 32bit, This Tool 32bit Not Sported, Only For \033[92m64Bit\033[0m ]");exit() 
 
 
