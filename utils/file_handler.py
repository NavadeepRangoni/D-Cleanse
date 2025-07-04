import pandas as pd
import chardet

def detect_encoding(file):
    rawdata = file.read(10000)
    result = chardet.detect(rawdata)
    file.seek(0)
    return result['encoding']

def read_large_csv(file):
    encoding = detect_encoding(file)
    return pd.read_csv(file, encoding=encoding)