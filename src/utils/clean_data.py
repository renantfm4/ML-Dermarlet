"""
Módulo responsável por limpar os dados de entrada, removendo imagens duplicadas e inválidas.
"""
import os
import imghdr
from PIL import Image
import hashlib

PATH_DIR = "./data"
hashes = {}

report = {
    'imagens_corrompidas': [],
    'imagens_duplicadas': [],
    'total_imagens_verificadas': 0,
    'total_imagens_removidas': 0
}

def is_valid_image(path):
    """
    Verifica se o arquivo é uma imagem válida.
    Tenta abrir a imagem com PIL e verificar seu formato.

    Args:
        path (str): Caminho para o arquivo de imagem.
    Returns:
        bool: True se o arquivo for uma imagem válida, False caso contrário.
    """
    try:
        if imghdr.what(path) is None:
            return False
        with Image.open(path) as img:
            img.verify()
        return True
    except Exception:
        return False

# Função geradora de hash pra verificar imagens duplicadas
def generate_hash(path):
    """
    Gera um hash SHA-256 para o arquivo de imagem especificado.

    Args:
        path (str): Caminho para o arquivo de imagem.
    Returns:
        str: O hash SHA-256 do arquivo.
    """
    hasher = hashlib.sha256()
    with open(path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def clean_directory(root_dir):
    """
    Limpa o diretório de imagens, removendo imagens duplicadas
    e inválidas. Atualiza o relatório com as imagens removidas.
    
    Args:
        root_dir (str): Caminho para o diretório raiz contendo as imagens.
    Returns:
        None
    """
    for split in ['Train', 'Test']:
        split_path = os.path.join(root_dir, split)
        for label in os.listdir(split_path):
            label_path = os.path.join(split_path, label)
            if not os.path.isdir(label_path):
                continue
            for filename in os.listdir(label_path):
                file_path = os.path.join(label_path, filename)
                report['total_imagens_verificadas'] += 1
                
                if not is_valid_image(file_path):
                    report['imagens_corrompidas'].append(file_path)
                    os.remove(file_path)
                    report['total_imagens_removidas'] += 1
                    continue

                filehash = generate_hash(file_path)
                if filehash in hashes:
                    report['imagens_duplicadas'].append(file_path)
                    os.remove(file_path)
                    report['total_imagens_removidas'] += 1
                else:
                    hashes[filehash] = file_path
