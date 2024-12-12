from fixtures import *
from utils import *
import pytest

with open('config.yaml') as f:
    # читаем документ YAML
    config = yaml.safe_load(f)
    FOLDER_IN = config['FOLDER_IN']
    FOLDER_OUT = config['FOLDER_OUT']
    FOLDER_EXTRACT = config['FOLDER_EXTRACT']
    COUNT = config['COUNT']
    ARC_NAME = config['ARC_NAME']
    ARC_TYPE = config['ARC_TYPE']
    host = config['host']
    user = config['user']
    password = config['password']
    port = config['port']
    local_path = config['local_path']
    remote_path = config['remote_path']
    pkgname = config['pkgname']


class TestPositive:

    # def test_deploy(self):
    #     result = []
    #     upload_files(host, user, password, pkgname+".deb", remote_path)
    #     result.append(ssh_checkout(host,
    #                                 user,
    #                                 password,
    #                                 f"echo '{password}' | sudo -S dpkg -i {remote_path}",
    #                                 "Настраивается пакет"))
    #     result.append(ssh_checkout(host,
    #                                 user,
    #                                 password,
    #                                 f"echo '{password}' | sudo -S dpkg -s {pkgname}",
    #                                 "Status: install ok installed"
    #                                 ))
    #     return all(result)

    # Тест на добавление файлов в архив
    # Очищаем папки перед началом теста.
    # Создаем необходимые папки и подкаталоги.
    # Добавляем файлы из входной папки в архив.
    # Проверяем, что архив успешно создан и содержит ожидаемые файлы.
    def test_add_files(self, clear_folders, make_folders, make_subfolders, make_files):
        result = []
        result.append(ssh_checkout(host,
                                   user,
                                   password,
                                   f"cd {FOLDER_IN}; 7z a -t{ARC_TYPE} {FOLDER_OUT}/{ARC_NAME}.{ARC_TYPE}",
                                   "Everything is Ok"))
        result.append(ssh_checkout(host,
                                   user,
                                   password,
                                   f"cd {FOLDER_OUT}; ls",
                                   f"{ARC_NAME}.{ARC_TYPE}"))
        assert all(result), "add files to archive TEST FAIL"


    # Тест на извлечение файлов из архива
    # Очищаем папки перед началом теста.
    # Создаем необходимые папки и подкаталоги.
    # Создаем архив с файлами из входной папки.
    # Извлекаем файлы из архива в указанную папку.
    # Проверяем наличие извлеченных файлов в целевой папке.
    def test_extract_files(self, clear_folders, make_folders, make_subfolders, make_files):
        result = []
        result.append(ssh_checkout(host,
                                   user,
                                   password,
                                   f"cd {FOLDER_IN}; 7z a -t{ARC_TYPE} {FOLDER_OUT}/{ARC_NAME}.{ARC_TYPE}",
                                   "Everything is Ok"))
        result.append(ssh_checkout(host,
                                   user,
                                   password,
                                  f"7z e -y -t{ARC_TYPE} {FOLDER_OUT}/{ARC_NAME}.{ARC_TYPE} -o{FOLDER_EXTRACT}",
                                  "Everything is Ok"))
        for file in make_files:
            result.append(ssh_checkout(host,
                                   user,
                                   password,
                              f"ls {FOLDER_EXTRACT}", file))
        assert all(result), "extract files from archive TEST FAIL"


    # Тест на целостность архива
    # Проверяем целостность архива с помощью команды 7z t.
    # Убеждаемся, что архив не поврежден и все файлы доступны.
    def test_integrity_arc(self):
        assert ssh_checkout(host,
                            user,
                            password,
                            f"7z t -t{ARC_TYPE} {FOLDER_OUT}/{ARC_NAME}.{ARC_TYPE}",
                            "Everything is Ok"), "testing archive TEST FAIL"

    # Тест на удаление файлов из архива
    # Очищаем папки перед началом теста.
    # Создаем необходимые папки и подкаталоги.
    # Создаем архив с файлами.
    # Удаляем один файл из архива.
    # Проверяем, что файл был успешно удален из архива.
    def test_delete_from_arc(self, clear_folders, make_folders, make_subfolders, make_files):
        result = []
        result.append(ssh_checkout(host,
                                   user,
                                   password,
                                   f"cd {FOLDER_IN}; 7z a -t{ARC_TYPE} {FOLDER_OUT}/{ARC_NAME}.{ARC_TYPE}",
                                   "Everything is Ok"))
        result.append(ssh_checkout(host,
                                   user,
                                   password,
                                   f"7z d -t{ARC_TYPE} {FOLDER_OUT}/{ARC_NAME}.{ARC_TYPE} {make_files[1]}",
                                   "Everything is Ok"))
        result.append(not ssh_checkout(host,
                                      user,
                                      password,
                                  f"7z l -t{ARC_TYPE} {FOLDER_OUT}/{ARC_NAME}.{ARC_TYPE}",
                                        make_files[1]))
        assert all(result), "deleting from archive TEST FAIL"

    # Тест на обновление архива новыми файлами
    # Обновляем архив добавлением новых файлов из входной папки.
    # Проверяем, что новые файлы были успешно добавлены в архив.
    def test_update_arc(self, make_subfolders):
        result = []
        result.append(ssh_checkout(host,
                                   user,
                                   password,
                                   f"cd {FOLDER_IN}; 7z u -y -t{ARC_TYPE} {FOLDER_OUT}/{ARC_NAME}.{ARC_TYPE}",
                                   "Everything is Ok"))

        result.append(ssh_checkout(host,
                                        user,
                                        password,
                                       f"7z l -t{ARC_TYPE} {FOLDER_OUT}/{ARC_NAME}.{ARC_TYPE}",
                                       make_subfolders[0]))
        assert all(result), "updating archive TEST FAIL"

    # Тест на вывод содержимого архива
    # Очищаем папки перед началом теста.
    # Создаем необходимые папки и подкаталоги.
    # Создаем архив с файлами из входной папки.
    # Проверяем содержимое архива на наличие ожидаемых файлов.
    def test_list_contents_arc(self, clear_folders, make_files):
        result = []
        result.append(ssh_checkout(host,
                                   user,
                                   password,
                                   f"cd {FOLDER_IN}; 7z a -t{ARC_TYPE} {FOLDER_OUT}/{ARC_NAME}.{ARC_TYPE}",
                                   "Everything is Ok"))
        for file in make_files:
            result.append(ssh_checkout(host,
                                   user,
                                   password,
                                       f"7z l -t{ARC_TYPE} {FOLDER_OUT}/{ARC_NAME}.{ARC_TYPE}",
                                       file))
        assert all(result), "list contents of archive TEST FAIL"


    # Тест на извлечение файлов с сохранением структуры каталогов
    # Очищаем папки перед началом теста.
    # Создаем необходимые папки и подкаталоги.
    # Создаем архив с файлами из входной папки.
    # Извлекаем файлы с сохранением структуры каталогов в указанную папку.
    # Проверяем наличие извлеченных файлов и подкаталогов после извлечения.
    def test_extract_with_full_paths(self, clear_folders, make_subfolders, make_files):
        result = []
        result.append(ssh_checkout(host,
                                   user,
                                   password,
                                   f"cd {FOLDER_IN}; 7z a -t{ARC_TYPE} {FOLDER_OUT}/{ARC_NAME}.{ARC_TYPE}",
                                   "Everything is Ok"))
        result.append(ssh_checkout(host,
                                   user,
                                   password,
                                   f"7z x -y -t{ARC_TYPE} {FOLDER_OUT}/{ARC_NAME}.{ARC_TYPE} -o{FOLDER_EXTRACT}",
                                   "Everything is Ok"))
        for file in make_files:
            result.append(ssh_checkout(host,
                                   user,
                                   password,
                                       f"ls {FOLDER_EXTRACT}", file))
        result.append(ssh_checkout(host,
                                   user,
                                   password,
                                   f"ls {FOLDER_EXTRACT}",
                                   make_subfolders[0]))
        result.append(ssh_checkout(host,
                                   user,
                                   password,
                                   f"ls {FOLDER_EXTRACT}/{make_subfolders[0]}",
                                   make_subfolders[1]))
        assert all(result), "extract with full paths TEST FAIL"


    # Тест на вычисление хеша архива
    # Вычисляем CRC32 для архива для проверки целостности данных.
    # Создаем архив.
    # Проверяем соответствие хеш-значения с ожидаемым значением CRC32 для всех файлов в архиве.
    def test_calculate_hash_arc(self, clear_folders, make_subfolders, make_files):
        ssh_exec_command(host,
                        user,
                        password,
                         f"cd {FOLDER_IN}; 7z a -t{ARC_TYPE} {FOLDER_OUT}/{ARC_NAME}.{ARC_TYPE}")
        crc = ssh_exec_command(host,
                               user,
                               password,
                               f"crc32 {FOLDER_OUT}/{ARC_NAME}.{ARC_TYPE}").strip().upper()
        assert ssh_checkout(host,
                            user,
                            password,
                            f"7z h -t{ARC_TYPE} {FOLDER_OUT}/{ARC_NAME}.{ARC_TYPE}",
                            crc), "calculate hash values for files in archive TEST FAIL"
