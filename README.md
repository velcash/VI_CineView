# VI_CineView

# Comment mettre en place le projet

Actuellement, uniquement valable pour MacOS ou Linux.

* Installer sqlite3
* pip install -r requirements.txt
* /bin/bash prepare_env.sh
* cd backend/
* python Database.py
* . venv/bin/activate
* ./bootstrap.sh
* Dans un autre terminale
* cd frontend/
* . env/bin/activate
* cd cine_view
* npm run serve

# Sujet

* Présenter les corrélations entre le budget, les origines, le classement 
(au box-office) et les récompenses (les plus prestigieuses)

# Intentions

* Les films recevants des récompenses sont-ils dans une bonne ne place au box office?
* Le genre a-t-il une importance pour recevoir une récompense?
* Le budget a-t-il une importance pour le classement au box office ou pour une récompense?
* Y-a-t-il des surprises (des anomalies)?

# Justification du choix de la représentation

## Représentation graphique
Pour mettre en évidence les rapports qui peuvent y avoir entre le boxOffice , le budget et les récompenses, on a choisit deux représentations:
- le Bar Chart horizontal
- le pie Chart  

L'idéal c'est de représenter toute l'information sur un seul graphique mais pour  assurer de mettre en oeuvre: "le seeking Mantra: overview first ",on aimerait que l'utilisateur aperçoit tout de suite les informations qu'on aimerait communiquer: Le fait d'avoir investit  sur un budget garanti-t-elle une bonne classement au box-office? ou bien l'attribution d'une récompense. Le genre a-t-il un impact au classement du box-office et à l'attribution de récompense. Etre mieux classé au box-office est -il garant d'une récompense?
Alors  la relation box-office, budget et récompense, sera évidente sur le Bar Chart, mais même si on représente le genre sur ce graphique avec despictogrammes, on ne pourrait pas tout de suite voir  la contribution du genre d'ou la nécéssité du pie Chart.
### 1. Bar Chart horizontale  
Le bar Chart est composé de deux axes, et de barres.
l'axe des ordonnées avec le rang dépendant de l'ordre que l'utilisateur , l'axe des abcisses représente le montant en dollars.
- Cette représentation nous paraît la plus appropriée à ce que nous on aimerait démontrer, car elle nous permet de comparer  deux features: le budget et le revenu en jouant sur la saturation de couleur pour faire la distinction entre l'un de l'autre.
- Sur chaque barre on affiche par des pictogrammes le genre auquel appartient le film. On a choisit le pictogramme car c'est ce qui parle le mieux pour indiquer le genre de film et que si on choisit la couleur, on aurait un problème pour les daltoniens.
-A côté de chaque barre on a mis un pictogramme indiquant la nature de récompense oscar ou palme d'or si le film indiqué en a reçu, le pictogramme correspond à l'image du trophée pour chaque récompense rien de mieux pour les représenter.

### 2. Graphique en secteur
On a choisit ce graphique, pour mettre en évidence le rôle du genre dans ce qu'on veut montrer pour le graphique Bar Chart.
On pourrait toute de suite voir la proportion de chaque genre qu'on représente avec une couleur en plus du pictogramme puisqu'il est déconseillé de coder une information sur la base seulement d'une couleur.
## Interaction
### 1. Sur le Bar Chart
Pour toujours assurer de mettre en oeuvre le "Seeking Mantra overview first, zoom and filter , detail on demand" on a ajouté de l'intéraction à notre représentation.  
-On donne à l'utilisateur la possibilité  d' obtenir plus d'information au survol de la souris sur chaque barre avec un zoom et l'apparition des informations sur le film telles :l' année de production, le montant du budget alloué, le montant du revenu généré, le genre et les récompenses obtenues.    
-On ajoute la possibilité de contrôler l'affichage  
  -  en réduisant ou en agrandissant la plage d'années ou de visualisation avec un slider.  
  -  en sélectionnant l'ordre d'affichage: selon budget décroissant ou croissant, selon le revenu croissant ou décroissant


### 2. Interaction globale
On leur permet également de choisir et de limiter la visualisation à une information précise:  
  -  L'affichage des films en se basant sur le box boxOffice et budget, c'est l'affichage par défaut.     
  -  L'affichage des films  sur la base des récompenses.   

-On leur donne la possibilité de filtrer l'affichage des films selon leur zones géographiques:
       on a choisit l'Europe et les Etats-Unis puis le reste par autres, car les films viennent majoritairement de ces deux grandes zones.

### 3. Interaction sur le diagramme en camembert     
Sur le diagramme en camembert, à part le zooming au survol de la souris, qui permet d'avoir le détail sur le genre indiqué par chaque secteur ainsi que son pourcentage de participation à l'information visualisée par l'utilisateur .
L'affichage des proportions varie en fonction de ce que l'utilisateur a sélectionné comme information à afficher via les filtres. 


# Implementation technique

Techniquement, nous avons un backend en python3 avec les données dans une DB SQLite.
La communication se fait avec le framework flask.
Concernant, la vue, elle est faite avec VueJS. Pour les chartes, nous utilisons la lib __ChartJS__ et le slider 
vient de la lib __vue-slider__.

La gestion des filtres se font au travers des requêtes SQL composées à partir des informations de la vue. Puis, nous 
parsons le résultat afin d'afficher ce qui est nécessaire dans chaque graphe.

# Sketches

TODO