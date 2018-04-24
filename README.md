# bink-test

Coding test for Bink


# The Application

The most recent version of the app is hosted at this address: http://zrobinson92.pythonanywhere.com/masts

If you want to specifically run the app locally here are the steps:
(Assuming you are going to install inside a fresh virtual environment)
1. From the base of the project run `pip3 install -r requirements.txt`
2. To create the local database run `python3 manage.py migrate`
3. To run the application run `python3 manage.py runserver`
4. Navigate to [http://localhost:8000/masts](http://localhost:8000/masts)
5. First time running the server there is no data in the DB
6. Use file upload functionality to upload the file located at: `bink-test/phoneMasts/resources/Mobile Phone Masts.csv`
where you cloned the repository

# The Tests

To run the tests on a clean install of the project:
1. From the base of the project run `pip3 install -r requirements.txt`
2. Run the unit tests with `python3 manage.py test phoneMasts`

# The Challenges

There are a couple of challenges I ran into when developing this application that lead me into areas that I would like to improve this application if I had more time:
1. Something that I would like to improve upon would be project structure. I would have liked to have separated the source files and test files into different directories. The problem I had with this was around imports and running the application and tests. I spent some time trying a variety of solutions and involving different structures and ways to solve the issue. In the end I didn't want to spend too long sorting out file structure when I could continue to develop as it was and so moved on and kept the fairly flat structure I have here.
2. Testing the file upload, I was unable to get working using both Mock and MagicMock from unittest. I have left my last attempt commented out in `test_upload_file_form.py` so you can see what I was trying to do.
3. I did not get through to the end of the exercise, but looking over it I would have refactored my `PhoneMasts` model to take a DateField rather than a string for date and specified to desired format for the Date to be DD-MMM-YYYY. It then would have been similar to the smaller phone masts per tenant table I have, requiring a QuerySet be created for dates in a specific range and then displaying them.