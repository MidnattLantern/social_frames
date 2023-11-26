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

- `python3 manage.py runserver`
- `control^ + C
This is how Social Frames was tested. the `runserver` prompt open up a server, the `^ + C` close the server, and to access the server, the terminal reveals an address, meaning anyone around the world could technically run Social Frames in this stage if they know the address while it's open.
