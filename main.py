# for testing purposes
import logging
import os
from datetime import datetime
from batching.batch_processor import batches_generator
from utils.data_utils import generate_mock_data

# TODO: proper logging set up
logging.basicConfig(
    filename=os.path.join(
        "logs", f"batches_test_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log"
    ),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def process_test_stream_data_to_batches():
    """To test with larger mock data."""
    mock_records_stream = generate_mock_data(1200, 1_200_000)

    for i, batch in enumerate(batches_generator(mock_records_stream)):
        batch_size = sum(len(record.encode("utf-8")) for record in batch)
        max_size = max(len(record.encode("utf-8")) for record in batch)
        if batch_size > 5_242_880 or max_size > 1_048_576:
            print(
                f"********* ERROR - MAX SIZE EXCEEDED *******\n batchsize: {batch_size}\n record size: {max_size}"
            )
        logging.info(
            f"Batch {i+1}: {len(batch)} records, {batch_size} bytes, {max_size} maximum record size."
        )
        print(f"Processed Batch {i + 1} with {len(batch)} records.")


if __name__ == "__main__":
    process_test_stream_data_to_batches()
