# django-Product-manage

A repository which contain Products Catalogue App
which can use for 
Load the products in the  excel using any excel reader library (or your own custom reader) of your choice,
Given a product name or product code, find the top-most parent of it by its name,
Given a product name, display the name of all of its children in sorted order,
Display a count of active and in-active products,
Display the value of average product price per Category L1 and Category L2,


# How to use this branch



To get this running, simply run the  the following 


## Step 1: clone this repository
## Step 2: Install requirements.txt

`pip install -r requirements.txt`

## Step 3: Create databases

Create the databases and the initial migrations with the following command:
 `python manage.py makemigrations`
`python manage.py migrate`

## Step 3: Run server

And start the server with 

`python manage.py runserver`


