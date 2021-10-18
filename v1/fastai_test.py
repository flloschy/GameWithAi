from fastai.vision.all import *
path = untar_data(URLs.PETS)/'images'
def is_cat(x): ImageDataLoaders.from_name_func(
    path, get_image_files(path), valid_pct=0.2, seed=42,
    label_func=is_cat, item_tfms=Resize(224)
)
learn = cnn_learner(dls, resnet34, metrics=error_rate)
learn.file_tune(1)