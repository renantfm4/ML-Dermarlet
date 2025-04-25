import os
from glob import glob

BASE_DIR = "data"

def get_images_by_split(split):
    """
    Retorna todas as imagens do split especificado (Train ou Test).
    """
    path = os.path.join(BASE_DIR, split)
    images = glob(os.path.join(path, '*', '*')) 
    return images

def get_images_by_disease(disease, split=None):
    """
    Retorna todas as imagens de uma doença específica.
    Se 'split' for fornecido, retorna apenas daquele split (Train ou Test).
    """
    if split:
        path = os.path.join(BASE_DIR, split, disease)
        return glob(os.path.join(path, '*'))
    else:
       
        train_path = os.path.join(BASE_DIR, 'Train', disease)
        test_path = os.path.join(BASE_DIR, 'Test', disease)
        return glob(os.path.join(train_path, '*')) + glob(os.path.join(test_path, '*'))
