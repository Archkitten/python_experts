## [Flask Portfolio Starter](https://nighthawkcodingsociety.com/projectsearch/details/Flask%20Portfolio%20Starter)
Runtime link: https://portfolio.nighthawkcodingsociety.com/
### Idea
Starter code should be fun and practical.
### Visual thoughts
#### Organize with Bootstrap menu 
#### Add some color and fun through VANTA Visuals (birds, halo, solar, net)
#### Show some practical and fun links (hrefs) like Twitter, Git, Youtube
#### Show project specific links (hrefs) per page

### Implementation progress (August 13th, 2021)
#### Project entry point is main.py, this enables Flask Web App and provides capability to renders templates (HTML files)
#### The main.py is the  Web Server Gateway Interface, essentially it contains a HTTP route and HTML file relationship.  The Python code constructs WSGI relationships for index, kangaroos, walruses, and hawkers.
#### The project structure contains many directories and files.  The template directory (containing html files) and static directory (containing js files) are common standards for HTML coding.  Static files can be pictures and videos, in this project they are mostly javascript backgrounds.
#### WSGI templates: index.html, kangaroos.html, ... are aligned with routes in main.py.
#### Other templates support WSGI templates.  The base.html template contains common Head, Style, Body, Script definitions.  WSGI templates often "include" or "extend" these templates.  This is a way to reuse code.
#### The VANTA javascript statics (backgrounds) are shown and defaulted in base.html (birds), but are block replaced as needed in other templates (solar, net, ...)
#### The Bootstrap Navbar code is in navbar.html. The base.html code includes navbar.html.  The WSGI html files extend base.html files.  This is a process of management and correlation to optimize code management.  For instance, if the menu changes discovery of navbar.html is easy, one change reflects on all WSGI html files. 
#### Jinja2 variables usage is to isolate data and allow redefinitions of attributes in templates.  Observe "{% set variable = %}" syntax for definition and "{{ variable }}" for reference.
#### The base.html uses combination of Bootstrap grid styling and custom CSS styling.  Grid styling in observe with the "<Col-3>" markers.  A Bootstrap Grid has a width of 12, thus four "Col-3" markers could fit on a Grid row.
#### A key purpose of this project is to embed links to other content.  The "href=" definition embeds hyperlinks into the rendered HTML.  The base.html file shows usage of "href={{github}}", the "{{github}}" is a Jinja2 variable.  Jinja2 variables are pre-processed by Python, a variable swap with value, before being sent to the browser.

### IDE management (things that happened beyond plan)
#### Recall on ".gitignore" solution to the pains of temporary files.  Start a ".gitignore" and avoid promoting temporary files to Git, for instance IDE xml files.
#### A project needs to establish a "requirements.txt" to keep track of Python packages used by the project.  This help in other IDEs and Deployment.  IntelliJ has menu Tool -> Sync Python Requirements to start file. 

Requirements: Scrum Board (Ideation / Design )
Scrum Master. Define tasks and place assignments to in-progress on the Scrum board.
Designer. Wire Frame (at least three theme pages, team mini-labs, and about)
Technical Lead. Coordinate brain write session, after preliminary wire frames, make sure you capture technical complexities as an output of this exercise (input, saving data, comments, visual actions, animations, ...)
GitHub assets
Navigators. Capture or build highlight of Ideation in README.md, this allows ideas to persist with Project,  Make sure that work from Developers works to expectations (testing, suggestions for improvement)
Developers. Bootstrap drop downs in navbar, start to form Wire Frame menu options.  Each menu option should have a Stub code page
Developers. Integration of Greet like functionality into a mini-lab page
Developers. Integration of Video Journal 0 into a mini-lab page
TPT points (Design-a-Thon)
Completed Task
Quality and Effort

Evidence: 
Aidan:
https://docs.google.com/document/d/1Hfj5lmAUTpCRWe_yNsZ8gwa4-_xsiJCL2-EJhQjU4ec/edit?usp=sharing

William: https://docs.google.com/document/d/1dB3nRMvoKc-11rIvAo-7lykMnfGde53yRo2XQuAwGAo/edit
https://docs.google.com/presentation/d/1eqZ7LM41xWljfpzlHo48bkBlsybnzl5qE66Ltlr5jT0/edit#slide=id.ged3369d0c1_7_5

Arch: 
https://docs.google.com/document/d/1QuDrQhJw3bN03GOHe0MxFisd8DuYWePGO4MYqzZIAX8/edit?usp=sharing

Tyler: 
https://github.com/Archkitten/python_experts/projects/1

Tyler: 
https://docs.google.com/document/d/1I8Icisj5PvAJZjlz8MXOyfsih3Yv6XpvOQDr8sqHd4s/edit?usp=sharing

David: I dont have his work :( 
