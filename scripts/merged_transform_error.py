from cyto_dl.api.model import CytoDLModel

model = CytoDLModel()
model.load_default_experiment(
    "segmentation_plugin",
    output_dir=output_folder,
)

# mimic overrides done in ml-segmenter
overrides = dict()
overrides["trainer.accelerator"] = "cpu"
overrides["spatial_dims"] = 3
overrides["trainer.max_epochs"] = 10
overrides["data.path"] = ""
overrides["data._aux.patch_shape"] = [16, 64, 64]
overrides["model._aux.filters"] = [16, 32, 64]
model.override_config(overrides)

model.train()