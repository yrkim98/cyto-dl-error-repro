# cyto-dl-error-repro

## Recreate merged transform errors

1) Install test data on `cyto-dl` by running `cyto-dl/scripts/download_test_data.py
2) In the test data folder `cyto-dl/data/example_experiment_data/segmentation`, change `train.csv` to have five columns, `raw`, `seg1`, `seg2`, `exclude_mask`, `base_image`, `merge_mask`
3) `raw` is the path to the raw image located in `cyto-dl/data/example_experiment_data/s3_data`
4) `seg1` and `seg2` is the path to the segmentated image located in `cyto-dl/data/example_experiment_data/s3_data`
5) make 3 copies of this .csv in `cyto-dl/data/example_experiment_data/segmentation`, name them `test.csv`, `train.csv`, `valid.csv`
6) Change logger in `segmentation_plugin.yaml` to `csv.yaml`
7) Change all `missing_key_mode`’s in `cyto-dl/data/im2im/segmentation_plugin.yaml` to `“create"` instead of `“ignore"`
8) in `scripts/merged_transform_error.py` set `output_folder` at top of screen to any folder on your filesystem to save training data to
9) set `cyto_dl_seg_folder` to `cyto-dl/data/example_experiment_data/segmentation`
10) run script

## Recreate error running training on only one segmentation (with other columns left blank)
1) Install test data on `cyto-dl` by running `cyto-dl/scripts/download_test_data.py (If you have it installed, reinstall)
2) In the test data folder `cyto-dl/data/example_experiment_data/segmentation`, change `train.csv` to have five columns, `raw`, `seg1`, `seg2`, `exclude_mask`, `base_image`, `merge_mask`
3) `raw` is the path to the raw image located in `cyto-dl/data/example_experiment_data/s3_data`
4) `seg1` is the path to the segmentated image located in `cyto-dl/data/example_experiment_data/s3_data`
5) leave `seg2` undefined, as well as the other columns in the csv
6) make 3 copies of this .csv in `cyto-dl/data/example_experiment_data/segmentation`, name them `test.csv`, `train.csv`, `valid.csv`
7) Ensure logger in `segmentation_plugin.yaml` is `csv.yaml`
8) Ensure all `missing_key_mode`’s in `cyto-dl/data/im2im/segmentation_plugin.yaml` are set to `“create"`
8) in `scripts/merged_transform_error.py` set `output_folder` at top of screen to any folder on your filesystem to save training data to
9) set `cyto_dl_seg_folder` to `cyto-dl/data/example_experiment_data/segmentation`
10) run script

