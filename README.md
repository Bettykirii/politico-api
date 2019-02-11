# politico-api
Api endpoints for politico app.Politico app enables citizens to vote,view poll results and view politicians who have expressed interests in the different government offices.

[![Build Status](https://travis-ci.com/Bettykirii/politico-api.svg?branch=develop)](https://travis-ci.com/Bettykirii/politico-api)[![Maintainability](https://api.codeclimate.com/v1/badges/f40d762e3c56cb8f30a1/maintainability)](https://codeclimate.com/github/Bettykirii/politico-api/maintainability)[![Test Coverage](https://api.codeclimate.com/v1/badges/f40d762e3c56cb8f30a1/test_coverage)](https://codeclimate.com/github/Bettykirii/politico-api/test_coverage)[![Coverage Status](https://coveralls.io/repos/github/Bettykirii/politico-api/badge.svg?branch=master)](https://coveralls.io/github/Bettykirii/politico-api?branch=master)[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f5bf7746e6424aad9feb4b6c5dd1ec74)](https://www.codacy.com/app/Bettykirii/politico-api?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Bettykirii/politico-api&amp;utm_campaign=Badge_Grade)


# Requirements
* Git version
* Python 3.6
* Vscode

# Installation

* clone the repo
  * git clone  https://github.com/Bettykirii/politico-api.git

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

API endpoints | Function       | URL Route
------------- | -------------  | -------------  
POST Parties  | Create parties | app/v1/parties
GET Parties   | get all parties| app/v1/parties
GET Parties <id> | Create parties | app/v1/parties<p_id>
GET Offices   | get all offices| app/v1/parties
POST Offices  | Create parties | app/v1/parties
GET Offices<id>   | get all parties| app/v1/parties