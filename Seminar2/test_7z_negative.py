from Seminar3.utils import checkout_negative

FOLDER_IN = "/home/wisdom/GB_tests/test_in"
FOLDER_OUT = "/home/wisdom/GB_tests/test_out"
FOLDER_EXTRACT = "/home/wisdom/GB_tests/extract"

def test_negative_extract_files():
    assert checkout_negative("7z e {}/broken_arch2.7z -o{}".format(FOLDER_OUT, FOLDER_OUT, FOLDER_EXTRACT),
                    "Is not archive"), "extract files from archive TEST FAIL"

def test_negative_integrity_arc():
    assert checkout_negative("7z t {}/broken_arch2.7z".format(FOLDER_OUT), "Is not archive"), "testing archive TEST FAIL"