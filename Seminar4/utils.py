import subprocess
import paramiko
import yaml


def deploy(host, user, password, local_path, remote_path):
    result = []
    upload_files(host, user, password, local_path, remote_path)
    result.append(ssh_checkout(host,
                                user,
                                password,
                                f"echo '{password}' | sudo -S dpkg -i {remote_path}",
                                "Настраивается пакет"))
    search_text = remote_path.split("/")[:-1].split(".")[0]
    result.append(ssh_checkout(host,
                                user,
                                password,
                                f"echo '{password}' | sudo -S dpkg -s {search_text}",
                                "Status: install ok installed"
                                ))
    return all(result)

def ssh_checkout(host, user, password, cmd, text, port=22):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect(hostname=host, username=user, password=password, port=port)
    stdin, stdout, stderr = client.exec_command(cmd)
    exit_code = stdout.channel.recv_exit_status()
    out = (stdout.read() + stderr.read()).decode("utf-8")
    client.close()
    return True if (text in out and exit_code == 0) else False

def ssh_checkout_negative(host, user, password, cmd, text, port=22):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect(hostname=host, username=user, password=password, port=port)
    stdin, stdout, stderr = client.exec_command(cmd)
    exit_code = stdout.channel.recv_exit_status()
    out = (stdout.read() + stderr.read()).decode("utf-8")
    client.close()
    return True if (text in out and exit_code != 0) else False

def ssh_exec_command(host, user, password, cmd, port=22):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect(hostname=host, username=user, password=password, port=port)
    stdin, stdout, stderr = client.exec_command(cmd)
    out = (stdout.read() + stderr.read()).decode("utf-8")
    client.close()
    return out

def upload_files(host, user, password, local_path, remote_path, port=22):
    print()
    print(f"Loading file {local_path} to remote computer in {remote_path}...")
    transport = paramiko.Transport((host, port))
    try:
        transport.connect(username=user, password=password)
        if transport.is_active():
            sftp = paramiko.SFTPClient.from_transport(transport)
            sftp.put(local_path, remote_path)
        if sftp:
            sftp.close()
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        if transport:
            transport.close()

def checkout(cmd: str, text: str) -> bool:
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
    if result.returncode == 0 and text in result.stdout:
        return True
    else:
        return False

def checkout_negative(cmd: str, text: str) -> bool:
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
    if result.returncode != 0 and text in result.stderr:
        return True
    else:
        return False

def calculate_crc32(cmd: str):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
    if result.returncode == 0:
        return result.stdout

def exec_command(cmd):
    subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")