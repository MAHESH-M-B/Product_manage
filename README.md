# Products Catalogue App

A repository which contain Products Catalogue App which can used for </br>
1,Load the products in the  excel to database</br>
2,To find top-most parent of a product  using a its name or product code</br>
3,To display the name of all of the children in sorted order  using product name</br>
4,Display the count of active and in-active products</br>
5,Display the value of average product price per Category L1 and Category L2</br>


# How to use this branch



To get this running, simply run the  the following 


## Step 1: clone this repository
navigate inside the directory


## Step 2: Install requirements.txt

`pip install -r requirements.txt`

## Step 3: Create databases

Create the databases and the initial migrations with the following command:</br>
`python manage.py makemigrations`</br>
`python manage.py migrate`

## Step 3: Run server

And start the server with 

`python manage.py runserver`


