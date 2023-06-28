
import os
import json
from collections import defaultdict
from PIL import Image

def count_pixels(image_path, json_file):
    # Charger l'image
    image = Image.open(image_path)

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
folder_path = "/Users/maxime.pariente/Downloads/small_dataset/semantic/677d5238-e36b-41a4-bd38-e85a0f95f285_result/ENSTA_Paris/envoie_playement/Anthony-Blr/left"
json_path = "/Users/maxime.pariente/Downloads/small_dataset/semantic/677d5238-e36b-41a4-bd38-e85a0f95f285_result/ENSTA_Paris/envoie_playement/Anthony-Blr/Left/t_1621535652_3.png.json"
png_files = [file for file in os.listdir(folder_path) if file.endswith('.png')]

L=[]
# Parcourir chaque fichier PNG et compter les pixels par couleur
for png_file in png_files:
    X=[]
    png_file_path = os.path.join(folder_path, png_file)
    result = count_pixels(png_file_path, json_path)

    # Afficher le nombre de pixels par couleur pour chaque fichier PNG
    #print(f"Fichier : {png_file}")
    X.append(f"Fichier : {png_file}")
    for class_name, count in result.items():
        #print(f"{class_name}: {count} pixels")
        X.append(f"{class_name}: {count} pixels")   
    L.append(X)
    #print()
    print(L)
#print(L)
