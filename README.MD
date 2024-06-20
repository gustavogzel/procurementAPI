# Backend of the project Procurement Dasboard
## Problem :
Generates a back-end project to consume the procurement data for a procurement government dashboard.

## Solution Approach:
This project is a modern web application that is powered by a REST API. That way, it can separate the front-end code from the back-end logic, and users can interact with the interface dynamically. 

It has created a foundation with a basic Flask project and added endpoints, which you connected to a Postgres database. Moreover, it can be tested with API through Swagger UI API documentation.

This project uses the database loaded in project dataloader
https://github.com/gustavogzel/dataloader

## Explanation


make sure uses the right parameters in config.py 
    app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://pstguser:pstg123@'+ip_databse+'/contrataciones'

When building the docker image use

docker build -t procurement_api:latest .

When runing the container set the ip asigned to the database in the bridge

docker run -e IP_DB=172.17.0.2 -p 8000:8000 procurement_api:latest 



