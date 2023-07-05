import os
import json
from collections import defaultdict
from PIL import Image

def count_pixels(image_path, color_classes):
    # Charger l'image
    image = Image.open(image_path)

    # Créer un dictionnaire par défaut pour stocker le nombre de pixels par classe
    class_counts = defaultdict(int)

    # Obtenir les pixels de l'image
    pixels = image.load()

    # Parcourir chaque pixel de l'image
    width, height = image.size
    for x in range(width):
        for y in range(height):
            pixel = pixels[x, y]

            # Vérifier si le pixel est une valeur en niveaux de gris
            if isinstance(pixel, int):
                # Utiliser la valeur du pixel comme clé pour récupérer la classe correspondante
                if pixel in color_classes:
                    class_name = color_classes[pixel]
                    class_counts[class_name] += 1
            else:
                # Convertir le tuple de pixels en une chaîne hexadécimale
                hex_color = '#{:02x}{:02x}{:02x}'.format(*pixel)

                # Vérifier si le code couleur a une classe associée dans le fichier JSON
                if hex_color in color_classes:
                    class_name = color_classes[hex_color]
                    class_counts[class_name] += 1

    # Retourner le dictionnaire des comptes de pixels par classe
    return class_counts


# Parcourir le dossier contenant les fichiers PNG
folder_path = "/home/poc2014/dataset/temp/INFRA10/semantic_segmentation_truth/train/Chaville-Sevre-Viroflay"
json_path = "t_1621535652_3.png.json"
png_files = [file for file in os.listdir(folder_path) if file.endswith('.png') and not file.endswith('labelIds.png')]

# Charger le fichier JSON des associations de couleur et de classe une seule fois
with open(json_path) as file:
    color_classes = json.load(file)

# Ouvrir le fichier de sortie en mode écriture
output_file = "pixcnt_Chaville-Sevre-Viroflay.txt"
with open(output_file, 'w') as f:
    # Parcourir chaque fichier PNG et compter les pixels par couleur
    for png_file in png_files:
        png_file_path = os.path.join(folder_path, png_file)
        result = count_pixels(png_file_path, color_classes)

        # Écrire le nombre de pixels par classe dans le fichier de sortie
        f.write(f"Fichier : {png_file}\n")
        for class_name, count in result.items():
            f.write(f"{class_name}: {count} pixels\n")
        f.write('\n')

print(f"Le traitement est terminé. Les résultats ont été enregistrés dans le fichier '{output_file}'.")
