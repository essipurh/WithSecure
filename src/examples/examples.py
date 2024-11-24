# example usage
# for testing purposes
from batching.batch_processor import batches_generator
from mock_data_generator import generate_mock_data
from batching.logging_config import logger


def process_test_stream_data_to_batches():
    """To test with larger mock data."""
    mock_records_stream = generate_mock_data(1200, 1_200_000)

    for i, batch in enumerate(batches_generator(mock_records_stream)):
        batch_size = sum(len(record.encode("utf-8")) for record in batch)
        max_size = max(len(record.encode("utf-8")) for record in batch)
        if batch_size > 5_242_880 or max_size > 1_048_576:
            logger.warning(
                f"SIZE EXCEEDED: batch size: {batch_size}, maximum record size: {max_size}"
            )
        logger.info(
            f"Batch {i+1}: {len(batch)} records, {batch_size} bytes, {max_size} maximum record size."
        )


if __name__ == "__main__":
    process_test_stream_data_to_batches()
