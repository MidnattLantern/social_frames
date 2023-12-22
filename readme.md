Social Frames (alias "Beta Frames"), was advised by Emma Fyrmark, a screen writer within the animation industry for insight. We created issues that makes up a long wish list of useful features an animation team would valuate, then we tagged the most crucial features as "must have", and put on a project board. The other issues were tagged as "feature request".

Cloudyboard is a create, read, update, delete ("CRUD") platform targeted for animation teams. The animation team share a team account, where directors can create metadata for projects, episodes and scenes, and where animators can upload sketches. This enable the team to work remotely.

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

there's a csrf token for each for security {% csrf_token %}

During earlt staes, there's no styling. This was because functionality had to take more priority than form.

During early stages, there were no director and artist and spectator's role. This was because at that stage, it's only relevant to make sure every content is able to be rendered.

Making changes to models, specifically if outdated items need to be removed, it may be neccessary to delete every migration and to reset the datbase at ElephantSQL. Although it's highly recomended to make one before writing the code, Social Frames didn't have any predetermined model for items beforehand. This deletion and reset process was discovered the hard way.

The sites initially rendered as functions, but was replaced with classes

Inputs for adding and editing items are handled with crispy forms

Cloudyboard use Pillow to handle sketch uploading and Cloudinary to store the sketches


Features
======

Sketch View
------
- The user can name and rename their images.
- The user can credit themselves but not edit it.
- The user can upload JP(E)G or PNG maximum of 1 MB. Storyboard artists in the animation industry never need high resolution images, so to prevent massive unneccessary storage space, Cloudyboard will check the image and reject if the file is bigger than 1 MB. Cloudyboard reckon that people within the industry have the tools and know how to resize JP(E)Gs and PNGs.
- What if you create a new sketch with the same name as an existing? Cloudyboard use `IntegrityError` to prevent duplicate slugs.

Scene View
------
- Scene is a CRUD page, views.py use if statements for the C, U, and D to know which of these action they want to perform. for example: `if 'add_episode' in request.POST:` without this if statement, the scene view could create a duplicate item when the user intend to rename a scene.

Technical debt
======
- Being my first time working with Django, I'm not familiar with what strings and blocks of code will eventually bite me in the tail. There are some mistakes I did spot but couldn't adress due to a deadline.
- Project view as ´index.html´: Cloudyboard doesn't have a 'lounge' or 'home page', as it's deseigned to not have one. the Cloudyboard logo and index.html will lead to Project view as the default. If a 'lounge' or 'home' page should be introduced in the future, you'd first need to change the entire relationship to the project view.
- The authorisation system is built upon a user filter. This means that unauthorised users with an URL-link to any stranger's item aren't kicked out, the items are just not visible.