# Acko Dashboard 1.0

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

Acko Dashboard 1.0 is a Data-driven approach to Company insights. Our idea focuses on leveraging data publicly available from the US Consumer Finance Network. Our model facilitates analytical insights into companies pitted against each other. The end result for our work is to provide an easier and automated approach to improving insurance companies based on historical data.

# Features

- Import csv Data file of Insurance company complaints and generate practical insights.
- Interactive UI to facilitate better understanding.

# Installation:

- Download the repo, it will be downloaded as 'Acko_1.0'. Rename the directory to 'hacko'. It is a django project.
- Now make a directory named 'hackos_proj' and shift the directory 'hacko' to it.
- There is a directory named frontend in 'hacko' directory. Place it in the directory 'hackos_proj' and delete in 'hacko' direcotry, 'frontend' has all the frontend code of the site.
- First you have to set up the backend to the project, First install the virtualenv, with command 'pip3 install virtualenv'
- Then create and activate the virtual environment using the command 'virtualenv env', this makes a virtalenv 'env'
- Now there is a requirements.txt file in the hacko directory. Install the requirements.
- The requirements can be installed using the 'pip install requirements.txt', this installs all the requirements to the backend part.
- Go to the github repo, you can find a link to the csv file dataset there. Download the dataset and place it in the following directory path 'hacko/hacko/accounts/static/accounts/csv', then make the directory 'static_cdn' in the hacko directory (I mean in the first directory).
- Now, open the terminal in the directory with 'manage.py' file.
- Run the file, to run the backend using the command 'python manage.py runserver'
- Now, open another terminal in same directory and run the migrations using the command 'python manage.py migrate'
- Then, create a user (a superuser), using command 'python manage.py createsuperuser', It promps you for the username, email and password, then create them (but remember don't forget the username, or password).
- Now, go to the file 'login.html' and login to the site using the credentials you just created.
- You can see the analysis to the different data, the data is analysed and different graphs are plotted using the canvasJS.

### Techstack used

Acko Dashboard 1.0 uses a number of programming languages and tools to function:

- [1] - Python Django, backend anyone?
- [2] - JQuery, cause duh :P
- [3] -Version Control : GIT, could I be more obvious?

And of course Acko Dashboard 1.0 itself is open source with a motivation to scale with target specific companies.

### Installation

Acko Dashboard 1.0 requires Django 1.11.6v to run.

Install the dependencies and devDependencies and start the server.

```sh
$Run the Requirements, duh!
```

### Development

Developers involved,

```sh
$ M Rahul Krishnan
$ Ram Manoj
$ Siddharth Kumar
```

### Todos

- More views
- UI for graphing.

## License

MIT

**Free Software, Hell Yeah!**
