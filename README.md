# Models Location for Model Classes
### Python 3.10.6
Inside the application's directory, go to the models.py

Here is where you create your model classes (ORM to the database). Seperate model classes go in the same file.

## Define the Field Type for Model Class's Fields
- CharField: A single line of text.
- TextField: Multiple lines of text.
- BooleanField: A Boolean true/false option.
- DateField: A date.
- TimeField: A time.
- DateTimeField: A date and time.
- URLField: A URL.
- IntegerField: An integer.
- DecimalField: A fixed-precision decimal number.
## Field Options
- null
    - Boolean option to allow null values.
    - Default is False.
- blank
    - Boolean option to allow blank values.
    - Default is False.
- default
    - Allows the configuration of a default value if a value for the field is not provided.
    - If you want to set the default value to a database null, set default to None.
- unique
    - This field must contain a unique value.
    - Default is False.
- min_length and max_length
    - Used with string types to identify the minimum and maximum string length.
    - Default is None.
- min_value and max_value
    - Used with number types to identify the minimum and maximum values.
- auto_now and auto_now_add.
    - Used with date/time types to indicate if the current time should be used.
    - auto_now will always set the field to the current time on save, which is useful for last_update fields.
    - auto_now_add will set the field to the current time on creation, which is useful for creation_date fields.

# Foreign Keys
To create a one-to-many relationship we include the foreign key field inside of the Model class and set it to the "FieldType" of **models.ForeignKey('name_of_model', on_delete=models.PROTECT)**

# Make a Migration
The migration is what uses the Model classes and converts it to a database schema. To make a migration type:
**python manage.py makemigrations app_name**

## Display the SQL for the migration
To build appropriate SQL statements, type:
**python manage.py sqlmigrate app_name migration_name**

# Update the database
The migrate command will run all migrations. In the case of SQLite, the command will even create the database if it doesn't exist. Let's create our database and perform the migrations.
**python manage.py migrate**


# View SQLite Database
After installing SQLite Extension, use the command pallete to type: **SQLite: Open Database**
Select **db.sqlite3**
At the bottom of your workbench on the left side, select the arrow next to SQLITE EXPLORER.


# Work With Data
Enter the following command to start the shell:
python manage.py shell

Import the models from models inside app:
from app_name.models import model_name, model_name

Create a new row by running the following Python command in the shell:

racer = Racer(name="Andy Mac", skill=100)
racer.save()

To Update type:
racer.skill = 99
racer.save()

#### You can find more Django PowerShell Commands here: https://learn.microsoft.com/en-us/training/modules/django-models-data/8-exercise-work-with-data

# Authentication and Authorization
Django has three main types of users by default: **users**, **staff**, and **superusers**. You can create your own types by making groups or setting unique permissions.
### Access Levels
|   Access     | User | Staff  | SuperUser |
|    :---      | ---: | :----: | :---      |
| Admin Site   | No   |  Yes   | Yes       |
| Manage Data  | No   |  No    | Yes       |
| Manage Users | No   |  No    | Yes       |
By default, staff have access to the admin site but not to modify any data. You can set individual permissions or create groups as needed to provide the appropriate levels of access.

To create users in Django, you must first create a superuser. To create a superuser: **python manage.py createsuperuser**.
After you create a superuser, you can access the admin site to create any other users.

After the admin user has been created, it's time for our first sign-in to the Django admin interface. During the project setup earlier in this module, we started the server, so our admin site is already active. Go to:
http://localhost:8000/admin.

# Register Models
To register your models in order to have access to the data, open your app(s) directory admin.py file. Just add these lines of code to register your models:
- **from .models import Model_1_Name, Model_2_Name**

- **admin.site.register(Model_1_Name)**
- **admin.site.register(Model_2_Name)**
- **etc**

# Create Views
Open the views.py file in a specific app. We will customize our views and the first step to do so is to alter the initial import statement.

Change the import statement to **from django.shortcuts import render, get_object_or_404** and add **from . import models**

Django View code can now be created.

# Create the URLconf
For our views to be callable, we need to register the appropriate paths.
Create a urls.py inside of the specific app directory.

use this code:

- from django.urls import path
- from . import views

- urlpatterns = [
    - path('', views.method_one_view_list, name='method_one_view_list'),
    - path('method_two_view_detail/<int:pk>', views.method_two_view_detail, name='method_two_view_detail'),
    #### More patterns to come later
]

Now we must register this URLconf with the main URLconf in the project by going to its urls.py.
First import from django.urls import path, include. Inside the urlpatterns array, include the path to the specific App's url.py in order to access the App's View code

- urlpatterns = [
    - ...
    - path('empty_or_something/', include('name_of_app.urls'))
]

# Create Base Templates (Parent Pages)
Creating a parent page is the same as creating any Django HTML template. You provide the outer structure and then include {% block %} placeholders. These placeholders allow the children to provide the content to be placed in those placeholders.

Create a new folder inside your specific App named ***templates***. This is where you will keep your html files.

### Child Page
We can create a child page from the parent by using the extends keyword. With this keyword, we provide the name of the HTML file of the parent template. We then use the appropriate {% block %} statements to add the content specific to that page.

# Generic Views
In the specific App's views.py, import django.views generic library
 **from django.views import generic**

After creating a View class using a parameter of generic.type_of_view (think CRUD: CreateView, DetailsView, UpdateView, and DeleteView), we must register the class with urls.py in the App.

# Creation workflow
At the surface, the code to allow a user to create an item might seem trivial. As it turns out, it's a deceptively involved process.

- The user sends a GET request to signal they want the form to create a new item.
- The server sends the form with a special token to prevent cross-site request forgery (CSRF).
- The user completes the form and selects submit, which sends a POST request to indicate the form has been completed.
- The server validates the CSRF token to ensure no tampering has taken place.
- The server validates all information to ensure it meets the rules. An error message is returned if validation fails.
- The server attempts to save the item to the database. If it fails, an error message is returned to the user.
- After successfully saving the new item, the server redirects the user to a success page.
This process requires quite a bit code! Most of it's boilerplate, which means it's the same every time you create it.

# Form templates for create and update
The generic views can create the HTML form for us dynamically. All we need to provide is a template to act as the placeholder for the form. The placeholder template ensures the form matches the rest of our site. Fortunately, we don't need much code to create it.

The generic views automatically create a form variable for our template to use. The form elements provided by Django can be displayed inside <p> tags or as a <table>.

The form variable contains all of the appropriate HTML to create the controls from the form. It doesn't contain the <form> tag itself or a submit button. Our template must include four items:

- The form element with the method set to POST because this setting triggers the save operation on the server.
- The code {% csrf_token %} to add the CSRF token to prevent spoofing.
- The code {{ form.as_p }} or {{ form.as_table }} to display the dynamically generated form.
- The submit button.

- <form method="post">{% csrf_token %}
    - {{ form.as_p }}
    - <button type="submit">Save</button>
- </form>

# get_absolute_url function to Models class
In order to get back to a page after submitting a Create or Update form, we must add the function get_absolute_url to our specific model and import the reverse method.

from django.urls import reverse

    def get_absolute_url(self):
        return reverse('dog_detail', kwargs={"pk": self.pk})

