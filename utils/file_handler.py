
import pandas as pd
import chardet

def detect_encoding(file):
    rawdata = file.read(10000)
    result = chardet.detect(rawdata)
    file.seek(0)

    encoding = result.get('encoding')

    # Avoid incorrect ASCII detection
    if not encoding or encoding.lower() == 'ascii':
        return 'utf-8'

    return encoding


def read_large_csv(file):
    encoding = detect_encoding(file)

    encodings = [encoding, 'utf-8-sig', 'utf-8', 'cp1252', 'latin1']

    for enc in dict.fromkeys(encodings):
        try:
            file.seek(0)
            return pd.read_csv(file, encoding=enc)
        except UnicodeDecodeError:
            continue

    raise ValueError("Unable to read CSV. Please check its file encoding.")
