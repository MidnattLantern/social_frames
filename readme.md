1. Cloudyboard version 1.0
======
- Cloudyboard (alias "Social Frames"), was advised by Emma Fyrmark, a screen writer within the animation industry for insight. We created issues that makes up a long wish list of useful features an animation team would valuate, then we tagged the most crucial features as "must have", and put on a project board. The other issues were tagged as "feature request".

- Cloudyboard is a management tool targeted to the indie animation industry. The intention is to prevent stress by providing a platform where tasks and expectations can be clear and concise within the animation team, specifically during the fundamental planning stages.

- During early development it was called "Social frames" but later renamed to "Cloudyboard". There may still be traces of "Social frames" left in the product.

- Cloudyboard is a create, read, update, delete ("CRUD") platform targeted for animation teams. The animation team share a team account, where directors can create metadata for projects, episodes and scenes, and where animators can upload sketches. This enable the team to work remotely.

2. User stories:
======
There are two primary roles as a "user": the "director", and the "artist/ animator":

- As a director, I can create a project so that each and every project is divided.
- As a director, I can edit an existing project so that the project details are up to date as the project shifts during production.
- As a director, I can delete any of my project(s) so that project and all its content are gone

- As a director, I can create an episode within a project so that my team can manage the project more conveniently
- As a director, I can edit an existing episode so that the episode details are up to date as the animation project shifts during production
- As a director, I can delete any episode so that any episode and all its content are gone

- As a director, I can add scenes within an episode so that my team can manage the project more conveniently
- As a director, I can edit an existing scene so that the scene details are up to date as the animation project shifts during production
- As a director, I can add scene notes so that my team agree on what's happening on each scene
- As a director, I can delete any scene so that a scene and all its content I don't want are gone

- As an artist, I can upload multiple sketches for each scene so that my director can see all of my suggestions for said scene
- As an artist, I can edit an existing sketch so that the sketch description is clear and concise as the animation project shifts. This excludes editing anything that can take away my credits.
- As a director, I can comment each artist's submission so that they can see what I think of their sketch or design
- As a director or artist, I can delete any of the submitted sketch(es) so that the sketch is gone

- As a user, I can create an account so that I can access Social Frame's service
- As a user, I can login with a unique name, email and password so that only I have access to my relevant works and collaborations
- As a user, I can log out so that the browser session and its content isn't connected to me


3. Features (user stories)
======
All pages have the Cloudboard logo at the top that is a hyperlink that either redirects the user to Project-view page or Sign-in page.

Sign-in
------
image: sign in demostration
- If the user isn't signed in to a team account, they'll be prompted to this page. 
- `Create a team account` hyperlink that redirects them to another page where they can create a team account.
- Form, where Username and Password are manditory.
- Sign in button.

Sign-up
------
image: signup demostration
- Hyperlink to go back to the sign-in page.
- Form, Username, and two password fields are manditory.
- Button to create the team account.

Sign-out
------
image: signout demostration
- Window that redirects the user back to Project-view.
- Button upon click that log you out.

Project view
------
image: project view demostration.
- Projects banner and a field below that reminds of Finder/ file explorer: `(account-name)/Projects`, click on the team account username redirects the user to signout page.
- Each project item are seperated for each of their own "squircle" (rectangle with round corners). Only the projects belonging to the user who is signed in are visible, this is acieved by a filter method checking what team-account is signed in.
- 2/3:rds of the squircle is a slug-hyperlink to episode view that reveals episodes belonging to that project. It reveals information about the Project: the name.
- 1/3:rd of the squircle is an edit form. The edit form let you change the project name but not the slug-name.
- The edit form also has a delete button that will delete the project and everything inside of it, including sketches, scenes and episodes. Clicking delete won't imediately delete the project, the user must confirm their decision.
- At the bottom of the page, the user can create a new project. The input option are Project-Name. Clicking submit, Cloudyboard will automatically create a slug-field based on the username of the team account by using `request=user`, and the given name by using `slugify`.
- Cloudybord will also make sure the project is only visible to the team account that created it, by assigning it to the user who is signed in.
- If the name is too long, or there already exist a slug name created by the team account, Cloudyboard will reject the cration. As of version 1.0 there are not error message if a project fail to be created.
- Project view and all the other views are CRUD pages, views.py use if statements for the C, U, and D to know which of these action they want to perform. for example: `if 'add_project' in request.POST:` without this if statement, the project view could create a duplicate item when the user intend to rename a project.

Episode view
------
image: episode view demostration
- Episode view follow a similar model as Project view. To avoid repetition, only the differences are covered:
- The banner will display the name of the project the user entered. "Episodes for `project name`".
- The Finder/ file explorer field says: `(account-name)/Projects/Episodes`, clicking on `Projects` redirects the user to Projects view.
- In addition to the episode object's name, it also show the chronology number, such as "Episode: `2`".
- In addition to be able to edit the name of the object, episodes let you edit the chronology. The episode view will list each episode according to chronology.
- In addition to give a new episode a name, the user can give it a chronology index.

Scene view
------
image: scenes overview demostration
image: scenes detail
- Scene view follow a similar model as Project view and Episode view. To aviod repetition, only the differences are covered:
- The banner will display the name of the episode the user entered. "Scenes for `episode name`".
- The Finder/ file explorer field says: `(account-name)/Projects/Episodes/Scenes`.
- In addition to the scene object's name and chronology index, it also show scene event notes. Such as what a character is saying, or what action a character is doing.
- In addition to give a new scene a name and chronology index, the user can write event notes, this option isn't manditory.

Sketch view
------
image: sketch upload detail demostration
image: sketch overview demostration
image: sketch item detail demostration
- Sketch view follow a similar model as Project view, Episode view and Scene veiw. To aviod repetition, only the differences are covered. This is the most complex model on Cloudyboard:
- The banner will display the name of the scene the user entered. "Sketches for `scene name`".
- The Finder/ file explorer field says: `(account-name)/Projects/Episodes/Scenes/Sketches`.
- Each sketch item show its name, the artist who made the sketch, the sketch as JPG or PNG (hosted by Cloudinary), and a comment section. Despite the visual similarities, there are no hyperlinks on these objects unlike the other objects.
- Director's comment section is similar to scene event notes from episode-view showing the scenes, but this content is provided after an item is created.
- The edit form only let the user change the name of the sketch, but they cannot change the name of the artist, or the image itself, in order to secure the credit of the artist who made the submition.
- In addition to edit and delete, the 1/3 section allow the user to leave or edit a comment for each sketch item.
- The add sketch section let the user submit a JP(e)G or PNG file, give their sketch a name, and leave their name so that they're credited. The image and the name of the artist cannot be edited.
- Cloudyboard will reject non JP(e)G or PNG files, and images that are larger than 1MB.


4. Future features:
======
This section cover some items from the wishlist of features me and my advisor left:
- As a user, I can press a button that toggles a rule-of-thirds-grid over a sketch so that I can see how flawed or well-executed the composition is.
- As an artist, I can see scenes my director have assigned me to work on so that I know what my director is expecting from me.
- As a director, I can assign scenes to my artists so that my team knows what I'm expecting from them
- As a user, I can play a slide-show for each episode beginning from a marked scene so that I can see in real-time what the timing would be like.
- As a director, I can assign a time duration for each scene in seconds so that my team knows for how long each scene should be playing
- As a director, I can create a character exodus for each project so that my team and spectators can get information about each character.
- As a director, I can pin one sketch for each scene so that my team can agree on what each scene should look like.
- As a director, I can assign a time on each frame, such as day or night so that my team can agree on what's happening in each scene.


5. Typography and colour schemes
======
- Taking inspiration from Finder/ file explorer, Cloudyboard has a minimalistic visual design, where the objects take the spotlight and the tools surrounding them are available.
- Cloudyboard use dark colours for the background: `#1b1b1c` and `#2a2a2b` in contrast with thewhite frames and text: `#fafafa`. Contrary to the convention where the background is white, and the text is black, the decision to go the opposite direction was made to be easier on the eyes. Animators tend to work extremely long hours into the night. White text on black background is more clear than black text on white background.
- The theme colour is a soft blue: `#98baff`. As of verison 1.0 this colour is only present when the user hover above any hyperlink.
- The font typography is Raleway, borrowed from Google Fonts. Raleway is a Sans Serif, it's simply slim and easy to read.
- Each object is a row. 2/3:rds is a hyperlink box with information in large text, 1/3:rd is an edit and delete form with small text.


6. Wireframes
======
image: UX demostration
- if the model for cloudyboard were to be demostrated on a familiar app, it would be like on Finder/ file explorer.
- sketcehs goes inside scenes, scenes goes inside episodes, episodes goes inside projects, projects goes inside a team account. And they behave like you'd expect files with this model would.
- Hence, the navigation bar under the header `team-account/projects/episodes/scenes/sketches`

image: slug redirect demostration
- As demostrated in this wireframe, links to episodes are available in the project-view, links to scenes are available in the episode-view, links to sketches are available in the scene-view.

image: partner wireframe 1
image: partner wireframe 2
- Since Cloudyboard was branstormed with someone with insight to the industry, these sketches images show vague ideas on what would be nice to be implimented.
- Obviously, a wishlist is just a wishlist, but the UX idea that items are large and take up attention was agreed on. The important objects have big font sizes. When you hover them, they light up in blue, making them stick out from the rest of the page.
- The wireframes gave two ideas: should the objects be displayed with a flex layout with two squares for each row, or a rectangle taking up one row each? The answer was the rectangle, since most objects are listed with a chronological order, preventing an over-stimulation of information for each row. Users are expected to be on a computer.


7. Technology:
======
- Cloudyboard is run using Django.
- Cloudyboard use ElephantSQL to handle database.
- The account registration and accessibility is handled by the Allauth extention.
- Cloudyboard is hosted by Heroku.
- The deployment on Heroku is done manually, which will prevent complications during development between updates.
- Cloudyboard use bootstrap for styling shortcuts, mainly for buttons and appearance for object items.
- Cloudyboard use Pillow to handle JP(e)G and PNG uploading and Cloudinary to store the sketches
- there's a csrf token for each submittion object in html for security reasons {% csrf_token %}


8. A. Validation Testing:
======
W3 warnings about Flask related strings/ blocks were ignored. This is because W3 will return `Bad value` errors for legitemate flask strings/ blocks, most commonly `{ is not allwoed`. Following HTML have been checked by W3:
------
- scene_view.html (5 Flask-related `bad value` raised)
- project_view.html (3 Flask-related `bad value` raised)
- index.html (4 Flask-related `bad value` raised)
- episode_view.html (4 Flask-related `bad value` raised)
- base.html (2 Flask-related `bad value` raised)
- logout.html (1 Flask-related `bad value` raised)
- logout.html (1 Flask-related `bad value` raised)
- signup.html (1 Flask-related `bad value` raised)

Following CSS have been checked by Jigsaw:
------
- style.css

The validator used for the Python files were the Code Institute Python Linter `https://pep8ci.herokuapp.com/`. There are some exceptions where raised warnings couldn't be solved, but the quality isn't affected. following Python files have been checked:
------
- views.py inside storyboard folder (7 exceptions)
- urls.py inside storyboard folder
- urls.py inside social_frames folder
- models.py inside storyboard folder
- forms.py inside storyboard folder
- admin.py inside storyboard folder


8. B. Manual testing
======
- Before the paths inside urls.py used slugfields, they had static names, such as `'scene_view/scene'` instead of `'scene_view/<slug:scene_slug>/'`. There were static links to the urls for each view page revealed universally to any user, such as a link to episode view inside project view. This step was done to be sure that the urls.py files are being imported and used properly by Django.

- The sites initially rendered as functions, but was replaced with classes.

- The first creation window for any view required you to manually give it a slug-field and your username. This gave more freedom in testing how the objects would behave, in particular during the stage to make sure that only a few objects are visible depending on who is signed in and what view insdie what object they're inside.

- Clicking create given object were tested to see if that would appear on the page, and only if project items were to be rendered inside project view, the same for episode, scene and sketch items. At this point, every given item is visible regardless what account is signed in.

- HTML use `for i loop` so that all items are rendered as seperate windows.

- Here's somehting interesting about models.py and PostgreSQL: you can add models and migrate them, but you cannot remove models and migrate. There were some models in the planning stage that turned out to be unneccessary obstacels, and other models that appeared to be missing and neccessary. This discovery resulted in fatal errors that made Cloudyboard dysfunctional. The solution that worked for this instance if old models are incomatible with new migrations, are to delete every migration file inside migration EXCEPT `__init__py`, the same for inside __pycache. Then you need to go to ElephantSQL and reset your databse. Finally, you can make a fresh migration. Planning models carefully in the planning stage is important for a reason, but this information is good to know in case you discover that some models turns out to be missing or are uneccessary obstacles.

- Filtering were implimented checking for two things: which user is signed in, and inside what object they're browsing in (but project view only checks for the user). This would make sure that only the relevant objects are visible to the authorsed user.

- Edit any given object to make sure the content get updated names and values. Edit form don't update any fields by default, but by using `cleaned_data.get()` for views.py, a few selected field could update depending on the user's input.

- Delete button for given object to make sure it dissapears from the database. To ensure that it somehow just wasn't invisible to the user, the Djanog administration panel reveal that it's really gone. The first delete button had no warning / confirmation popup.

- There are still print lines to indicate what actions were performed/ teseted among the create, edit, and delete forms during development. These were useful at a strange stage when editing an object would also create an object.

- Two accounts couldn't create a project with the same name, and one account couldn't create two scenes with the same name, even though they're inside different episodes. Using different slug fields solved this, so they can have the same name, as long as the slugfield are different.

- When manual input for slugfield and animation team are entered, it should behave as expected, automatic input for those things were implimented. Using requests for user and slugfields, as well as the slugified name for the given name, combining these, Django would create a new slugfield, and assign it to the signed in user autoamtically.

- Inputs for adding and editing objects are handled with crispy forms

- Images larger than 1MB were published to make sure they would be rejected.

- In invalid cases such as when duplicates weren't stopped, they had to be removed usign the Django Admin panel, as they would interfere with the page and return a Django debug page.

- These invalid cases were handled using `try` and `except(error)` that could occur. They handle errors by making sure nothing happens at all. Better that nothing happens, rather than a page fails to load forever.

- Most CSS styling was implimented after the functionality was stable.

- Although an animator would never be on an iPhone or any horizontal screen, Clodyboard still looks nice on a small iPhone. For CSS styling, testing was made on Firefox development tool Responsive design mode (396 x 854). To enter this mode: press Cmd+Opt+M (assuming MacOS is the operating system). After deployment to Heroku, Cloudyboard was accessible outside Codeanywhere and VS code, so it could be tested with a real iPhone.

- The first Heroku deployment had an issue: image uploading would result in a 500 error. But after performing a freeze command to update the requirements, it became possible to upload images from Heroku deployment.

- This should be going without saying, but it is important: the `DEBUG` inside settings:py was switched to `False` before final Heroku deployment. The first Heroku deployments was set to `True` in order to spot the reason the image upload 500 error would occur. Interestingly, if the debug is set to `True`, Heroku won't read the CSS styling file for Cloudyboard.


8. C. Fixed bugs (ver 1.0)
======
- As of version 1.0 there are no discovered bugs.
- As Clodyboard keeps evolving in the future, there are risks of bugs occuring.
- There's currently no bug report system in Cloudyboard, but if you discover any, you can report them to my email: isakvent@outlook.com .


8. D. Technical debt
======
Being my first time working with Django, I'm not familiar with what strings and blocks of code will eventually bite me in the tail. There are some mistakes I did spot but couldn't adress due to a deadline:
- Project view as ´index.html´: Cloudyboard doesn't have a 'lounge' or 'home page', as it's deseigned to not have one. the Cloudyboard logo and index.html will lead to Project view as the default. If a 'lounge' or 'home' page should be introduced in the future, you'd first need to change the entire relationship to the project view.
- The authorisation system is built upon a user filter. This means that unauthorised users with an URL-link to any stranger's item aren't kicked out, the items are just not visible.
- The CSS `ul>li` styling is currently occupied to satisfy a neccessary styling for the sign-up page.
- There renaming transition isn't fully complete. There may be traces of "social-frames" that hasn't been renamed due to more important priorities.


9. Deployment
======
- The source code has its repository hosted on Github.
- The live site is hosted by Heroku. Important before deploying to heroku: it's manditory to run this in the terminal: `pip3 freeze --local > requirements.txt` so that local requirements are 'on the cloud'.

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
Among many things, this prompt generates a text file that will make the enviroment more cohesive on other computers if Cloudyboard should be maintained by a team.

- `django-admin startproject social_frames .`
- `python3 manage.py startapp storyboard`
These prompts genrates the skeleton setup for Django implimentation.

- `python3 manage.py migrate`
For every new app, it's neccessary to migrate to keep the database up to date.

Cloud service setup:
------
Cloudyboard was setup on Heroku in following steps:
- click "New app"
- Give the app a name, and pick Europe
- Inside the "Settings tab", is where the "config vars" is setup.
- The file "Procfile" and its content is neccessary before deployment.
- Inside the Deploy tab, click "Github" as deployment method.
- In the field, social_frames was entered and selected.
- Click "deploy branch".
Cloudyboard was setup on ElephantSQL in following steps:
- Click "Create new instance".
- Give it a name, as of 27 nov 2023, Cloudyboard has the "Tiny turtle" plan.
- Click "location", Cloudyboard use Stockholm as its data center.
- Click "Create instance"
- The link can be found in env.py
Cloudyboard was setup on Cloudinary in following steps:
- Inside the Dashboard tab, there's an API enviroment variable"
- The API key can be found inside env.py

10. Credits
======
- The layout is custom made, with help from Bootstrap 4.
- The font used is Raleway found at Google Fonts.
