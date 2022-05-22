# Assignment 2 - Todo Application

## Author



## Description

Create a Django Web Application with a single model to hold Todos and a single home / index page that will list out all of the Todos that have been entered via the admin. The home page should use Class-Based Views and extend a base template even though there is only one page. Once created, you will add testing to make sure the model and all pages work correctly. Lastly, prep it for hosting on Heroku.

The main non-admin page will be a list of all the Todos and the date that they should be completed by. Additionally there should be some buttons (as links) for add, edit, and delete that will take the user to the corresponding admin page for that functionality. You can see a screenshot of what I am expecting below in the screenshots section.

Tests for the site should be similar to the ones we wrote in class. I am expecting three in total. Just like what we did in the in-class.

Add required files and settings for publishing the site on Heroku. Fully hosting is worth extra credit. If doing so, submit the URL for the site to Canvas as the submission for this assignment. Regardless of extra credit, have your most recent commit pushed up to GitHub.

Ensure that you have a `requirements.txt` file with your required packages. I will not grade the assignment if I can't restore the packages easily!

In general, the program should allow the following functionality:

1. Created Django Project and App for todo functionality.
2. Base template that other templates will extend from.
3. Todo Model.
4. Home URL/View/Template listing all Todos. Views must be Class-Based.
5. Superuser can do CRUD operations in the admin.
6. Basic Bootstrap styling.
7. Three Tests for the project which include:
   1. Model Content. Be sure to test all fields.
   2. URL exists at correct location.
   3. Homepage.
      1. Assert response code.
      2. Assert correct template used.
      3. Assert response contains correct content (Name and Date).
8. Files and Settings correct for publishing to Heroku.
9. Ensure `requirements.txt` is included in your project.
10. If doing Extra Credit, URL submitted to Canvas as Assignment Submission.

Documentation should include the following for this, and all future assignments:
* Comments at the top of each file that you add source code to with the following:
  * Your Name
  * Class
  * Date
* A comment after the definition of each method describing what it does. Use the """ (triple quote) doc string method for the comment.
* Comments in the rest of the code where it isn't obvious what is going on. (I prefer above the line comments vs at the end of the line because who likes to horizontally scroll, but either will work)

### Database Requirements
I have included an ERD (Entity Relationship Diagram) that shows the database tables. You should be able to use this diagram to know how to structure your models. Additionally, I tend to include the User (and sometimes related) tables in the ERD. You will never need to create these user models as they are included by Django. However, by including them in the ERD you can see the relationships between users and other tables. In the case of this assignment, there is no relationship between users and Todos. But, in future assignments, there will be. Consider this a primer into being able to create models from an ERD.

In the case of this assignment and the Todo model that you will need to create, it will contain the following fields:
* Name
* Complete By

![Database Entity Relationship Diagram](https://barnesbrothers.net/cis218/assignment_images/assignment_2/cis218_assignment_2_erd.png "Database Entity Relationship Diagram")

### Screenshots
I am not expecting that your site will necessarily look exactly like mine, but I am expecting that you will use Bootstrap and that you will try your best to match the screenshot. Since you don't know exactly how I did it though, it's fine if there are differences. Think of the screenshot as a general guide.

![Todo Page Screenshot](https://barnesbrothers.net/cis218/assignment_images/assignment_2/cis218_assignment_2_screenshot.png "Todo Page Screenshot")

### Solution Requirements
* Created Django Project and App for static pages.
* Base template that other templates will extend from.
* Todo Model.
* Home URL/View/Template listing all Todos.
* Superuser can do CRUD operations in the admin.
* Basic Bootstrap styling.
* 3 Tests for the project.
* Files and Settings for publishing to Heroku.
* If doing extra credit, URL submitted to Canvas as Assignment Submission.

### Notes
> [!IMPORTANT]
> * All Views must be Class-Based Views. Function-Based views will not be graded.
> * All Templates should be in a `templates` directory in the root of the project. Templates in any other location will not be graded.
> * Ensure that you have a `requirements.txt` file with your required packages. I will not grade the assignment if I can't restore the packages easily!
> * Your number of commits should be similar to the number we did with the in-class work or more. You need to show me your progression through the development process of your assignment. Submitting an assignment with only 1 or 2 commits does not do this. You need more. Failure to have enough commits will result in a "zero".
> * Assignment work should be similar to the work we did with the in-class work. If a submitted assignment is wildly different than the in-class work and no references to resources that were used are provided via this README file, I will assume that you did not write the code yourself and instead stole it from somewhere without giving credit. Which will result in a "zero". Even if you plan to use outside references and list them in this README, be sure you are not plagiarizing anyone's work. See the syllabus for more information.

You do not need to make CRUD pages for this assignment. All CRUD operations are done via the admin.
The buttons (links) you see in the screenshot are links to the admin pages. Not links to custom CRUD pages.

In order to render out the number of Todos in the template, you can reference the following link. It shows how to use what is called a template filter. This linked page contains all sorts of template tags and filters that can be used inside templates to do things. This is an invaluable resource that I reference constantly. We will explore template tags and filters more in later chapters / assignments. But knowing about it now does not hurt. In fact, you can see tags that we have already used such as the url one.
<br>https://docs.djangoproject.com/en/4.0/ref/templates/builtins/#length

In order to be able to link to certain pages within the admin, you can look at the following page:
<br>https://docs.djangoproject.com/en/dev/ref/contrib/admin/#reversing-admin-urls

In it, you can see that reversing a url for an admin page follows the format:

```
{{ app_label }}_{{ model_name }}_{{ action }}
```

So, assuming an app named `todo` and a model named `Todo` you would use the following for getting to the change link:

```
todo_todo_change
```

And since the url template tag takes a url name, you can get to admin ones by prefixing the url name with the app label (more on this later too). In the case of the admin, the app label is admin. So, the full name that can be reversed would be:

```python
'admin:todo_todo_change'
```

The last bit of info you need to recognize is that the change page is for a specific database entry.
So, we need the PK for the thing we would like to change. Thus we will need to provide the `object_id`
to any use of reverse or url and the change link.
NOTE: Not all links require a id / pk. Read the linked Django doc page to know which ones.

So, doing this in the template would look something like:

```htmldjango
{% url 'admin:todo_todo_change' <object_id> %}
```

Where <object_id> will be replaced with the id / pk of the object we are trying to link to.
Assuming you have an instance of a Todo in the template called `todo`, it would look something like:

```htmldjango
{% url 'admin:todo_todo_change' todo.pk %}
```

If you have more questions regarding this, don't hesitate to ask.

## Grading
| Feature                                  | Points |
|------------------------------------------|--------|
| Create Django Project and App            |    10  |
| Base Template                            |    10  |
| Todo Model                               |    15  |
| Home Url/View/Template                   |    15  |
| Superuser can do CRUD in admin           |    15  |
| Bootstrap Styling                        |    10  |
| Automated Tests                          |    10  |
| Heroku Deployment Files and Settings     |     5  |
| Documentation                            |     5  |
| Readme                                   |     5  |
| **Total**                                | **100**|
| **Extra Credit** Full Heroku Deployment  |   **5**|

## Outside Resources Used



## Known Problems, Issues, And/Or Errors in the Program


