# WithSecure Programming Exercise

This project provides answer to the WithSecure exercise, where the mission was to write a library which takes in an array of variable size records and splits the input into a batch of records. The input for the library is [ record1, record2, ..., recordN]. The Output is [ batch1, batch2,.., batchN], where batches are an array of records.

The output has following restrictions:

- maximum size of output record is 1 MB, larger records should be discarded
- maximum size of output batch is 5 MB
- maximum number of records in an output batch is 500
