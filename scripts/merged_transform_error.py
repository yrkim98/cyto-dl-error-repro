from cyto_dl.api.model import CytoDLModel

# define some output folder to save training runs to
# output_folder = ''
model = CytoDLModel()
model.load_default_experiment(
    "segmentation_plugin",
    output_dir=output_folder,
)

# mimic overrides done in ml-segmenter
overrides = dict()
overrides["trainer.accelerator"] = "cpu"
overrides["trainer.max_epochs"] = 10
overrides["data.path"] = #path to segmentation folder in cyto-dl/data/example_experiment_data
overrides["data._aux.patch_shape"] = [16, 64, 64]
overrides["spatial_dims"] = 3
model.override_config(overrides)

model.train(run_async=True)