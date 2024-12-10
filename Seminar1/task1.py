import subprocess

def checkout(cmd: str, text: str) -> bool:
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0 and text in result.stdout:
        return True
    else:
        return False


if __name__ == '__main__':
    assert checkout('ping -c 3 rambler.ru', '12% packet loss'), print('test FAIL')