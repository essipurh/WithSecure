# WithSecure Programming Exercise

This project provides answer to the WithSecure exercise, where the mission was to write a library which takes in an array of variable size records and splits the input into a batch of records. The input for the library is [ record1, record2, ..., recordN]. The Output is [ batch1, batch2,.., batchN], where batches are an array of records.

The output has following restrictions:

- maximum size of output record is 1 MB, larger records should be discarded
- maximum size of output batch is 5 MB
- maximum number of records in an output batch is 500

---

## Features

- Processes records of variable size and batches them.
- Discards records exceeding size limits.
- Maintains the order of records.

## Usage

**To install using venv:**

- run: python -m venv .venv
- activate .venv:
  - venv\Scripts\activate.bat # In cmd.exe
  - venv\Scripts\Activate.ps1 # In PowerShell
  - source myvenv/bin/activate # Linux/MacOS
- install requirements: pip install -r requirements.txt

**To istall using setup.py:**

- run: pip install -e .

The library takes an input array of records and outputs a list of batches that conform to the following constraints:

- **Maximum record size**: 1 MB (records larger than this size are discarded).
- **Maximum batch size**: 5 MB.
- **Maximum records per batch**: 500.

The output is a list of batches, where each batch is an array of records in the same order as the input.

---

## Example

To test the batching_generator, src/examples/example.py has an example, which takes in streaming mock data and logs
processing of the data. The script create a logs/ directory where logging files can be found. Example of a log file's contents:

2024-11-24 13:47:47,943 - INFO - Batch 104: 9 records, 4984360 bytes, 984052 maximum record size
2024-11-24 13:47:48,235 - WARNING - Record discarded. Record size: 1182243.
2024-11-24 13:47:48,403 - WARNING - Record discarded. Record size: 1122240.
2024-11-24 13:47:48,585 - WARNING - Record discarded. Record size: 1199934.
2024-11-24 13:47:49,238 - INFO - Batch 105: 13 records, 5186327 bytes, 934180 maximum record size.
2024-11-24 13:47:49,849 - INFO - Batch 106: 11 records, 4832103 bytes, 948536 maximum record size.
2024-11-24 13:47:50,555 - INFO - Batch 107: 9 records, 4824756 bytes, 1046710 maximum record size.
