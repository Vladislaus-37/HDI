# Yes, my code is hard to read, sorry


# Import libs
import os
import subprocess
import platform
import sys
import colorama
import math
import time
colorama.init()

# Read config file
with open("config.conf", 'r', encoding='utf-8') as file:
    configdata = file.readlines()
file.close()

name_alias=[]
com_alias=[]
sys_build='BETA.020126.3'
sys_ver='β10'

def main():
    # Output Header
    print(colorama.Fore.WHITE+colorama.Back.BLACK+' ')
    print('HDI', sys_ver)
    print(colorama.Style.RESET_ALL+'—————————')


    # Main part
    while True:
        cow=input(colorama.Fore.YELLOW+str(os.path.basename(os.getcwd()))+'>'+colorama.Fore.WHITE+' $').strip().split(" ")
        Cow_Herder(cow)

def Cow_Herder(cow_list):
    if cow_list[0]=='index': # Index command
        index()

    elif cow_list[0]=='read': # Read txt file
        read(cow_list[1:])

    elif cow_list[0]=='open': # Open file with default application
        runfile(cow_list[1:])   

    elif cow_list[0]=='chdir' or cow_list[0]=='cd': # Change dir
        chdir(cow_list[1:])

    elif cow_list[0]=='exit': # For haters)
        print('Wait 4 seconds')
        time.sleep(3)
        print('Good bye!')
        time.sleep(1)
        sys.exit()

    elif cow_list[0]=='help': # Help manual
        print(colorama.Fore.CYAN + 'HDI', sys_ver, 'Help Guide')
        print(colorama.Fore.WHITE + 'Commands:')
        print('  index                           - Show directory contents')
        print('  read    [name]                  - Read a text file')
        print('  open    [name]                  - Open a file with default app')
        print('  chdir   [path]                  - Change current directory')
        print('  cdir    [path]                  - Create dir')
        print('  cudir                           - Show current dir')
        print('  exit                            - Exit the program')
        print('  help                            - Show this guide')
        print('  delfile [name]                  - Delete file')
        print('  deldir  [path]                  - Delete empty dir')
        print('  renm    [name] [new_name]       - Rename file or dir')
        print('  copy    [scr]  [dest]           - Copy file')
        print('  about                           - About HDI')
        print('  log     [text]                  - Log text to console')
        print('  fms     [name]                  - Run FMS script')
        print('  py      [type] [name/str]|[str] - Run python file or code')
        print('  alias   [name] [com]|[com]      - Create alias for command or commands group')
        print('  calc    [expr]                  - Calculate mathematical expression,' \
        'also with python operands and functions with math lib')

    elif cow_list[0]=='delfile': # Delete file
        delfile(cow_list[1:])

    elif cow_list[0]=='deldir': # Delete dir
        deldir(cow_list[1:])

    elif cow_list[0]=='renm': # Rename file or dir
        rename(cow_list[1:])

    elif cow_list[0]=='cdir': # Create dir
        cdir(cow_list[1:])

    elif cow_list[0]=='cudir': # Show current dir
        print('Current dir:   ',os.getcwd())

    elif cow_list[0]=='copy': # Copy file
        copy(cow_list[1:])
    
    elif cow_list[0]=='qr': # Emm, here was be a qr code to NOWKIES Telegram post
        print('Ha!')
        print('What you want to see here?')

    elif cow_list[0]=='about' or cow_list[0]=='screenfetch': # About HDI
        print('')
        print('▓▓▓▓▓▓▓▓▓▓▓▓▒')
        print('▓           ▒',)
        print('▓ HDI       ▒')
        print('▓ ────      ▒',colorama.Style.BRIGHT+colorama.Fore.LIGHTWHITE_EX+'       HDI', sys_ver)
        print('▓ $         ▒'+colorama.Style.RESET_ALL+colorama.Fore.WHITE)
        print('▓           ▒')
        print('▒▒▒▒▒▒▒▒▒▒▒▒▒')
        print('')
        print(' HDI it`s a simple open sourse console file manager based on Python3')
        print('')
        print('Developers:')
        print('  Tr37')
        print('  Sairsay')
        print('  AGENT912')
        print('')
        print('Source code: github.com/Vladislaus-37/HDI')
        print('Site       : sites.google.com/view/hdi-fms')
        print('')
        print('Build:   ', sys_build)

    elif cow_list[0]=='log': # Log to console
        print(colorama.Fore.LIGHTBLUE_EX+' '.join(cow_list[1:]).rstrip('\n'), colorama.Fore.WHITE)
    
    elif cow_list[0]=='fms': # Run FMS script
        fms(cow_list[1])

    elif cow_list[0]=='py': # Run python file or strings
        pyexe(cow_list[1:])

    elif cow_list[0]=='alias': # Create Alias
        add_alias(cow_list[1:])

    elif cow_list[0]=='calc': # Calculate mathematical expression
        try:
            result=eval(' '.join(cow_list[1:]))
            print(colorama.Fore.GREEN+str(result))
        except ZeroDivisionError:
            print(colorama.Fore.GREEN+'0')
        except NameError or ModuleNotFoundError:
            print(colorama.Fore.GREEN+'Python function or variable is not found')
        except SyntaxError:
            print(colorama.Fore.GREEN+'Bro, your syntax sucks')
        except Exception as err:
            print(colorama.Fore.GREEN+str(err))

    elif cow_list[0]=='' or cow_list[0]=='\n' or cow_list[0]=='#': # For comment in FMS and white lines
        123

    else: # This SYNTAX else)
        run_alias(cow_list)
    return 0

def index():    # Index command
    try:
        print(' ')
        print('Contents of', os.getcwd()) 
        print('------------------------------------------------------------------')
        print('| Type  | Name            | Size                                 |')
        print('|-------|-----------------|--------------------------------------|')
        for item in os.listdir():
            if os.path.isfile(item):
                print('| File: | ' + item + ' | ' + str(os.path.getsize(item)) + ' bytes |')
            if os.path.isdir(item):
                print('| Dir:  | ' + item + ' | ' + str(os.path.getsize(item)) + ' bytes |')
        print('------------------------------------------------------------------')
    except:
        print(colorama.Fore.LIGHTRED_EX + '    INDEX_ERR')
        print(colorama.Fore.WHITE + '    May be path of dir is invalid')
        print('    Or your system is do not supported')
    return 0

def read(File):     # Read txt file
    try:
        with open(File[0].rstrip('\n'), 'r') as file:
            contenta = file.read()
        print(colorama.Fore.LIGHTBLACK_EX+'------------------')
        print(colorama.Fore.LIGHTBLUE_EX+' ')
        print(contenta)
        print(colorama.Fore.LIGHTBLUE_EX+' ')
        print(colorama.Fore.LIGHTBLACK_EX+'------------------')
        print(colorama.Fore.WHITE+'')
        file.close()
    except:
        print(colorama.Fore.LIGHTRED_EX + '    READ_ERR')
        print(colorama.Fore.WHITE + '    May be name of file is invalid')
        print('    Or your system is do not supported')
    return 0

def runfile(File):       # Run file
    try:
        filepath = os.getcwd() + "/" + File[0].rstrip('\n')
        if platform.system() == 'Darwin':       # for macOS
            subprocess.call(('open', filepath))
        elif platform.system() == 'Windows':    # for Windows
            os.startfile(filepath)
        else:                                   # for Pinguins
            subprocess.call(('xdg-open', filepath))
    except:
        print(colorama.Fore.LIGHTRED_EX + '    OPEN_ERR')
        print(colorama.Fore.WHITE + '    May be name of file is invalid')
        print('    Or your system is do not supported')
    return 0

def chdir(File):        # Change dir
    try:
         os.chdir(File[0].rstrip('\n'))
    except:
        print(colorama.Fore.LIGHTRED_EX + '    CHDIR_ERR')
        print(colorama.Fore.WHITE + '    May be path of dir is invalid')
        print('    Or your system is do not supported')
    return 0

def delfile(File):       # Delete flie
    try:
        os.remove(File[0].rstrip('\n'))
    except:
        print(colorama.Fore.LIGHTRED_EX + '    DEL_FILE_ERR')
        print(colorama.Fore.WHITE + '    May be path of file is invalid')
        print('    Or your system is do not supported')
    return 0

def deldir(File):       # Delete dir
    dirpath=File[0].rstrip('\n')
    try:
        os.rmdir(dirpath)
    except:
        print(colorama.Fore.LIGHTRED_EX + '    DEL_DIR_ERR')
        print(colorama.Fore.WHITE + '    May be name of dir is invalid')
        print('    Or your dir is not empty')
        print('    Or your system is do not supported')
    return 0

def rename(File):
    try:
        os.rename(File[0].rstrip('\n'), File[1].rstrip('\n'))
    except:
        print(colorama.Fore.LIGHTRED_EX + '    RENAME_ERR')
        print(colorama.Fore.WHITE + '    May be path of file is invalid')
        print('    Or your system is do not supported')
    return 0

def cdir(File):     # Create dir
    try:
        os.mkdir(''.join(File[0]).rstrip('\n'))
    except:
        print(colorama.Fore.LIGHTRED_EX + '    CREATE_DIR_ERR')
        print(colorama.Fore.WHITE + '    May be path of new dir is invalid')
        print('    Or your system is do not supported')
    return 0

def copy(File):     # Copy file
    src = File[0].rstrip('\n')
    dest = File[1].rstrip('\n')
    print(src, '->', dest) 
    try:
        if platform.system() == 'Darwin':       # for macOS
            subprocess.call(('cp', src, dest))
        elif platform.system() == 'Windows':    # for Windows
            subprocess.call(('cmd', '/c', 'copy', src, dest))
        else:                                   # for Pinguins
            subprocess.call(('cp', src, dest))
    except:
        print(colorama.Fore.LIGHTRED_EX + '    COPY_ERR')
        print(colorama.Fore.WHITE + '    May be name of file is invalid')
        print('    Or your system is do not supported')
    return 0

# Run fms script
def fms(path):
    try:
        with open(path+'.fms', 'r', encoding='utf-8') as file:
            script = file.readlines()
            file.close()
        for i in script:
            Cow_Herder(i.rstrip('\n').split(' '))
    except:
        print(colorama.Fore.LIGHTRED_EX + '    FSM_ERR')
        print(colorama.Fore.WHITE + '    May be name of script is invalid')
        print('    Or script will be wrong')

# Run py file or execute python strings
def pyexe(pyexe_pe):
    if pyexe_pe[0] == 'file':
        runfile([' '.join((pyexe_pe[1:]))])
    elif pyexe_pe[0] == 'exe':
        code_py=' '.join(pyexe_pe[1:]).split(' | ')
        try:
            for i in code_py:
                exec(i)
        except Exception as err:
            print(colorama.Fore.LIGHTRED_EX + '    PY_ERR')
            print(colorama.Fore.MAGENTA + '    ' + str(err))
            print(colorama.Fore.WHITE + '    Check your code')
    return 0

# Create alias
def add_alias(name_com):
    global name_alias, com_alias
    name_alias.append(name_com[0])
    com_alias.append(str(' '.join(name_com[1:])).split(' | '))
    print("Alias    :", name_alias[-1])
    print("Commands :", com_alias[-1])
    return 0

# Run Alias code
def run_alias(name):
    global name_alias, com_alias
    if name[0] not in name_alias:
        print('')
        print(colorama.Fore.LIGHTRED_EX + '    SYNTAX_ERR')
        print(colorama.Fore.WHITE + '')
    else:
        comands=com_alias[name_alias.index(name[0])]
        for i in comands:
            Cow_Herder(i.split(' '))

# Run Part  
if sys.argv[-1]!=sys.argv[0]:
    if sys.argv[1]=='fms':
        fms(' '.join(sys.argv[2:]))
    else:
        main()
else:
    main()

# by TR37 https://t.me/tr333777
