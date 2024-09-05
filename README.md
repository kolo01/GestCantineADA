# Lancement de mon application
****

**Creer un dossier pour contenir tout notre travail**



> Creer son environnement virtuel avec 
       `python -m venv env`
        
        
> Activer son environnement virtuel
    `.\env\Scripts\activate`
    
> Installer Django
    `pip install django`
    
> Creer son projet
    `django-admin.exe startproject nom_du_projet`
    
> Modifier le nom du dossier de notre projet 
      `  mv .\nom_du_projet\  src`
        
> Telecharger le projet avec 
     `git clone https://github.com/kolo01/projectmodule1.git`

>  Deplacer les elements provenant du repository (les elements recuperer à l'etape precedente) dans le dossier du project renommée src

> toujours avec l'environnement activé, nous installons les dependances en faisant 
    ` pip install -r le_chemin_vers_le_fichier_requirements.txt` (en fonction de la ou vous vous trouvez dans l'arborescence)
    
> On va dans notre SGBD et on crée la base de donnée 
`cantine_db`

> on lance nos migrations avec 
    `python manage.py makemigrations`
    `python manage.py migrate`

> on lance notre projet 
    `python manage.py runserver`
    
> on va dans le navigateur et on tape : 
    `http://127.0.0.1:8000/`


         

