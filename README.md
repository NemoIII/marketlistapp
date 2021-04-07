# Market List Django Module

---

### First Step:

1. Create a folder where your project will be place and name it with project name.
2. _cd folder_
3. Create a virtual enveriment. Here was used pipenv to create the virtualenv.
   * _pipenv shell_ to start the enveriment.
   * _pip install -r requeriments.txt_
   * _django-admin startproject <project name>_
4. _cd <project name>.
   * _python manage.py runserver_
5. _Ctrl C_ to stop the server.
6. Start a new app.
   * _python manage.py startapp <app name>
7. Add the app into the project settings.
   * _cd .._
   * _vim settings.py_
   * Go to `INSTALLED_APPS` and add the app `'<app name>'`
8. _python manage.py runserver_

---

**After you have done that above:**

---
#### On admin page:
Access [_localhost:8080/admin_](http://127.0.0.1:8000/admin/)

Click on [_Scores_](http://127.0.0.1:8000/admin/scores/score/)

![_Scores_](img/1.png)

You'll see a ![+ Add](img/3.png)
Add a value below 70 scores on **Result:** and save.

That simple! :grinning:

What happend in here:

* If the score is loewr than 70, is sending a sms messagem to the phone registered on Twiolio Free Trial.
```Python
if self.result < 70:
```

---


