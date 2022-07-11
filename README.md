# Brief Project Description 
**NewsRead** is a python flask web application built using a microservices architecture and deployed in the cloud.

This Web Application allows you to get the latest news from different parts of the world - culled from different news sources - right on one Web Page. 

So basically, it is a news content aggregator. 

NewsRead is highly customizable and offers the user a variety of options to chose from in selecting how thier news feed will be displayed. 
This includes country, language and category selections. 

A secondary objective of this project is to demonstrate usage of Microservices in software design.

# What Are Microservices? 
Microservices, as explained by [Redhat](https://www.redhat.com/en/topics/microservices/what-are-microservices) are an an architectural approach to building applications. 

As an architectural framework, microservices are distributed and loosely coupled, such that a change in one microservice does not break the entire app. 

Two major benefits of this loosely coupled design are:
 - Reliability
 - Scalability 

Microservices are highly reliable in that malfunction of one part of the application does not necessarily affect the entire service. 
Due to their loose architecture, each microservice can be scaled up or down - as needed - without affecting the entire service.
Microservices underlie much of Modern Devops and Software engineering. 

This application is divided into three microservices:
 - Frontend service
 - Login service
 - News service 

### Frontend Service 
The Frontend microservice of this application is responsible for displaying the home page and directing users to the Login Service. 

This service runs on port 5000

### Login Service 
The login service utilises the flask login manager as well as intricate python code, to register and authenticate users. 

The MYSQL relational database management system is utilised extensively in the Creaton and management of users. 
MYSQ is used here to:
 - Create a database. 
 - Create a user accounts table. 
 - Create new user accounts. 
 - Store user credentials. 
 - Authenticate users. 
This service runs on port 5001
NewsRead uses API from [Mediastack](https://www.mediastack.com) to fetch news content. 

