import venv
import subprocess
import sys

def create_venv_and_install():
    venv.create('venv', with_pip=True)
    
    # Determine the pip path
    if sys.platform == 'win32':
        pip_path = r'venv\Scripts\pip'
    else:
        pip_path = 'venv/bin/pip'
    
    # Install dependencies
    subprocess.check_call([pip_path, 'install', '-r', 'requirements.txt'])

if __name__ == "__main__":
    create_venv_and_install()
