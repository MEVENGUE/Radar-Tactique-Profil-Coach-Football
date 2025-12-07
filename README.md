# 📊 Radar Tactique – Profil Coach Football

Ce projet génère un **diagramme radar tactique** pour représenter le **profil d'un entraîneur de football** selon différents axes tactiques. Il permet aux analystes, recruteurs ou passionnés de mieux comprendre **les préférences de jeu, la philosophie défensive et la construction offensive** d’un coach.

---

## 🧠 Objectif

Le but est de **visualiser le profil tactique d’un entraîneur** de manière claire, synthétique et esthétique, à partir de **5 grands axes tactiques** décomposés en sous-facteurs.

---

## 📌 Facteurs analysés

Le radar repose sur 5 catégories principales (chaque axe est noté sur 100) :

### 1. 🔵 Formes de jeu
Représente la philosophie dominante :
- **Positionnalisme** (occupation rationnelle de l’espace, jeu par zones)
- **Relationnisme** (logique de relations entre joueurs, connexions libres)
- **Fonctionnalisme** (fonctions définies, adaptation au contexte)
- **Jeu d’approche** (logique brésilienne, progression intuitive)

👉 *Sources* :  
- https://medium.com/@stirlingj1982/what-is-relationism-c98d6233d9c2  
- https://medium.com/@stirlingj1982/the-positionist-5af49c787cb0  
- https://jogofuncional1.blogspot.com/2024/11/removing-5-fixed-lanes-of-positional.html  
- https://lapelotasiempreal10.com/reflexiones/el-juego-de-aproximacion-las-raices-del-futbol-brasilero/

---

### 2. 🟢 Défense organisée
Comment l’équipe défend en bloc :
- Marquage zonal
- Ligne défensive haute/basse
- Couverture axiale
- Densité défensive
- Capacité à bloquer l’adversaire

👉 *Source :*  
https://spielverlagerung.de/2025/06/04/defensive-gewinnt-spiele-offensive-gewinnt-titel-mh/

---

### 3. 🟠 Pressing
Capacité à presser collectivement :
- Déclencheurs de pressing
- Orientation du pressing
- Intensité globale
- Rest-défense (sécurité en cas d’échec du pressing)

👉 *Source :*  
https://learning.coachesvoice.com/cv/chelsea-liverpool-tactics-may-2025/

---

### 4. 🔴 Transitions défensives
Réactions à la perte de balle :
- Contrôle du ballon
- Temps de repli
- Agressivité immédiate ou temporisation

---

### 5. 🟣 Construction du jeu
Capacité à construire depuis l’arrière :
- Relance courte
- Sortie sous pression
- Progression par passes
- Implication du gardien

👉 *Source :*  
https://spielverlagerung.de/2025/07/08/aspektanalyse-ballbesitzspiel-des-fc-chelsea-vr/

---

## 🖼️ Exemples de coaches disponibles

Le projet inclut des images pour les coaches suivants :

<div align="center">

### Coaches disponibles

| Coach | Image |
|-------|-------|
| **Antonio Conte** | ![Antonio Conte](./Output/Antonio_Conte.jpg) |
| **Mikel Arteta** | ![Mikel Arteta](./Output/Arteta.jpg) |
| **Roberto De Zerbi** | ![Roberto De Zerbi](./Output/de_zerbi.jpg) |
| **Pep Guardiola** | ![Pep Guardiola](./Output/guardiola.jpg) |
| **Hansi Flick** | ![Hansi Flick](./Output/Hansi_Flick.jpg) |
| **Simone Inzaghi** | ![Simone Inzaghi](./Output/inzaghi.jpg) |
| **Jurgen Klopp** | ![Jurgen Klopp](./Output/Jurgen_Klopp.jpg) |
| **Luis Enrique** | ![Luis Enrique](./Output/Luiz_Enrique.jpg) |
| **Thomas Frank** | ![Thomas Frank](./Output/Thomas_frank.jpg) |
| **Will Still** | ![Will Still](./Output/Will_Still.jpg) |
| **Xabi Alonso** | ![Xabi Alonso](./Output/Xabi_Alonso.jpg) |
| **Xavi Hernandez** | ![Xavi Hernandez](./Output/Xavi_Hernandez.jpg) |

</div>

---

## 🚀 Installation

### 1. Cloner le projet
```bash
git clone https://github.com/MEVENGUE/Radar-Tactique-Profil-Coach-Football.git
cd Radar-Tactique-Profil-Coach-Football
```

### 2. Installer les dépendances
```bash
pip install matplotlib numpy
```

## ✍️ Personnalisation

Modifie les valeurs dans le script Python (labels, scores, coach_name, etc.) pour créer le radar de n’importe quel entraîneur.

Tu peux également :

ajouter l’image du coach depuis Wikipédia (image_path)

ajuster les couleurs ou le style

## 📚 Ressources supplémentaires :

*Source :* 

https://spielverlagerung.de/

https://learning.coachesvoice.com/

https://medium.com/@stirlingj1982

https://www.coachingthecoaches.net/


## 🧩 Auteurs et Contributeurs

Créé par Franck MEVENGUE pour le projet personnel d’analyse tactique.
Contributions bienvenues pour enrichir les styles, facteurs, ou automatiser la génération.
