# Brief Description 
**NewsRead** is a python flask web application built using a microservices architecture and deployed in the cloud.

This Web application allows you to get the latest news from different parts of the world - culled from different news sources - right on one Web page. 

So basically, it is a news content aggregator of sorts. 

The primary objective of this project is to demonstrate usage of Microservices in software design.

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
