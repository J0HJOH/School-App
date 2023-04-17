# AE-FUNAI Mobile App 

## Description
This projects aims at building a modile app for FUNAI students and for the school management with the sole
of providing and offering better features that will enhance the school portal 

## Contribution Guildlines

* Fork this repository
* Clone the repository to your local machine using git clone https://github.com/J0HJOH/School-App
###  Follow this steps to begin your contribution:
 #### For the Frontend:
   - Built using Flutter

  ##### Getting Started with flutter

This project is a starting point for a Flutter application.

A few resources to get you started if this is your first Flutter project:

- [Lab: Write your first Flutter app](https://docs.flutter.dev/get-started/codelab)
- [Cookbook: Useful Flutter samples](https://docs.flutter.dev/cookbook)

For help getting started with Flutter development, view the
[online documentation](https://docs.flutter.dev/), which offers tutorials,
samples, guidance on mobile development, and a full API reference.



 ### For the Backend:
- Built using Python
* Prerequisites:
    * Ensure you have Python installed

* Create a Virtual Enivroment 
    * cd ./env (Where env is the name of your virtual enviroment)
* Activate your Virtual Enivroment on your terminal
    * For Windows Users
        * ./scripts/activate
    * For Mac Users
        * ./bin/activate
* cd school-app/backend
* Run the following commands
```py
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate

```
* Create a Super User
    * Using the command
    ```py
    python manage.py createsuperuser
    ```
* Run the development server using
    * Using the command
    ```py
    python manage.py runserver
    ```
