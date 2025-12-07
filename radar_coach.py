import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.image as mpimg
import numpy as np

# — Coach Info —
coach_name = "Hansi Flick"
coach_age = 60
team_name = "FC Barcelona"
season = "2024/25"
structure_offensive = "3-2-5"
structure_defensive = "4-4-2 mid-block"
image_path = r"C:\Users\MEVENGUE Franck\Desktop\Projet code Perso\Radar Coach football\Images\Hansi_Flick.jpg"  # ← adapte à ton image locale si besoin

# — Données tactiques —
categories = {
    "Formes de jeu": {
        "Positionnalisme": 70, "Relationnisme": 80,
        "Fonctionnalisme": 75, "Jeu d’approche": 50
    },
    "Défense organisée": {
        "Compacité défensive": 85, "Marquage": 80,
        "Ligne défensive": 85, "Couverture axiale": 80
    },
    "Pressing": {
        "Intensité pressing": 88,
        "Déclencheurs pressing": 85,
        "Rest-défense": 78,
        "Orientation pressing": 82,
        "Contre-pressing": 90
    },
    "Transitions défensives": {
        "Temps de repli": 80,
        "Contrôle du 2e ballon": 68,
        "Agressivité immédiate": 85,
        "Adaptation": 80,
        "Temporisation": 75
    },
    "Construction du jeu": {
        "Relance courte": 88,
        "Sortie sous pression": 85,
        "Progression par passes": 90,
        "Gardien impliqué": 78
    }
}

colors_map = {
    "Formes de jeu": "#1f77b4",
    "Défense organisée": "#2ca02c",
    "Pressing": "#ff7f0e",
    "Transitions défensives": "#d62728",
    "Construction du jeu": "#8e44ad"
}

# — Aplatir les données —
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

# — Figure —
fig = plt.figure(figsize=(12, 10))
fig.patch.set_facecolor('#F0EEE9')

# Titre principal
fig.suptitle(coach_name, fontsize=24, fontweight='bold', y=0.98)
fig.text(0.5, 0.92,
         f"Âge : {coach_age}   |   {team_name}   |   Saison {season}",
         ha='center', fontsize=12)

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

# Sous-titre centré sous le titre
fig.text(
    0.5, 0.90,
    f"Structure offensive : {structure_offensive}   |   Structure défensive : {structure_defensive}",
    fontsize=9, color='gray', fontstyle='italic', ha='center'
)

# — Image du coach —
img = mpimg.imread(image_path)
ax_img = fig.add_axes([0.15, 0.82, 0.20, 0.15])
ax_img.imshow(img)
ax_img.axis('off')

# — Légende à droite —
patches = [mpatches.Patch(color=col, label=cat) for cat, col in colors_map.items()]
ax_leg = fig.add_axes([0.70, 0.77, 0.15, 0.2])
ax_leg.axis('off')
ax_leg.legend(handles=patches, loc='upper left', frameon=False, fontsize=12)

# — Bas de page —
fig.text(0.5, 0.02,
         "Radar tactique – Profil basé sur formes de jeu, phases défensives, pressing et transitions",
         ha='center', fontsize=12, style='italic')

plt.show()
