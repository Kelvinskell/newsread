# Brief Project Synopsis 
**NewsRead** is a python flask web application designed to be deployed as a containerized application.

This Web Application allows you to get the latest news from different parts of the world - culled from different news sources - right on one Web Page. 

So basically, it is a news content aggregator. 

**NewsRead** is highly customizable and offers the user a variety of options to chose from in selecting how thier news feed will be displayed. 
This includes country, language and category selections. 

This application has been 'Dockerized' and you can find the image on DockerHub: **`kelvinskell/newsread`**.

## Local Usage
You can run this application locally as a container on your server by applying the following steps:
 - Clone this repository.
 - Navigate to the project directory. 
 - Create a .env file in the directory and populate it with the value for the following parameter:
   - MYSQL_ROOT_PASSOWRD 
 - Also Create a .env file in the _application_ directory. 
 - Populate your _application/.env_ files with the values to these parameters:
   - DATABASE_PASSWORD
   - MYSQL_ROOT_PASSWORD
   - MYSQL_USER
   - MYSQL_HOST 
   - MYSQL_DB (The value for thsi should be 'newsread')
   - SECRET_KEY (The value for this should be '08dae760c2488d8a0dca1bfb')
   - API_KEY (The value for this should be'f39307bb61fb31ea2c458479762b9acc' or alternatively, create your own [MediaStack](https://mediastack.com/) API)

These values will be needed in order to correctly execute the _docker-compose_ command. 
   
 - Execute **`docker compose up`**

## Terraform automation

This application is specially designed to be deployed on **AWS Elastic Container Service (ECS)**.
There is a terraform directory attached which contains terraform code to automatically provision an ECS Cluster for you.
All you have to do then is execute the terraform code to have the application deployed on Your AWS ECS Cloud Infrastructure.
- Clone this repository.
- Navigate to the project directory.
- Switch in the _terraform_ directory.
- Execute `terraform plan`.
- If you are happy with the proposed changes, execute `terraform apply -auto-approve`

## Continuous Deployment
[Here]() is a comprehensive guide on how to use **AWS CodeDeploy** to automate the deployment of this application to ECS.

# Contributions 
This is an open source, active project with an MIT License. 
Contributions are highly welcome and will be appreciated. 
Just submit a pull request and I will respond. 
Also, if you find any bugs or other issues, please do well to submit a pull request.

I am always open to connections on [LinkedIn](https://www.linkedin.com/in/kelvin-onuchukwu-3460871a1)