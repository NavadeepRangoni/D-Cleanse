
import pandas as pd
import chardet


def detect_encoding(file):
    rawdata = file.read(10000)
    result = chardet.detect(rawdata)
    file.seek(0)

    encoding = result.get("encoding")

    if not encoding or encoding.lower() == "ascii":
        return "utf-8"

    return encoding


def read_large_csv(file):
    encodings = ["utf-8", "utf-8-sig", "latin1", "cp1252"]

    last_error = None

    for enc in encodings:
        try:
            file.seek(0)

            df = pd.read_csv(
                file,
                encoding=enc,
                engine="python",
                on_bad_lines="warn",
                sep=None,
                dtype=str,
                keep_default_na=False
            )

            return df

        except (
            UnicodeDecodeError,
            pd.errors.ParserError,
            ValueError
        ) as e:
            last_error = e

    raise ValueError(
        f"Unable to read CSV file. Error: {last_error}"
    )
