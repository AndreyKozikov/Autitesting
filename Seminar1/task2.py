import subprocess
import string

def split_to_words(string_to_split):
    cleaned_string = string_to_split.replace("\n", " ")
    for char in string.punctuation:
        cleaned_string = cleaned_string.replace(char, " ")
    return [word for word in cleaned_string.lower().split(" ") if word]

def checkout(cmd: str, text: str, split_words=False) -> bool:
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    string_result = split_to_words(result.stdout) if split_words else result.stdout.lower()
    return result.returncode == 0 and (any (text.lower() in word for word in string_result) if split_words
                                       else text.lower() in string_result)


if __name__ == '__main__':
    assert checkout('ping -c 3 rambler.ru', '0% packet loss'), print('test FAIL')
    assert checkout('ping -c 3 rambler.ru', 'packet', True), print('test FAIL')