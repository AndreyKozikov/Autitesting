import pytest
from utils import exec_command
import random, string
import yaml
from datetime import datetime

with open('config.yaml') as f:
    # читаем документ YAML
    config = yaml.safe_load(f)
    FOLDER_IN = config['FOLDER_IN']
    FOLDER_OUT = config['FOLDER_OUT']
    FOLDER_EXTRACT = config['FOLDER_EXTRACT']
    COUNT = config['COUNT']
    ARC_NAME = config['ARC_NAME']
    FILE_SIZE = config['FILE_SIZE']
    ARC_TYPE = config['ARC_TYPE']

@pytest.fixture()
def clear_folders():
    exec_command(f"rm -rf {FOLDER_IN}/* {FOLDER_OUT}/* {FOLDER_EXTRACT}/*")

@pytest.fixture()
def make_folders():
    exec_command(f"mkdir {FOLDER_IN} {FOLDER_OUT} {FOLDER_EXTRACT}")

@pytest.fixture()
def make_files():
    files = []
    for i in range(COUNT):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        exec_command(f"cd {FOLDER_IN}; dd if=/dev/urandom of={filename} bs={FILE_SIZE} count=1 iflag=fullblock")
        files.append(filename)
    return files

@pytest.fixture()
def make_subfolders():
    filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    subfoldername = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    exec_command(f"mkdir {FOLDER_IN}/{subfoldername}")
    exec_command(f"cd {FOLDER_IN}/{subfoldername}; dd if=/dev/urandom of={filename} bs={FILE_SIZE} count=1 iflag=fullblock")
    return subfoldername, filename

@pytest.fixture()
def make_broken_arc():
    files = []
    for i in range(COUNT):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        exec_command(f"cd {FOLDER_IN}; dd if=/dev/urandom of={filename} bs={FILE_SIZE} count=1 iflag=fullblock")
        files.append(filename)
    exec_command(f"cd {FOLDER_IN}; 7z a -t{ARC_TYPE} {FOLDER_OUT}/{ARC_NAME}.{ARC_TYPE}")
    exec_command(f"truncate -s 1 {FOLDER_OUT}/{ARC_NAME}.{ARC_TYPE}")
    yield
    exec_command(f"rm -rf {FOLDER_IN}/* {FOLDER_OUT}/*")



@pytest.fixture(autouse=True)
def log_test_statistics():
    yield  # Выполнение теста
    try:
        with open("stat.txt", "a") as stat_file:
            # Текущее время
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Статистика загрузки процессора из файла /proc/loadavg
            cpu_load = "N/A"
            try:
                with open("/proc/loadavg", "r") as loadavg_file:
                    cpu_load = loadavg_file.read().strip()
            except FileNotFoundError:
                cpu_load = "Load average not available"

            # Формирование строки для записи
            log_entry = (f"Текущее время: {current_time}, количество файлов: {COUNT}, "
                         f"размер файла: {FILE_SIZE}, загрузка процессора: {cpu_load}\n")

            # Запись строки в файл
            stat_file.write(log_entry)
    except Exception as e:
        print(f"Ошибка при записи в файл stat.txt: {e}")