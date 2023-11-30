Social Frames (alias "Beta Frames"), was advised by Emma Fyrmark, a screen writer within the animation industry for insight. We created issues that makes up a long wish list of useful features an animation team would valuate, then we tagged the most crucial features as "must have", and put on a project board. The other issues were tagged as "feature request".

Social Frames was developed on a Macintosh ("Mac" for short), because some crucial features for development are only available on Linux and MacOS.

Repository setup
------
The repository was accessed from Visual Studio Code ("VS Code" for short). To access the repository from VS Code, one of many ways are following:
1. download the extention: Github,
2. Make sure no file or document is open,
3. On the left sidebar, click "Source Controll", then "Clone repository"
4. At the middle top, click "From Github", then the repository name,
5. Finally, pick a destination inside the Finder.

For security reasons, type in `.DS_Store` to the `.gitignore` file.

Using the terminal in VS Code, the following prompts was entered in the terminal:
------
- `pip3 install 'django<4' gunicorn`
- `pip3 install dj_database_url==0.5.0 psycopg2`
- `pip3 install dj3-cloudinary-storage`
These are libraries that will make the enviroment collaborate with Django and Cloudinary.

- `pip install -r requirements.txt`
Among many things, this prompt generates a text file that will make the enviroment more cohesive on other computers if Social Frames should be maintained by a team.

- `django-admin startproject social_frames .`
- `python3 manage.py startapp storyboard`
These prompts genrates the skeleton setup for Django implimentation.

- `python3 manage.py migrate`
For every new app, it's neccessary to migrate to keep the database up to date.

Cloud service setup:
------
Social frames was setup on Heroku in following steps:
- click "New app"
- Give the app a name, and pick Europe
- Inside the "Settings tab", is where the "config vars" is setup.
- The file "Procfile" and its content is neccessary before deployment.
- Inside the Deploy tab, click "Github" as deployment method.
- In the field, social_frames was entered and selected.
- Click "deploy branch".
Social frames was setup on ElephantSQL in following steps:
- Click "Create new instance".
- Give it a name, as of 27 nov 2023, Social Frames has the "Tiny turtle" plan.
- Click "location", Social Frames use Stockholm as its data center.
- Click "Create instance"
- The link can be found in env.py
Social frames was setup on Cloudinary in following steps:
- Inside the Dashboard tab, there's an API enviroment variable"
- The API key can be found inside env.py

If you're new to Django
------
- Inside `social_frames` folder, there's the `urls.py` folder which will know which html to render html. The html documents are inside the `storyboard folder` inside the `templates` folder.
- First exhibition would be the `urls.py` file.

Technology:
------
- Social frames use Django to handle database
- The account registration and accessibility is handled by Allauth extention
- Social frames is hosted by Heroku
- Social frames is handling its storage on PostgreSQL

Manual testing
------
- `python3 manage.py runserver`
- `control^ + C
This is how Social Frames was tested. the `runserver` prompt open up a server, the `^ + C` close the server, and to access the server, the terminal reveals an address, meaning anyone around the world could technically run Social Frames in this stage if they know the address while it's open.

The deployment on Heroku is done manually, which prevents complications during development between updates.

Some code is fragile with letters, one misplaced `/` can make the service dysfunctional.

Test accounts at urls.py