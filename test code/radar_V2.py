import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.image as mpimg
import numpy as np
import pandas as pd
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# === Chargement des données depuis Excel ===
excel_path = r"C:\Users\MEVENGUE Franck\Desktop\Projet code Perso\Radar Coach football\test code\Fichier Excel\Profil_Tactique_Arteta_2024-2025.xlsx"
df = pd.read_excel(excel_path, index_col=0)

# === Coach Info ===
coach_name = df.loc["coach_name", "Valeur"]
coach_age = int(df.loc["coach_age", "Valeur"])
team_name = df.loc["team_name", "Valeur"]
season = df.loc["season", "Valeur"]
image_path = df.loc["image_path", "Valeur"]
structure_offensive = df.loc["structure_offensive", "Valeur"]
structure_defensive = df.loc["structure_defensive", "Valeur"]

# === Données tactiques ===
categories = {
    "Formes de jeu": {
        "Positionnalisme": df.loc["Positionnalisme", "Valeur"],
        "Relationnisme": df.loc["Relationnisme", "Valeur"],
        "Fonctionnalisme": df.loc["Fonctionnalisme", "Valeur"],
        "Jeu d’approche": df.loc["Jeu d’approche", "Valeur"]
    },
    "Défense organisée": {
        "Compacité défensive": df.loc["Compacité défensive", "Valeur"],
        "Marquage": df.loc["Marquage zonal", "Valeur"],
        "Ligne défensive": df.loc["Ligne défensive", "Valeur"],
        "Couverture axiale": df.loc["Couverture axiale", "Valeur"]
    },
    "Pressing": {
        "Intensité pressing": df.loc["Intensité pressing", "Valeur"],
        "Déclencheurs pressing": df.loc["Déclencheurs pressing", "Valeur"],
        "Rest-défense": df.loc["Rest-défense", "Valeur"],
        "Orientation pressing": df.loc["Orientation pressing", "Valeur"],
        "Contre-pressing": df.loc["Contre-pressing", "Valeur"]
    },
    "Transitions défensives": {
        "Temps de repli": df.loc["Temps de repli", "Valeur"],
        "Contrôle du 2e ballon": df.loc["Contrôle du 2e ballon", "Valeur"],
        "Agressivité immédiate": df.loc["Agressivité immédiate", "Valeur"],
        "Temporisation": df.loc["Temporisation", "Valeur"],
        "Adaptation": df.loc["Adaptation adversaire", "Valeur"]
    },
    "Construction du jeu": {
        "Relance courte": df.loc["Relance courte", "Valeur"],
        "Sortie sous pression": df.loc["Sortie sous pression", "Valeur"],
        "Progression par passes": df.loc["Progression par passes", "Valeur"],
        "Gardien impliqué": df.loc["Gardien impliqué", "Valeur"]
    }
}

colors_map = {
    "Formes de jeu": "#1f77b4",
    "Défense organisée": "#2ca02c",
    "Pressing": "#ff7f0e",
    "Transitions défensives": "#d62728",
    "Construction du jeu": "#8e44ad"
}

# Aplatir les données
labels, values, colors = [], [], []
for cat, subs in categories.items():
    for name, val in subs.items():
        labels.append(name)
        values.append(val)
        colors.append(colors_map[cat])

# Fermer le radar avec la première valeur
values.append(values[0])
colors.append(colors[0])
angles = np.linspace(0, 2 * np.pi, len(values), endpoint=True)

# === Figure ===
fig = plt.figure(figsize=(12, 10))
fig.patch.set_facecolor('#F0EEE9')

# Titre principal
fig.suptitle(coach_name, fontsize=24, fontweight='bold', y=0.98)
fig.text(0.5, 0.92,
         f"Âge : {coach_age}   |   {team_name}   |   Saison {season}",
         ha='center', fontsize=12)

# Sous-titre avec structures
fig.text(
    0.5, 0.90,
    f"Structure offensive : {structure_offensive}   |   Structure défensive : {structure_defensive}",
    ha='center',
    fontsize=9,
    color='gray',
    fontstyle='italic'
)

# Radar central
ax = fig.add_axes([0.06, 0.10, 0.90, 0.75], polar=True)
ax.plot(angles, values, color='black', linewidth=1.5)
ax.fill(angles, values, color='lightgrey', alpha=0.3)

for i in range(len(values) - 1):
    ax.bar(angles[i], values[i], width=0.32, color=colors[i], edgecolor='black', alpha=0.9)

# Étiquettes tactiques
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=9, rotation=15, color='#222222',
                   fontweight='bold', fontname='DejaVu Sans')
ax.set_yticks([20, 40, 60, 80, 100])
ax.set_yticklabels(['20', '40', '60', '80', '100'], fontsize=8, color='black')
ax.set_rlabel_position(0)

# Image du coach
img = mpimg.imread(image_path)
ax_img = fig.add_axes([0.14, 0.82, 0.20, 0.15])
ax_img.imshow(img)
ax_img.axis('off')

# Légende
patches = [mpatches.Patch(color=col, label=cat) for cat, col in colors_map.items()]
ax_leg = fig.add_axes([0.70, 0.77, 0.15, 0.2])
ax_leg.axis('off')
ax_leg.legend(handles=patches, loc='upper left', frameon=False, fontsize=12)

# Pied de page
fig.text(0.5, 0.02,
         "Radar tactique – Profil basé sur formes de jeu, phases défensives et construction",
         ha='center', fontsize=12, style='italic')

# réseaux sociaux :
img = mpimg.imread(r"C:\Users\MEVENGUE Franck\Desktop\Projet code Perso\Radar Coach football\twitter_icon.png")  # une icône de 32x32 px
imagebox = OffsetImage(img, zoom=0.4)
ab = AnnotationBbox(imagebox, (0.75, 0.023), frameon=False, xycoords='figure fraction')
fig.add_artist(ab)

fig.text(0.755, 0.02, "@zekingdavinci", fontsize=9, color='gray', fontstyle='italic')


plt.show()
