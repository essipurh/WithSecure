import random
import string
from typing import Generator, List


def generate_mock_data(n_records: int, max_record_length: int) -> Generator:
    """
    Generates a list of mock records with random string lengths.
    Lists length is n_records and maximum record size is max_regird_length.

    Parameters
    ----------
    n_records : int
      Number of records generated.

    max_record_length : int
      Maximum length of a single record (string).

    Yields
    ------
    Generator
      Returns a list of strings aka records.
    """
    for _ in range(n_records):
        record_length = random.randint(1, max_record_length)
        yield "".join(
            random.choices(string.ascii_letters + string.digits, k=record_length)
        )
