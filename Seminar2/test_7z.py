from utils import checkout, calculate_crc32

FOLDER_IN = "/home/wisdom/GB_tests/test_in"
FOLDER_OUT = "/home/wisdom/GB_tests/test_out"
FOLDER_EXTRACT = "/home/wisdom/GB_tests/extract"
ARC_NAME = "arch2.7z"

# def make_dir():
#     pass
#
# def clear_dir():
#     pass
#
# def make_files():
#     pass

def test_add_files():
    result = []
    result.append(checkout(f"cd {FOLDER_IN}; 7z a {FOLDER_OUT}/{ARC_NAME}", "Everything is O"))
    result.append(checkout(f"cd {FOLDER_OUT}; ls", f"{ARC_NAME}"))
    assert all(result), "add files to archive TEST FAIL"

def test_extract_files():
    result = []
    result.append(checkout(f"cd {FOLDER_OUT}; 7z e -y {FOLDER_OUT}/{ARC_NAME} -o{FOLDER_EXTRACT}",
                    "Everything is Ok"))
    result.append(checkout(f"ls {FOLDER_EXTRACT}", "test1"))
    result.append(checkout(f"ls {FOLDER_EXTRACT}", "test2"))
    result.append(checkout(f"ls {FOLDER_EXTRACT}", "test3"))
    assert all(result), "extract files from archive TEST FAIL"

def test_integrity_arc():
    assert checkout(f"7z t {FOLDER_OUT}/{ARC_NAME}", "Everything is Ok"), "testing archive TEST FAIL"

def test_delete_from_arc():
    assert checkout(f"7z d {FOLDER_OUT}/{ARC_NAME} {test2}",
                    "Everything is Ok"), "deleting from archive TEST FAIL"

def test_update_arc():
    assert checkout(f"cd {FOLDER_IN}; 7z u {FOLDER_OUT}/{ARC_NAME}", "Everything is Ok"), \
        "updating archive TEST FAIL"


def test_list_contents_arc():
    result = []
    result.append((f"7z l {FOLDER_OUT}/{ARC_NAME}", "test1"))
    result.append((f"7z l {FOLDER_OUT}/{ARC_NAME}", "test2"))
    result.append((f"7z l {FOLDER_OUT}/{ARC_NAME}", "test3"))
    assert all(result), "list contents of archive TEST FAIL"

def test_extract_with_full_paths():
    result = []
    result.append(checkout(f"7z x -y {FOLDER_OUT}/{ARC_NAME} -o{FOLDER_EXTRACT}", "Everything is Ok"))
    result.append(checkout(f"ls {FOLDER_EXTRACT}", "test1"))
    result.append(checkout(f"ls {FOLDER_EXTRACT}", "test2"))
    result.append(checkout(f"ls {FOLDER_EXTRACT}", "test3"))
    result.append(checkout(f"ls {FOLDER_EXTRACT}", "folder1"))
    result.append(checkout(f"ls {FOLDER_EXTRACT}", "test4"))
    result.append(checkout(f"ls {FOLDER_EXTRACT}", "test5"))
    result.append(checkout(f"ls {FOLDER_EXTRACT}", "test6"))
    assert all(result), "extract with full paths TEST FAIL"

def test_calculate_hash_arc():
    crc = calculate_crc32(f"crc32 {FOLDER_OUT}/{ARC_NAME}").strip().upper()
    assert checkout(f"7z h {FOLDER_OUT}/{ARC_NAME}", crc), "calculate hash values for files in archive TEST FAIL"
