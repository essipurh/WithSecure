from batching.batch_processor import batches_generator

MAX_RECORD_SIZE = 1_048_576  # 1 MB
MAX_BATCH_SIZE = 5_242_880  # 5 MB
MAX_RECORDS_PER_BATCH = 500


def test_split_into_batches():
    records = ["a", "aabb" * 100]
    batches = list(batches_generator(records))

    assert len(batches) == 1
    assert batches[0] == records


def test_split_into_batches_generator():
    records = ("a" * i for i in range(10_000))
    batches = list(batches_generator(records))

    assert len(batches) == 10_000 / MAX_RECORDS_PER_BATCH
    for batch in batches:
        assert (
            max(len(record.encode("utf-8")) for record in batch) <= MAX_RECORD_SIZE
        )  # 1MB
        assert (
            sum(len(record.encode("utf-8")) for record in batch) <= MAX_BATCH_SIZE
        )  # 5MB
        assert len(batch) <= MAX_RECORDS_PER_BATCH  # 500


def test_exclude_large_records():
    records = ["a" * 1_048_577, "b" * 500]
    batches = list(batches_generator(records))

    assert len(batches) == 1
    assert batches[0] == ["b" * 500]


def test_several_batches():
    too_big = "b" * 1_048_577
    records = ["a" for i in range(600)]
    records.append(too_big)
    batches = list(batches_generator(records))

    assert len(batches) == 2
    assert len(batches[0]) == 500
    assert len(batches[1]) == 100  # the length of the input list is 600 + 1
    assert batches[-1][-1] != too_big
