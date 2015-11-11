#Introduction #


----------




The purpose for this project is to write a program that reads lightning data from stdin and matches that data against a source of assets to produce an alert. Each line of the lightning data should be arranged as a JSON object representing a lightning strike.  The assets data should also be arranged as a list of JSON objects.


----------


# Install#


----------
The package was expected to work in linux environment. Firstly clone the repo.

    $ git clone 
The project was preferably installed and implemented in a virtual environment. So create a new environment by

    $ virtualenv lightening_venv
    $ . lightening_venv/bin/activate

 The next step is to install the program by

    $ cd lightning_alert
    $ pip install -e .[test]

We can run the following code for testing

    $ lightning_alert < lightning.json assets.json

Where lightning.json and assets.json is in the installed folder.

If the project was expected to installed in actual environment, we can run the following code to install and test

    $ sudo pip install -e .[test]
    $ lightning_alert < lightning.json assets.json

----------


# Characteristics#


----------
##Time complexity##
