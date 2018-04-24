bink-test
=========

Coding test for Bink


# The Application

The most recent version of the app is hosted this this address: http://zrobinson92.pythonanywhere.com/masts

If you want to specifically run the app locally here are the steps:
(Assuming you are going to install inside a fresh virtual environment)
1. From the base of the project run `pip3 install -r requirements.txt`
2. To create the local database run `python3 manage.py migrate`
3. To run the application run `python3 manage.py runserver`
4. Navigate to [http://localhost:8000/masts](http://localhost:8000/masts)
5. First time running the server there is no data in the DB
6. Use file upload functionality to upload the file located at: `bink-test/phoneMasts/resources/Mobile Phone Masts.csv`
where you cloned the repository