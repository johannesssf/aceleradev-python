import hashlib
import json
import requests
import string


IN_URL = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token={}'
OUT_URL = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token={}'
OUT_URL_TEST = 'https://httpbin.org/post'
ANSWER_FILE = 'answer.json'
TOKEN = '8ac215804c8d19bc702a4dd6c8e43e9da1c85670'


def read_data(url):
    data = requests.get(url)
    return json.loads(data.text)


def decrypt_char(key, character):
    char_idx = string.ascii_lowercase.find(character)

    if char_idx >= 0:
        decrypted = char_idx - key
        return string.ascii_lowercase[decrypted]

    return character


def save_data_to_file(data, filename):
    with open(filename, 'w') as answer:
        json.dump(data, answer)


def send_file_to_server(url, filename):
    files = {"answer": (filename, open(filename, 'rb'))}
    res = requests.post(url, files=files)

    print(res.status_code)
    print(res.text)


def calculate_sha1(text):
    return hashlib.sha1(text.encode()).hexdigest()


if __name__ == "__main__":
    data = read_data(IN_URL.format(TOKEN))
    decrypted_chars = [decrypt_char(data['numero_casas'], c)
                       for c in data['cifrado'].lower()]

    decrypted_msg = ''.join(decrypted_chars)
    data['decifrado'] = decrypted_msg
    data['resumo_criptografico'] = calculate_sha1(decrypted_msg)

    save_data_to_file(data, ANSWER_FILE)
    send_file_to_server(OUT_URL.format(TOKEN), ANSWER_FILE)
