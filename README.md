# cyto-dl-error-repro

## Recreate merged transform errors

1) Install test data on `cyto-dl` by running `cyto-dl/scripts/download_test_data.py
2) In the test data folder `cyto-dl/data/example_experiment_data/segmentation`, change `train.csv` to have five columns, `raw`, `seg1`, `seg2`, `exclude_mask`, `base_image`, `merge_mask`
3) `raw` is the path to the raw image located in `cyto-dl/data/example_experiment_data/s3_data`
4) `seg1` and `seg2` is the path to the segmentated image located in `cyto-dl/data/example_experiment_data/s3_data`
5) make 3 copies of this .csv in `cyto-dl/data/example_experiment_data/segmentation`, name them `test.csv`, `train.csv`, `valid.csv`
6) in `scripts/merged_transform_error.py` set `output_folder` at top of screen to any folder on your filesystem to save training data to
7) set `cyto_dl_seg_folder` to `cyto-dl/data/example_experiment_data/segmentation`
8) run script


