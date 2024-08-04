import subprocess

def check_style():
    result = subprocess.run(['flake8', '.'], capture_output=True, text=True)
    if result.returncode != 0:
        print("Style check failed:")
        print(result.stdout)
        exit(1)
    else:
        print("Style check passed!")

if __name__ == "__main__":
    check_style()
