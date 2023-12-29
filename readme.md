1 Cloudyboard version 1.0
======
- Live link: https://social-frames-661ae1751b8d.herokuapp.com/ 
- Github repository: https://github.com/MidnattLantern/social_frames.git 
- Cloudyboard (codenamed "Social Frames”), was advised by Emma Fyrmark, a screenwriter with insight into the animation industry. We created a list of useful features that an animation team would value, prioritized the most crucial ones as "must-haves", and put them on a project board. The other features were tagged as "feature requests". 
- Cloudyboard is a management tool targeted at the indie animation industry to prevent stress by providing a platform where tasks and expectations are clear and concise, especially during the fundamental planning stages. 
- It was originally called “Social Frames” during early development but was later renamed "Cloudyboard". There may still be traces of "Social Frames" left in the source code.
- Cloudyboard is a platform for animation teams that allows them to create, read, update and delete ("CRUD") data. The team shares a team account where directors can create metadata for projects, episodes, and scenes, and animators can upload sketches. This enables the team to work remotely.


2 User stories:
======
There are two primary roles as a "user": the "director", and the "artist/ animator":

- As a director, I can create a project so that every project is divided.
- As a director, I can edit an existing project so that the project details are up to date as the project shifts during production.
- As a director, I can delete any of my project(s) so that the project and all its content are gone.
- As a director, I can create an episode within a project so that my team can manage the project more conveniently.
- As a director, I can edit an existing episode so that the episode details are up to date as the animation project shifts during production.
- As a director, I can delete any episode so that any episode and all its content are gone.
- As a director, I can add scenes within an episode so that my team can manage the project more conveniently.
- As a director, I can edit an existing scene so that the scene details are up to date as the animation project shifts during production.
- As a director, I can add scene notes so that my team agree on what's happening on each scene.
- As a director, I can delete any scene so that a scene and all its content I don't want are gone.
- As an artist, I can upload multiple sketches for each scene so that my director can see all of my suggestions for said scene.
- As an artist, I can edit an existing sketch so that the sketch description is clear and concise as the animation project shifts. This excludes editing anything that can take away my credits.
- As a director, I can comment on each artist's submission so that they can see what I think of their sketch or design.
- As a director or artist, I can delete any of the submitted sketch(es) so that the sketch is gone.
- As a user, I can create an account so that I can access Social Frame's service.
- As a user, I can login with a unique name, email and password so that only I have access to my relevant works and collaborations.
- As a user, I can log out so that the browser session and its content aren't connected to me.


3 Features (user stories)
======
All pages have the Cloudboard logo at the top which is a hyperlink that either redirects the user to the Project-view page or Sign-in page.

Sign-in
------
![image: sign in demostration](https://raw.githubusercontent.com/MidnattLantern/social_frames/main/readme%20images/sign%20in%20demostration.png)
- If the user isn't signed in to a team account, they'll be prompted to this page. 
- `Create a team account` hyperlink that redirects them to another page where they can create a team account.
- Form, where Username and Password are mandatory.
- Sign-in button.

Sign-up
------
![image: signup demostration](https://raw.githubusercontent.com/MidnattLantern/social_frames/main/readme%20images/signup%20demostration.png)
- Hyperlink to go back to the sign-in page.
- Form, Username, and two password fields are mandatory.
- Button to create the team account.

Sign-out
------
![image: signout demostration](https://raw.githubusercontent.com/MidnattLantern/social_frames/main/readme%20images/signout%20demostration.png)
- Window that redirects the user back to Project-view.
- Button upon click that logs you out.

Project view
------
![image: project view demostration.](https://raw.githubusercontent.com/MidnattLantern/social_frames/main/readme%20images/project%20view%20demostration.png)
- A project banner is present at the top of the page, followed by a field reminding the user of the Finder/File Explorer. The field displays `(account-name)/Projects`. Clicking on the team account username redirects the user to the signout page.
- Each project item is separated into its own "squircle" (a rectangle with round corners). Only the projects belonging to the signed-in user are visible. This is achieved by a filter method that checks which team account is signed in.
- Two-thirds of the squircle is a slug hyperlink to the episode view, which reveals episodes belonging to that project. It also displays the name of the project.
- One-third of the squircle is an edit form that allows the user to change the project name.
- The edit form has a delete button that will delete the project and everything inside it, including sketches, scenes, and episodes belonging to that project. Clicking delete won't immediately delete the project. The user must confirm their decision.
- At the bottom of the page, the user can create a new project. The input option is Project-Name. Clicking submit will automatically create a slug field based on the team account's username, using `request=user`, and the given name by using `slugify`.
- Cloudyboard will ensure that the project is only visible to the team account that created it by assigning it to the signed-in user.
- If the name is too long, or there already exists a slug name created by the team account, Cloudyboard will reject the creation. As of version 1.0, there are no error messages if a project fails to be created.
- The project view and all other views are CRUD pages. Views.py uses if statements for the C, U, and D to know which actions to perform. For example, `if 'add_project' in request.POST:`. Without this if statement, the project view could for example create a duplicate item when the user intends to rename a project.

Episode view
------
![image: episode view demostration](https://raw.githubusercontent.com/MidnattLantern/social_frames/main/readme%20images/episode%20view%20demostration.png)
- The Episode view follows a similar model as the Project view. To avoid repetition, only the differences are covered:
- The banner displays the name of the project entered by the user, such as "Episodes for `project name`".
- The Finder/file explorer field shows "(account-name)/Projects/Episodes". By clicking on "Projects", the user will be redirected to the Projects view.
- The episode object's name is accompanied by a chronology number, for example, "Episode: `2`".
- Apart from changing the name of the object, users can edit the chronology of episodes. The episode view lists each episode according to chronology.
- Users can assign a chronology index in addition to naming a new episode.

Scene view
------
![image: scenes overview demostration](https://raw.githubusercontent.com/MidnattLantern/social_frames/main/readme%20images/scenes%20overview%20demostration.png)
![image: scenes detail](https://raw.githubusercontent.com/MidnattLantern/social_frames/main/readme%20images/scenes%20detail.png)
- The scene view follows a similar model as the Project view and Episode view. To avoid repetition, only the differences are covered:
- The banner at the top of the Scene view displays the name of the episode entered by the user: "Scenes for `episode name`".
- The Finder or File Explorer field in the Scene view shows the path to the Scenes folder: `(account-name)/Projects/Episodes/Scenes`.
- In addition to the name and chronology index of each scene, the Scene view also displays scene event notes. These notes can include details about what characters are saying or doing.
- When creating a new scene in the Scene view, the user can choose to add event notes, but it is not a mandatory option. The user can also give the new scene a name and chronology index.

Sketch view
------
![image: sketch upload detail demostration](https://raw.githubusercontent.com/MidnattLantern/social_frames/main/readme%20images/sketch%20upload%20detail%20demostration.png)
![image: sketch overview demostration](https://raw.githubusercontent.com/MidnattLantern/social_frames/main/readme%20images/sketch%20overview%20demostration.png)
![image: sketch item detail demostration](https://raw.githubusercontent.com/MidnattLantern/social_frames/main/readme%20images/sketch%20item%20detail%20demostration.png)
- The Sketch view follows a similar model as the Project view, Episode view and Scene view. To avoid repetition, only the differences are covered. This is the most complex model on Cloudyboard:
- The banner in Sketch view will display the name of the scene that the user has entered, with the text "Sketches for `scene name`".
- The Finder/File Explorer field in Sketch view will show `(account-name)/Projects/Episodes/Scenes/Sketches`.
- Each sketch item will display its name, the artist who made the sketch, the image of the sketch as either JPG or PNG (hosted by Cloudinary), and a comment section. Note that despite their visual similarities, unlike other objects, there are no hyperlinks on these objects.
- The director's comment section in Sketch view is similar to the scene event notes in Episode view that show the scenes. However, in Sketch view, this content is provided after an item is created.
- The edit form in Sketch view only allows the user to change the name of the sketch. Users cannot change the name of the artist or the image itself, to ensure that the artist who submitted the sketch is always credited.
- In addition to editing and deleting, the 1/3 section in Sketch view allows the user to leave or edit a comment for each sketch item.
- The "add sketch" section in Sketch view allows the user to submit a JPG or PNG file, give their sketch a name, and leave their name for crediting purposes. The image and the name of the artist cannot be edited after submission.
- Cloudyboard will reject non-JPG or PNG files and images that are larger than 1MB.


4 Future features:
======
This section covers some items from the wishlist of features me and my advisor left:
- As a user, I can press a button that toggles a rule-of-thirds-grid over a sketch so that I can see how flawed or well-executed the composition is.
- As an artist, I can see scenes my director has assigned me to work on so that I know what my director is expecting from me.
- As a director, I can assign scenes to my artists so that my team knows what I'm expecting from them
- As a user, I can play a slide show for each episode beginning from a marked scene so that I can see in real-time what the timing would be like.
- As a director, I can assign a time duration for each scene in seconds so that my team knows for how long each scene should be playing
- As a director, I can create a character exodus for each project so that my team and spectators can get information about each character.
- As a director, I can pin one sketch for each scene so that my team can agree on what each scene should look like.
- As a director, I can assign a time for each frame, such as day or night so that my team can agree on what's happening in each scene.


5 Typography and colour schemes
======
- Taking inspiration from Finder/File Explorer, Cloudyboard has a minimalistic visual design, where the objects take the spotlight and the tools surrounding them are available.
- Cloudyboard use dark colours for the background: `#1b1b1c` and `#2a2a2b` in contrast with thewhite frames and text: `#fafafa`. Contrary to the convention where the background is white, and the text is black, the decision to go the opposite direction was made to be easier on the eyes. Animators tend to work extremely long hours into the night. White text on a black background is more clear than black text on a white background.
- The theme colour is a soft blue: `#98baff`. As of version 1.0, this colour is only present when the user hovers above any hyperlink.
- The font typography is Raleway, borrowed from Google Fonts. Raleway is a Sans Serif, it's simply slim and easy to read.
- Each object is a row. 2/3:rds is a hyperlink box with information in large text, and 1/3:rd is an edit and delete form with small text.


6 Wireframes
======
![image: UX demostration](https://raw.githubusercontent.com/MidnattLantern/social_frames/main/readme%20images/UX%20demostration.png)
- To draw parallels to something familiar, the organization of Cloudyboard can be compared to that of a familiar app like Finder or File Explorer.
- In this model, sketches are stored within scenes, scenes are stored within episodes, episodes are stored within projects, and projects are stored within a team account. This structure is similar to that of files within a file system.
- To navigate through this structure, you can use the navigation bar located under the header, which shows the path as `team-account/projects/episodes/scenes/sketches`.

![image: slug redirect demostration](https://raw.githubusercontent.com/MidnattLantern/social_frames/main/readme%20images/slug%20redirect%20demostration.png)
- As demonstrated in this wireframe, links to episodes are available in the project-view, links to scenes are available in the episode-view, and links to sketches are available in the scene-view.

![image: partner wireframe 1](https://raw.githubusercontent.com/MidnattLantern/social_frames/main/readme%20images/partner%20wireframe%201.png)
![image: partner wireframe 2](https://raw.githubusercontent.com/MidnattLantern/social_frames/main/readme%20images/partner%20wireframe%202.png)
- Cloudyboard was brainstormed together with someone with industry insight, and the sketches and images represent vague ideas for implementation.
- The UX idea is to ensure that important objects have large font sizes and take up attention. When you hover over them, they light up in soft blue, distinguishing them from the rest of the page.
- The wireframes entertained two layout option ideas: a flex layout with two squares per row or a rectangle occupying an entire row. The decision was made to go with the rectangle layout, as most objects are listed chronologically, ensuring that each row doesn't contain too much information and overwhelm the user. Assuming that users will be viewing the page on a computer, a horizontal layout is appropriate.


7 Technology:
======
- Cloudyboard is run using Django.
- Cloudyboard use ElephantSQL to handle the database.
- The account registration and accessibility are handled by the Allauth extension.
- Cloudyboard is hosted by Heroku.
- The deployment on Heroku is done manually, which will prevent complications during development between updates.
- Cloudyboard use Bootstrap for styling shortcuts, mainly for buttons and the appearance of object items.
- Cloudyboard use Pillow to handle JP(e)G and PNG uploading and Cloudinary to store the sketches
- there's a csrf token for each submission object in HTML for security reasons {% csrf_token %}


8A. Validation Testing:
======
W3 warnings about Flask-related strings/ blocks were ignored. This is because W3 will return `Bad value` errors for legitimate flask strings/ blocks, most commonly `{ is not allowed`. The following HTML has been checked by W3:
------
- scene_view.html (5 Flask-related `bad value` raised)
- project_view.html (3 Flask-related `bad value` raised)
- index.html (4 Flask-related `bad value` raised)
- episode_view.html (4 Flask-related `bad value` raised)
- base.html (2 Flask-related `bad value` raised)
- logout.html (1 Flask-related `bad value` raised)
- logout.html (1 Flask-related `bad value` raised)
- signup.html (1 Flask-related `bad value` raised)

The following CSS have been checked by Jigsaw:
------
- style.css

The validator used for the Python files was the Code Institute Python Linter `https://pep8ci.herokuapp.com/`. There are some exceptions where raised warnings couldn't be solved, but the quality isn't affected. following Python files have been checked:
------
- views.py inside storyboard folder (7 exceptions)
- urls.py inside storyboard folder
- urls.py inside social_frames folder
- models.py inside storyboard folder
- forms.py inside storyboard folder
- admin.py inside storyboard folder


8B. Manual testing
======
- Previously, the paths inside urls.py used static names like `'scene_view/scene'` instead of `'scene_view/<slug:scene_slug>/'` which included slug fields. This was changed to test the correct usage of urls.py files. This step was done to be sure that the urls.py files were being imported and used properly by Django.

- Initially, the sites were created as functions but later replaced with classes.

- When creating a new view, a slug field and username had to be manually entered. This provided greater flexibility in testing the object behaviour, specifically when only a selected number of objects needed to be visible depending on the signed-in account and the view they accessed.

- To verify that a particular object was created and appeared on the page, clicking on the create button was tested. Only project items were rendered inside the project view and the same applied to episode, scene, and sketch items. At this point, every item was visible regardless of the account that was signed in.

- The HTML use `for i loop` to ensure that each item is rendered in a separate window. In the final product, they’re divided into their own squircles.

- Here's something interesting about models.py and PostgreSQL: If you have added models and migrated them in PostgreSQL, but later find that they are unnecessary obstacles or some models are missing, you cannot remove them and migrate again. To solve this issue, delete every migration file inside migration except `__init__.py`, as well as inside `__pycache__`, reset the database on ElephantSQL, and make a fresh migration. Planning models carefully in the planning stage is important for a reason, but this information is good to know in case you discover that some models turn out to be missing or are unnecessary obstacles.

- Filtering was implemented checking for two things: The signed-in user and the object they are browsing in, except in the project view where it only checks for the user.

- Edit any given object to make sure the content gets updated names and values. The edit form doesn't update any fields by default, but by using `cleaned_data.get()` for views.py, a few selected fields could be updated depending on the user's input.

- To delete an object, use the delete button. The Django administration panel confirms that the object is deleted and not just somehow invisible to the user. The first delete button did not have any warning or confirmation popup.

- During development, print lines were used to indicate the actions performed and tested among the create, edit, and delete forms. These were useful when editing an object would also create an object. The print lines are still available in the source code

- There were some issues with creating projects and scenes with the same name in different accounts and episodes. To resolve this, Cloudyboard uses different slug fields to allow for the same name as long as the slug fields are different.

- Once the manual input of slugfield and the animation team worked as expected, automatic input was implemented. By using requests for user and slug fields, and the slug field name for the given name, combining these, Django would create a new slug field and assign it to the signed-in user automatically.

- Inputs for adding and editing objects are handled with crispy forms

- Images larger than 1MB were published to make sure they would be rejected.

- In cases where duplicates were not stopped, they had to be removed using the Django Admin panel to avoid interference with the page and to prevent the return of a Django debug page.


- Invalid cases were handled using `try` and `except(error)` to prevent errors from occurring. The idea was to make sure that nothing happens at all, rather than having a page fail to load forever.

- Most of the CSS styling was implemented after the functionality was stable.

image: responsive demonstration
- Although an animator would never use Cloudyboard on an iPhone or any horizontal screen, it was still designed to look nice on a small iPhone. Responsive design testing was done using the Firefox development tool called Responsive Design Mode (396 x 854). To enter this mode, press Cmd+Opt+M (assuming MacOS is the operating system). After deployment to Heroku, Cloudyboard was accessible outside Codeanywhere and VS code, making it possible to test with a real iPhone.

- The first Heroku deployment had an issue with image uploading, resulting in a 500 error. However, after running a freeze command to update the requirements, it became possible to upload images from the Heroku deployment.

- It is important to note that the `DEBUG` inside settings.py was switched to `False` before the final Heroku deployment. The first Heroku deployments were set to `True` to spot the reason for the image upload 500 error. Interestingly, if `DEBUG` is set to `True`, Heroku won't read the CSS styling file for Cloudyboard.


8C. Fixed bugs (ver 1.0)
======
- As of version 1.0 there are no discovered bugs.
- As Clodyboard keeps evolving in the future, there are risks of bugs occurring.
- There's currently no bug report system in Cloudyboard, but if you discover any, you can report them to my email: isakvent@outlook.com.


8D. Technical debt
======
Being my first time working with Django, I'm not familiar with what strings and blocks of code will eventually bite me in the tail. There are some mistakes I did spot but couldn't address due to a deadline:
- Project view as ´index.html´: Cloudyboard doesn't have a 'lounge' or 'home page', as it's designed to not have one. the Cloudyboard logo and index.html will lead to the Project view as the default. If a 'lounge' or 'home' page should be introduced in the future, you'd first need to change the entire relationship to the project view.
- The authorisation system is built upon a user filter. This means that unauthorised users with a URL link to any stranger's item aren't kicked out, the items are just not visible.
- The CSS `ul>li` styling is currently occupied to satisfy a necessary styling for the sign-up page.
- Their renaming transition isn't fully complete. There may be traces of "social frames" that haven't been renamed due to more important priorities.


9 Deployment
======
- The source code has its repository hosted on Github.
- The live site is hosted by Heroku. Important before deploying to Heroku: it's mandatory to run this in the terminal: `pip3 freeze --local > requirements.txt` so that local requirements are 'on the cloud'.

Repository setup
------
The repository was accessed from Visual Studio Code ("VS Code" for short). To access the repository from VS Code, one of many ways are following:
1. download the extension: Github,
2. Make sure no file or document is open,
3. On the left sidebar, click "Source Control", then "Clone repository"
4. At the middle top, click "From Github", then the repository name,
5. Finally, pick a destination inside the Finder.

For security reasons, type in `.DS_Store` to the `.gitignore` file.

Using the terminal in VS Code, the following prompts were entered in the terminal:
------
- `pip3 install 'django<4' gunicorn`
- `pip3 install dj_database_url==0.5.0 psycopg2`
- `pip3 install dj3-cloudinary-storage`
These are libraries that will make the environment collaborate with Django and Cloudinary.

- `pip install -r requirements.txt`
Among many things, this prompt generates a text file that will make the environment more cohesive on other computers if Cloudyboard is maintained by a team.

- `django-admin startproject social_frames .`
- `python3 manage.py startapp storyboard`
These prompts generate the skeleton setup for Django implementation.

- `python3 manage.py migrate`
For every new app, it's necessary to migrate to keep the database up to date.

Cloud service setup:
------
Cloudyboard was setup on Heroku in the following steps:
- click "New app"
- Give the app a name, and pick Europe
- Inside the "Settings tab", is where the "config vars" is set up.
- The file "Procfile" and its content are necessary before deployment.
- Inside the Deploy tab, click "Github" as the deployment method.
- In the field, social_frames were entered and selected.
- Click "deploy branch".
Cloudyboard was setup on ElephantSQL in the following steps:
- Click "Create new instance".
- Give it a name, as of 27 Nov 2023, Cloudyboard has the "Tiny Turtle" plan.
- Click "location", Cloudyboard use Stockholm as its data center.
- Click "Create instance"
- The link can be found in env.py
Cloudyboard was setup on Cloudinary in the following steps:
- Inside the Dashboard tab, there's an API environment variable"
- The API key can be found inside env.py


10 Credits
======
- The layout is custom-made, with help from Bootstrap 4.
- The font used is Raleway found at Google Fonts.
- Spell and grammar checking for this readme were done using Grammarly
