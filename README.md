# politico-api
Api endpoints for politico app.Politico app enables citizens to vote,view poll results and view politicians who have expressed interests in the different government offices.

[![Build Status](https://travis-ci.com/Bettykirii/politico-api.svg?branch=develop)](https://travis-ci.com/Bettykirii/politico-api)[![Maintainability](https://api.codeclimate.com/v1/badges/f40d762e3c56cb8f30a1/maintainability)](https://codeclimate.com/github/Bettykirii/politico-api/maintainability)[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f5bf7746e6424aad9feb4b6c5dd1ec74)](https://www.codacy.com/app/Bettykirii/politico-api?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Bettykirii/politico-api&amp;utm_campaign=Badge_Grade)[![Coverage Status](https://coveralls.io/repos/github/Bettykirii/politico-api/badge.svg?branch=develop)](https://coveralls.io/github/Bettykirii/politico-api?branch=develop)




# Requirements
* Git version
* Python 3.6
* Vscode

# Host
  * Heroku host https://politico-api2.herokuapp.com/app

# Installation

* clone the repo
  * git clone  https://github.com/Bettykirii/politico-api.git
v
* cd to project directory
   * cd politico-api

* Create a virtual environment and activate :


 python3 -m venv venv
  * On Windows:

py -3 -m venv venv
*If you needed to install virtualenv because you are on an older version of Python, use the following command instead:

virtualenv venv
* On Windows:

\Python27\Scripts\virtualenv.exe venv
Activate the environment
Before you work on your project, activate the corresponding environment:

. venv/bin/activate
* On Windows:

venv\Scripts\activate
Your shell prompt will change to show the name of the activated environment.

API endpoints       | Function             | URL Route
-------------       | -------------        |  -------------  
POST Parties        | Creates parties      | app/v1/parties
GET Parties         | get all parties      | app/v1/parties
GET specific party  | gets a specific party by id | app/v1/parties/ int:partyID
PATCH specific party| edit specific party   | app/v1/parties/int:partyID
DELETE specific party| delete specific party| app/v1/parties/int:partyID
POST Offices  | Create parties | app/v1/offices
GET Offices   | get all parties| app/v1/offices
GET specific party  | get specific party| app/v1/offices/int:officeID

# Acknowlegements
 * Andela bootcamp

# Authors
 * Warware kirii
