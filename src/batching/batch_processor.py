from typing import Generator, List

# TODO: logging for discarded records? to use deque instead of list?
MAX_RECORD_SIZE = 1_048_576  # 1 MB
MAX_BATCH_SIZE = 5_242_880  # 5 MB
MAX_RECORDS_PER_BATCH = 500


def batches_generator(records: List[str]) -> Generator:
    """
    Splits input of list of records into batches maintaining the order of the records.
    In the output the maximum size of record is 1 MB, maximum batch size is 5 MB and
    maximum amount if records in a batch is 500.

    Parameters
    -----------
    records : list[str]
      List of records (strings).

    Yields
    ------
    generator[list[str]]
      A generator of batches, where each batch is a list of records (strings).
    """

    current_batch = []
    current_batch_size = 0

    for record in records:
        record_size = len(
            record.encode("utf-8")
        )  # the records are assumed to be strings, could use sys.getsizeof if non string
        if record_size > MAX_RECORD_SIZE:
            continue

        if (record_size + current_batch_size > MAX_BATCH_SIZE) or (
            len(current_batch) >= MAX_RECORDS_PER_BATCH
        ):
            yield current_batch
            current_batch = []
            current_batch_size = 0

        current_batch.append(record)
        current_batch_size += record_size

    if current_batch:
        yield current_batch


# not sure if needed. Testing uses the generator..
def create_batches(records: List[str]) -> List[List[str]]:
    """
    Creates a list of batches, which are list or input records (string).
    Parameters
    -----------
    records : list[str]
      List of records (strings).
    Returns
    -------
    list[list[str]]
      A list of batches, where each batch is a list of records (strings).
    """
    return list(batches_generator(records))