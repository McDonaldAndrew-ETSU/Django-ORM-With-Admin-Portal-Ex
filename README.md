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
