# Awards
## Author  
  
[Esau Kiprono](https://github.com/EsauKip)  
  
# Description  
 This is a website application that users can view projects posted and rate them according to design, usability and content. Users can also be able to add their own projects to be rated by others on registering an account and logging in.

##  Live Link  
 
  

 
## User Story  
  


  
## Setup and Installation  
  
##### Clone the repository:  
 ```bash 
 git@github.com:ESauKip/Awards.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd Awards 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual 
- source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python manage.py server 
```
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.8](https://www.python.org/)  
* [Django==3.2.9](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs  
  
## Support and Contact Information 

To make a contribution to the code used or for any queries feel free to contact me via my email addresses kipronoesau28@gmail.com

## License

### MIT LICENCE