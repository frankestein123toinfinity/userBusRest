### User-End API for Tum-Tum-Tracker
Updates a SQlite db in the Mobile App.

This API uses `python3`(3.5.2+). Please DONOT use `python` for editing the API itself.

Steps to Use this API:
* Create a Virtual Environment for Isolating your API.
  * In Terminal, execute `pip install virtualenv`. This is a common tool used to create Isolated python environments.
  * Create a new directory to work in and `cd` into it. Next execute `virtualenv -p /path/to/python3 venv`. This creates a virtual environment named venv which has access to only `python3` and no other dependency.
      * Incase the above execution gives an error, check the path of `python3` using `whereis python3`. This should give a rough idea about your path.
  * Activate the Virtual Environment by using `source venv/bin/activate` from the folder you executed the virtualenv function in. This will result in a prompt with your environment name, i.e. `(venv)user@xyz:~current/directory,$` instead of `user@xyz:~current/directory,$`
* Install your dependencies in your isolated environment, namely `django`and `djangorestframework`
   * `pip install <dependency-name>` Just in case :P.
* Now just clone this repository in your folder and you're good-to-go!

A better comprehensive tutorial of setting the environment along with testing and building similar APIs is provided in this [link](https://scotch.io/tutorials/build-a-rest-api-with-django-a-test-driven-approach-part-1).

Toodles!
