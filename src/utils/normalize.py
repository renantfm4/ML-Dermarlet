import os
import numpy as np
from PIL import Image
from sklearn.preprocessing import LabelEncoder

def normalization(input_folder, output_folder, normal_folder, image_size=(224, 224)):
    """
    Pré-processa as imagens de uma pasta:
    - Redimensiona para image_size (224x224 no caso)
    - Normaliza os pixels (0 a 1) e salva em 'normal_folder'
    - Salva imagens pre-processadas como uint8 em 'output_folder'
    - Aplica LabelEncoder nos rótulos (nomes das subpastas que indicam a categoria da lesão)
    """
    # categorias (nomes das subpastas)
    labels = [label for label in os.listdir(input_folder) if os.path.isdir(os.path.join(input_folder, label))]

    label_encoder = LabelEncoder()
    label_encoded = label_encoder.fit_transform(labels)
    label_map = dict(zip(labels, label_encoded))  # dictionario: {nome_da_pasta: número}

    print("\n--> Mapeamento de Labels/categorias:")
    for label, num in label_map.items():
        print(f"{label} -> {num}")

    for label_name in labels:
        label_path = os.path.join(input_folder, label_name)

        # cria pastas para as categorias, tanto para as imagens processadas quanto para as normalizadas
        output_label_path = os.path.join(output_folder, label_name)
        normal_label_path = os.path.join(normal_folder, label_name)

        os.makedirs(output_label_path, exist_ok=True)
        os.makedirs(normal_label_path, exist_ok=True)

        print(f"\n--> Processando categoria: {label_name} (Label: {label_map[label_name]})")

        for file_name in os.listdir(label_path):
            file_path = os.path.join(label_path, file_name)

            try:
                with Image.open(file_path) as img:
                    img = img.convert('RGB')
                    img = img.resize(image_size)
                    img_array = np.array(img) / 255.0  # normaliza fazendo divisão por 255

                    # salva a versão normalizada em (.npy)
                    npy_path = os.path.join(normal_label_path, file_name.split('.')[0] + ".npy")
                    np.save(npy_path, img_array)  # Salvando como array NumPy

                    # converte para uint8 e salvar a imagem já processada
                    img_array_uint8 = (img_array * 255).astype(np.uint8)
                    img_processed = Image.fromarray(img_array_uint8)

                    output_file_path = os.path.join(output_label_path, file_name)
                    img_processed.save(output_file_path)

            except Exception as e:
                print(f"Erro ao processar {file_path}: {e}")

    print("\nTodas as imagens foram processadas e salvas!")

# teste da normalização, passando a pasta Train como exemplo e criando novas pastas para as imagens processadas (processedTrain) e normalizadas (normalTrain)
if __name__ == "__main__":
    input_folder = "data/Train"
    output_folder = "data/processedTrain"
    normal_folder = "data/normalTrain"

    normalization(input_folder, output_folder, normal_folder)