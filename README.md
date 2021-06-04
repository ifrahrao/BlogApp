# BlogApp
This is a blog app where you can post blogs and also comment on that.

#How to use
Clone This Project (Make Sure You Have Git Installed)
 ```
git clone https://github.com/ifrahrao/BlogApp.git 
```

Install Dependencies using environment yml file
```
conda env create -f environment. yml
```

Activate Environment 
```
conda activate blog_app
```

Go to folder where project located then set database
```
python manage.py makemigrations
python manage.py migrate
```

Create Superuser
```
python manage.py createsuperuser
```
After all these steps , you can start testing this project.
