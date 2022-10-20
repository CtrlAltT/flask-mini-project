# flask-mini-project

Prerequsite 

 Docker ( not mandatory)
 
 Postman
 
 Description
 
 This is a simple microservice develop in flask which return data  from a json file which is store on the disk.
 
 Project structure. 
 
 1. bin (wsgi entrypoint ) necessary to have a flask instance opend
 2. src : here is the bussines logic, read_data.py is responsible to read and send all the data via endpoints or custom commands. 
  a. test folder: unittests for read data layer.
  

Run and testing

# Test endpoints. 

Flask instance expose 4 endpoints:

/ - returns all data from json

/name - returns candidate name from json

/experience - returns candidate experience

/education - returns candidate education 

Run without docker. 

Troubleshooting

 Please be sure that you are in the root directory while execute bellow commands. 

1. run python3 -m venv env (create a virtual enviroment where we will install requirements for this project)
2. run pip3 install -r requirements.txt
3. run ./bin/run.sh

After third command we can navigate to http://127.0.0.1:8080 or use a rest read client(e.g. Postman)

Example of response from http://127.0.0.1:8080/education :
  {
      "education": [
          {
              "degree": "Bachelor's degree",
              "end_date": "jul-2012",
              "school": "University Vasile Alecsandri",
              "start_date": "oct-2009"
          }
      ]
  }
  
Running with docker

To build a containerised version of the API, run:

docker build . -t flask-app

To launch the containerised app, run:

docker run -p 5000:5000 flask-app

You should see your server boot up, and should be accessible as before.

Test with custom commands. 

There are 4 custom commands implemented ( commands.py )

In order to check the response run:
1. run python3 -m venv env
2. run pip3 install -r requirements.txt

After that, from root dir run in terminal:

python -m flask ** name of the command **

Available custom commands:

name
all_information
experience
education

E.g. 
python -m flask education returns: 
    [{'degree': "Bachelor's degree",
      'end_date': 'jul-2012',
      'school': 'University Vasile Alecsandri',
      'start_date': 'oct-2009'}]


 
