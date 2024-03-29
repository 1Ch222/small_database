import os
import json
from collections import defaultdict
import torch
from torchvision import transforms
from PIL import Image

def count_pixels(image_path, json_file):
    # Charger l'image en utilisant PyTorch
    image = Image.open(image_path)
    image = transforms.ToTensor()(image)
    image = image.cuda()  # Transférer l'image sur le GPU

    # Charger le fichier JSON des associations de couleur et de classe
    with open(json_file) as file:
        color_classes = json.load(file)

    # Créer un dictionnaire par défaut pour stocker le nombre de pixels par classe
    class_counts = defaultdict(int)

    # Parcourir chaque pixel de l'image
    width, height = image.size(2), image.size(1)
    for x in range(width):
        for y in range(height):
            pixel = image[:, y, x].tolist()
            hex_color = '#{:02x}{:02x}{:02x}'.format(int(pixel[0]*255), int(pixel[1]*255), int(pixel[2]*255))

            # Vérifier si le code couleur a une classe associée dans le fichier JSON
            if hex_color in color_classes:
                class_name = color_classes[hex_color]
                class_counts[class_name] += 1

    # Retourner le dictionnaire des comptes de pixels par classe
    return class_counts


# Parcourir le dossier contenant les fichiers PNG
folder_path = "/home/poc2014/dataset/temp/INFRA10/semantic_segmentation_truth/train/Bièvres"
json_path = "t_1621535652_3.png.json"
output_file = "pixcnt_Bièvres.txt"  # Fichier de sortie pour enregistrer les résultats

png_files = [file for file in os.listdir(folder_path) if file.endswith('.png')]

# Ouvrir le fichier de sortie en mode écriture
with open(output_file, 'w') as f:
    # Parcourir chaque fichier PNG et compter les pixels par couleur
    for png_file in png_files:
        png_file_path = os.path.join(folder_path, png_file)
        with torch.cuda.device(0):  # Utiliser le GPU pour le traitement
            result = count_pixels(png_file_path, json_path)

        # Écrire le nombre de pixels par couleur dans le fichier de sortie
        f.write(f"Fichier : {png_file}\n")
        for class_name, count in result.items():
            f.write(f"{class_name}: {count} pixels\n")
        f.write('\n')

print("Le traitement est terminé. Les résultats ont été enregistrés dans le fichier 'pixel_counts.txt'.")
