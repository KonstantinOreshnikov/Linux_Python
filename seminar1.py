import subprocess

def check_command_output(command, text):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)

        if text in result.stdout:
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return False

command = 'cat /etc/os-release'
text = 'PRETTY_NAME="Ubuntu 22.04.4 LTS"'
# command = 'ls -l'
# text = 'example.txt'

result = check_command_output(command, text)
print(result)