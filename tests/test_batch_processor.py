# TODO: fix the pytest module imports: instead of bacthing.batch_processor --> batch_processor
from batching.batch_processor import batches_generator

def test_split_into_batches():
  records = ['a', 'aabb' * 100]
  batches = list(batches_generator(records))

  assert len(batches) == 1
  assert batches[0] == records

def test_exclude_large_records():
    records = ["a" * (1_048_577), "b" * 500]
    batches = list(batches_generator(records))
    assert len(batches) == 1
    assert batches[0] == ["b" * 500]

def test_several_batches():
   too_big = "b" * (1_048_577)
   records = ["a" for i in range(600)]
   records.append(too_big)
   batches = list(batches_generator(records))
   assert len(batches) == 2
   assert len(batches[0]) == 500
   assert len(batches[1]) == 100 # the length of the input list is 600 + 1 
   assert batches[-1][-1] != too_big
