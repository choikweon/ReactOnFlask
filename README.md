# Flask

**Chapters**

 - Chapter 1 : Hello, World!
   + installs ```flask``` and ```python-dotenv```
 - Chapter 2 : Templates
   + template htmls go to */app/template* directory
   + does not really use traditional html, should be rendered thru ```render_template()```
   ```{{% cond or block %}}```
 - Chapter 3 : Web Forms
   + installs ```flask-wtf```
   + code blocks replace traditional html and js form code inside ```<form>``` 
   + _*??*_ what does ```form.hidden_tag```() do?
 - Chapter 4 : Database
   + installs ```flask-sqlalchemy``` and ```flask-migrate```
   + the tutorial uses SQLite, but I am trying to use PostgreSQL instead
   + psycopg2 error occurs when connecting to DB -> solved. use ```psycopg2-binary``` instead
   + Flask is to be run from localhost by default. when using docker, add ```--host=0.0.0.0``` option to access Flask server in the container (and do not forget to add ```EXPOSE portnum``` to Dockerfile)
   + network between containers use its name, for example, use ```db:``` instead of ```localhost:```
   + docker-compse up! Flask and PostgreSQL containers are up and linked to each other.
   + for multiple command for executing flask db migration, use
   ```
   command: bash -c "command 1 && command 2 && ... "
   ```
   + from the example microblog, ```User``` model crashes with PostgreSQL default table ```user```. need to avoid the name. Changed into ```Mbluser```
   + Passing ```flask shell```, seems not to be used in docker environment.
 - Chapter 5 : User Logins
   + installs ```flask-login```, ```email-validator```
   + ```@login_required``` decorator flashes unwanted messages. if I want to fix this, do I have to fix ```flask-login``` from the source?
 - Chapter 6 : Profile Page and Avatars
   + the tutorial uses Gravatar service to generate a picture from md5 hash of the email, but I chose to use a random portrait from <a href="https://www.eveonline.com">EVE Online</a>. using url for the image : ```https://images.evetech.net/characters/95######/portrait``` where # is a digit.
   + adding more and more to the db. and making more templates and forms for them.
 - Chapter 7 : Error Handling
   + making template for some frequent errors : 404 and 500.
   + logs into ```./log``` when ```DEBUG=False``` in config.py
   + built another python container "debug" for ```python -m smtpd -n -c DebuggingServer localhost:8025```
   + python mock mail server did work on localhost, but did not in new debug container. could not find out the reason. whatever. removed the debug container.
   + at the end of the chapter, ```EditProfileForm``` overloads constructor to get a username argument passed to it. NOT fully understood. gotta study python inheritance and overloading part again.
 - Chapter 8 : Followers
   + added user-user m:n relation ```followed```
   + now my brain is getting overheated.
   + I do not understand how ORM and SQLAlchemy is working.
   + need to study ORM and SQLAlchemy, taking enough time. skipping for now.
   + _*!!*_ the code actually generated a table called ```followers```. need to take a look at the code.
   + added ```tests.py``` for unit testing.
   + avatar test fails. sure.
   + the other tests passed but the test cases used SQLite. meaningless.
 - Chapter 9 : Pagination
   + added ```PostForm``` for posting
   + added ```explore``` function which renders index as explore page.
   + ```{% if form %}``` to switch between index and explore
   + pagination applied. using config ```POST_PER_PAGE```
   + _*??*_ uses ```request.args.get()``` the part I do not understand. comes from ```from flask import request```. need to study on it.
   + user/<username> page still shows temp posts. did I miss something?
   + when registering new user, the user is automatically logged in sometimes, or not logged in some of the times. need to check.
 - Chapter 10 : Email Support
   + installs ```flask-email``` and ```pyjwt``` (imports as ```jwt```)
   + installed ```requests``` for sending email request to a seperate container
   + ~~added ```.env.dev``` to ```.gitignore``` temporally, because the file now contains my Google account and password (which is for email server configuration). I don't want to publish them into a public github repo.~~
   + gmail does not allow 'low security apps' to access the account. should make gmail allow it in the account settings.
   + tested flask-email in a seperate environment, and got ```RuntimeError: Working outside of application context.``` message. need to study what an "app" is in Flask.
   + sending email works in ```with app.app_context():``` clause. app and context.
     - does run without the clause if it runs within the app. _*??*_
   + as email server is run in a seperate container, ```.env.dev``` is removed from ```.gitignore```
   + email server did not work as expected: forgot ```--host=0.0.0.0``` as mentioned in Ch. 4. 으악 짜증나.. 이것땜에 똑같은 삽질을 반복함..
   + seperate email server is up!
   + when sending an email from gmail server, "sender" and "text_body" does not appear in the mail recieved.
   + _*??*_ how does ```expires_in``` in ```jwt``` work?
   + skipped threading part, since I use a seperated email server.
 - Chapter 11 : Facelift
   + installs ```flask-bootstrap```
   + ... just copy and pasted the templates from the tutorial github
   + looks better!
 - Chapter 12 : Dates and Times
   + installs ```flask-moment```
   + does some TZ works
 - Chapter 13 : I18n and L10n
   + installs ```flask-babel```
   + _*??*_ which translation engine does this use? will it translate into/from korean?
     - did not really used any engine. all the translated texts are supposed to provided by the developer.
   + learned that i18n means internationalization, and l10n means localization (...)
   + ```_()``` and ```_l()```...
   + _*??* lazy evaluation?_
   + _*??* how are ```_()```, ```_l()```, and rendering ordered in the process?_
   + translation complete!
   + need to exec ```pybabel extract, export, update, init, compile``` to apply them all.
   + command group enhancements : ```app/cli.py``` file would define custom flask command options but i will skip this part because the service runs in a docker container.
 - Chapter 14 : Ajax
   + installs ```langdetect```
   + Single Page Applications. SPAs. written in JS mostly. client-side executes the code.
   + Ajax : Asynchronous JavaScript and XML (XML replaced by JSON recently).
   + uses jQuery
   + JS involved, getting more complexed.
   + what does ```g``` do?
   + why do we use ```g.locale``` when we can get the preffered language from the browser?
 - Chapter 15 : A Better Application Structure
   + using blueprint, the whole service is modulized into three parts.
   + changes many lines of codes, and regroups files into directories.
   + errors WILL occur, so this chapter is branched into "blueprint"
   + errors DID occur, fixed them and now the app runs without errors, but not as intended.
   + pages are not routed properly, so cannot access pages from url.
   + 갑자기 이렇게 바꾸면 정신없음...
   + problems solved : did not include "bp"s created into the app.
   + everything screwed up, all hierarchy mixed up. no idea why the author did blueprinting after creating the app to the end.
   + and more errors.
   + and more errors..
   + and more errors...
   + fixed all errors I could found, but there may be more.
 - Chapter 16 : Full-Text Search
   + installs ```elasticsearch```
   + needed the engine installed, not only the python module. -> here goes docker.
   + ... the license system is somehow complex.
   + elasticsearch is no more open-source and 혹시라도 모르니까... I will skip this part.
 - Chapter 17, 18, 19 : Deployment on Linux, Heroku, Docker Containers
   + installs ```gunicorn```
   + tried using amazon ECS, which deploys docker container
     - failed. no idea what to do. also, if I somehow manage to make it work, the cost will be more expensive than lightsail.
   + instead, used aws lightsail ubuntu server
   + each containers were safe, but the difference in OS made it difficult to move to the server
   + anyways, the app is now deployed on an aws server.
   + the page is on : http://3.37.58.29
     - will be down in a few days, after testing.  

 - Chapter 20 : Some JavaScript Magic
   + using bootstrap ```popover()``` and ajax function, makes a mouse-hover popover interface.
   + need to study more about async request and calls.
   + flask + html + db + bootstrap + JS with ajax = ???
   <img src="images/whyworks.jpg" width=240>

 - Chapter 21 : User Notification
   + nothing much. adding another db model and pages for private messages.
   + adding and updating notification badge using repeating ajax call of 10 seconds

 - Chapter 22 : Background Jobs
   + installs ```rq```
   + makes db model for task queue
   + the email is sent using rq in this chapter, but I already have a seperate email server.
   + implemets user post export using task queue.
   + not actually implemented in this project
   + _*??* why are the tasks written in the database when redis takes care of the queue? just to show the progress %?_

 - Chapter 23 : Application Programming Interfaces (APIs)
   + installs ```flask-httpauth```
   + implements REST API for the website.



**Installed packages**

 - flask
   + flask itself
 - python-dotenv
   + saves environment variables at .flaskenv file
   + ```FLASK_APP=microblog.py```
 - flask-wtf
   + defines variables as ```app.config[dictionary_key]```
   + can use ```config.py``` class
   + supports web form
      ```python
      from flask_wtf import FlaskForm
      from wtforms import StringField, PasswordField, BooleanField, SubmitField
      from wtforms.validators import DataRequired
      ```
 - flask-sqlalchemy
   + flask wrapper for SQLAlchemy, which is an <a href="http://en.wikipedia.org/wiki/Object-relational_mapping">Object Relational Mapper</a>
   + support most of relational DB, such as MySQL, PostgreSQL, SQLite
   + ok. PostgreSQL. am I going to come back here for flask when I study PostgreSQL? -> Yes. been there and now here.
 - flask-migrate
   + created by Miguel Grinberg himself
   + flask wrapper for Albemic, which is a DB migration framework for SQLAlchemy
 - psycopg2-binary
   + used for Flask-PostgreSQL data interface. to be exact, python library for psql. ```psycopg2``` package exists, but somehow ```psycopg2-binary``` should be installed instead. ```psycopg2``` throws some error when intalled.
   + not from the tutorial.
   + need to update to pip version 21.2.4
 - flask-login
   + user login module for Flask. keeps tracking the logged in user.
 - email-validator
   + as the name says...
 - flask-mail
   + sends email from the configured email server
 - pyjwt
   + python JSON web token
 - requests
   + sends http request
   + _*!!*_ not from the tutorial, but i installed it to make a seperate mail server container and send a mail request to it.
 - flask-bootstrap
   + flask version of bootstrap
 - flask-moment
   + also created by Grinberg. addon for <a href="http://momentjs.com/">Moment.js</a>.
 - flask-babel
   + translator for flask
 - langdetect
   + language detection. Detects the language used to write the string. not flask-based.
 - ~~elasticsearch~~
   + ~~a text search engine~~
 - gunicorn
   + a WSGI tool, which is critical to make the app open to the world.
   + web app in the debug mode is too fragile. need a WSGI for handling multiple requests.
 - ~~rq~~
   + ~~redis queue.~~ 
 - flask-httpauth
   + authorization using token


**Final Comment**

최종 결과물 : http://3.37.58.29

와... 뭐라고 해야 할지 모르겠는데요, 지금까지 알던건 html과 약간의 css, js였고, 웹 페이지는 직접 html을 깎아가며 만들었고 db도 직접 세팅을 해야 했습니다. 그리고 서버는 아파치로 돌렸고요. 그런데... 플라스크는 그냥 flask run 명령어 하나에 모든게 다 되네요.
그리도 붙일 수 있는 모듈도 너무 많아서...

<img src="/images/toomany.jpg" width=240>

대충 이런 느낌입니다. 오히려 그냥 붙이기만 하면 되는게 너무 많아서 당황스럽습니다.
다만, 모든 것들이 다 pip 패키지에 포장되어서 배달되기 때문에, 그 안에서 무슨 일들이 일어나고 있는지 알 필요가 없다는게 조금 찝찝합니다. 그렇다고 이 찝찝함을 해소하기 위해 패키지를 다 뜯어 볼 수도 없고.

이 저자, Miguel Grinberg, 정말 대단합니다. 많은 튜토리얼들을 봐 왔지만, 이렇게 아무것도 없는 백지에서부터 실제 돌아가는, 그리고 뭔가 쓸데도 있어보이는 (실제로는 없지만) 서비스를 만들기까지 모든 과정을 단계별로 하나씩 자세히 설명해주는 튜토리얼은 처음입니다. 정말 "Mega" Tutorial이라고 할 만 합니다.

거의 3주동안 23개의 챕터를 다 봤지만, 이제 Flask를 알줄 아냐고 물어본다면, 부끄럽게도 대답은 '아니다' 라고 할 것 같습니다. 이 "메가" 튜토리얼에서 너무나도 잘 떠먹여 준 덕분에, 큰 삽질을 하지 않고 튜토리얼을 따라갈 수 있었습니다. 하지만 진짜 공부는 삽질에서 온다고 생각합니다. 이 튜토리얼을 따라가면서, 시키는 대로 하지 않고 제 마음대로 몇 군데 바꿔서 진행한 곳이 있는데, 예를 들어 처음부터 도커로 어플리케이션을 띄워서 시작했으며, db도 sqlite를 사용하지 않고 PostgreSQL로 도커에 따로 띄워서 진행 했습니다. 물론 이 과정에서 많은 삽질을 했고, 덕분에 도커 사용은 어느정도 익힌 듯 합니다. 하지만 플라스크는, 쉽게 받아먹은 만큼 머리에 완전히 박히지 않았고, 튜토리얼에서 만든 작은 서비스를 혼자서 다시 만들어 보라고 하면, 못 할거라고 생각합니다.

물론 프로그래밍의 10%는 직접 코딩하는것이고, 90%는 다른데서 긁어온 코드와 Stack Overflow라고 하긴 하지만, 그래도 제 스스로 평가하기에 제가 이 튜토리얼을 따라가면서 플라스크를 제대로 배웠다고 생각하지는 않습니다.

<img src="images/whyworks.jpg" width=240> <img src="images/whyworks.jpg" width=240> <img src="images/whyworks.jpg" width=240>

...을 반복하면서 와! 신기하다! 라고 생각하는 것의 연속이었던 것 같네요.
특히 자바스크립트와 ajax가 들어가면서 특히 더요.

플라스크와 웹을 배우면서 생각보다 많은 시간이 걸렸는데, 돌아보면 이렇게 "제대로 배운것 같지는 않은데요..." 라고 스스로 평가하게 되니 너무나 아쉽습니다. 그래도 앞으로 회사에서 계속 맡은 일을 하면서, 그리고 삽질을 하면서(...) 점점 더 실력이 늘 거라고 생각합니다.

또, 앞으로 남는 시간에 개인 프로젝트로 제가 가진 트레이딩 카드를 정리하고 파는 웹사이트를 만들려고 하는데, 이때 다시 Flask를 이용해 보려고 합니다. 이 때는 처음부터 모든 것을 직접 만들어야 하니까, 이 과정을 거치고 나면 또 어느정도 자신있게, 플라스크로 뭔가 할 수 있게 되지 않을까요.

 updated Oct 1 2021