# Brief Project Synopsis 
**NewsRead** is a python flask web application deployed in the cloud.

This Web Application allows you to get the latest news from different parts of the world - culled from different news sources - right on one Web Page. 

So basically, it is a news content aggregator. 

**NewsRead** is highly customizable and offers the user a variety of options to chose from in selecting how thier news feed will be displayed. 
This includes country, language and category selections. 


# Project Description 
This application is made up of three units:
 - Frontend service
 - Login service
 - News service 

### Frontend Service 
The Frontend service of this application is responsible for displaying the home page and directing users to the Login Service. 


### Login Service 
The login service utilises the flask login manager as well as intricate python code, to register and authenticate users. 

The MYSQL relational database management system is utilised extensively in the creaton and management of users. 
MYSQL is used here to:
 - Create a database. 
 - Create a user accounts table. 
 - Create new user accounts. 
 - Store user credentials. 
 - Authenticate users.
Authenticated users are then redirected to the News Service. 
 

### News Service 
NewsRead uses API from [Mediastack](https://www.mediastack.com) to fetch news content. 
This service extensively utilises jinja2 templating engine to nicely display python objects.
Python objects in this context are formatted data from the JSON object returned by the API. 

This service also provides a customization page for users to choose what news to appear in their feed. 


# Usage 
**This project is still in the pipelines and not yet ready for production.**

# Contributions 
This is an open source, active project with an MIT License. 
Contributions are highly welcome and will be appreciated. 
Just submit a pull request and I will respond. 
Also, if you find any bugs or other issues, please do well to submit a pull request.

**N.B: I hope to migrate this web application from a monolithic architecture into a fully fledged microservice architecture sometime in the near future.** 

I am always open to connections on [LinkedIn](https://www.linkedin.com/in/kelvin-onuchukwu-3460871a1) 




