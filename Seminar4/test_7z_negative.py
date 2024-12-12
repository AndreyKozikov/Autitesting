from fixtures import *
from utils import ssh_checkout_negative
import yaml
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



class TestNegative:
    def test_negative_extract_files(self, clear_folders, make_folders, make_subfolders, make_broken_arc):
        assert ssh_checkout_negative(host,
                                   user,
                                   password,
                                     f"7z e -t{ARC_TYPE} {FOLDER_OUT}/{ARC_NAME}.{ARC_TYPE} -o{FOLDER_EXTRACT}",
                                    "Is not archive"), "extract files from archive TEST FAIL"

    def test_negative_integrity_arc(self, clear_folders, make_folders, make_subfolders, make_broken_arc):
        assert ssh_checkout_negative(host,
                                   user,
                                   password,
                                     f"7z t -t{ARC_TYPE} {FOLDER_OUT}/{ARC_NAME}.{ARC_TYPE}",
                                    "Is not archive"), "testing archive TEST FAIL"