import os
import sys
import platform
import subprocess

print('Do you want to install HDI 1.0? [Y/N]')
accept = input().strip()
if accept.lower() != 'y':
    print('Installation cancelled.')
    sys.exit()
myhdipath=os.getcwd()
username = input('What is your system username? ').strip()
if not username:
    print('Username cannot be empty.')
    sys.exit()

current_dir = os.getcwd()
setup_dir = None

# Определение ОС и создание директории
if platform.system() == 'Windows':
    os.mkdir('C:/HDI')
    os.chdir('C:/HDI')
    setup_dir=('C:/HDI')
elif platform.system() == 'Darwin':
    print('HDI 1.0 is not supported on macOS yet.')
    sys.exit()
else:  # Linux
    setup_dir = f'/home/{username}/HDI'
    try:
        if not os.path.exists(setup_dir):
            os.makedirs(setup_dir)
        os.chdir(setup_dir)
    except Exception as e:
        print(f'Error creating directory {setup_dir}: {e}')
        sys.exit()

print(f'Setup directory created: {setup_dir}')

# Копирование основного файла
src_file = os.path.join(current_dir, 'mfiles', 'setupcode.txt')
dest_file = os.path.join(setup_dir, 'HDI.py')

try:
    if platform.system() == 'Windows':
        subprocess.call(('cmd', '/c', 'copy', (myhdipath+'\mfiles\setupcode.txt'), 'C:\HDI\HDI.py'))
    else:
        subprocess.run(['cp', src_file, dest_file], check=True)
    print('Main file created: HDI.py')
except subprocess.CalledProcessError as e:
    print(f'Error copying file: {e}')
    sys.exit()
except Exception as e:
    print(f'Unexpected error: {e}')
    sys.exit()

# Установка зависимости colorama
print('Installing libraries...')
try:
    subprocess.run([sys.executable, '-m', 'pip', 'install', 'colorama'], check=True)
    print('Libraries installed.')
except subprocess.CalledProcessError as e:
    print(f'Pip installation failed: {e}')
    sys.exit()

print('Setup completed successfully!')
print('Press ENTER to exit.')
input()
