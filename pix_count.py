import os
import json
from collections import defaultdict
from PIL import Image
import torch

# Définir le modèle pour une utilisation sur GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def count_pixels(image_path, json_file):
    # Charger l'image et transférer sur le GPU
    image = Image.open(image_path).to(device)

    # Charger le fichier JSON des associations de couleur et de classe
    with open(json_file) as file:
        color_classes = json.load(file)

    # Créer un dictionnaire par défaut pour stocker le nombre de pixels par classe
    class_counts = defaultdict(int)

    # Parcourir chaque pixel de l'image
    width, height = image.size
    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            hex_color = '#{:02x}{:02x}{:02x}'.format(*pixel)

            # Vérifier si le code couleur a une classe associée dans le fichier JSON
            if hex_color in color_classes:
                class_name = color_classes[hex_color]
                class_counts[class_name] += 1

    # Retourner le dictionnaire des comptes de pixels par classe
    return class_counts


# Parcourir le dossier contenant les fichiers PNG
folder_path = "/home/poc2014/dataset/temp/INFRA10/semantic_segmentation_truth/train/Anthony-Blr"
json_path = "t_1621535652_3.png.json"
png_files = [file for file in os.listdir(folder_path) if file.endswith('.png')]

# Ouvrir le fichier de sortie en mode écriture
with open("pixcnt_Anthony-Blr.txt", 'w') as f:
    # Parcourir chaque fichier PNG et compter les pixels par couleur
    for png_file in png_files:
        X = []
        png_file_path = os.path.join(folder_path, png_file)
        result = count_pixels(png_file_path, json_path)

        # Écrire le nombre de pixels par couleur dans le fichier de sortie
        f.write(f"Fichier : {png_file}\n")
        for class_name, count in result.items():
            f.write(f"{class_name}: {count} pixels\n")
        f.write('\n')
