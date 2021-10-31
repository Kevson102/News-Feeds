# Phoenix News Feeds

## This app is called [Phoenix News Feeds](https://github.com/Kevson102/News-Feeds.git).

### **This project was done using Python 3.9** 

# DESCRIPTION

This is a **News** application application that will help  list and preview news articles from various News sources.   

The user will be able to:

* See various news sources on the homepage of the application.
* Select a news source and see all news articles from the selected news source in the application.
* See the image, description and the time a news article was created.
* Read a desired article by clicking on the article title.

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display news sources | **On page load** | List of various news sources is displayed per category |
| Display articles from a news source | **Click a news source** | Redirected to a page with a list of articles from the source |
| Display the preview of an article | **On page load** | Each article displays an image, title, description and publication date |
| Read an entire article | **Click an article** | Redirected to the news source's site to read the entire article |

### Prerequisites

The following are required to start working on the project from your local computer:

* A computer running on either Windows, MacOS or Ubuntu operating system installed with the following:

```
-Python version 3.9
-Flask
-Pip
-virtualenv
-Visual Studio
```

#### Dependencies
```
click==7.1.2
dominate==2.6.0
Flask==1.1.4
Flask-Bootstrap==3.3.7.1
Flask-Script==2.0.6
gunicorn==20.1.0
itsdangerous==1.1.0
Jinja2==2.11.3
MarkupSafe==2.0.1
visitor==0.1.3
Werkzeug==1.0.1
```

## Getting Started

* Clone this repo to your local computer.
* Have python3.9 installed in your computer.
* Navigate to the cloned project folder from the terminal.
* Create a virtual environment and access the folder via your virtual machine.
* Visit https://newsapi.org/ and register for an API key.
* Create start.sh file in the root directory and in it write the following lines:
```
 export NEWS_API_KEY='<Your-Api-Key>'
 python3.9 manage.py server
```
* Run ```chmod +x start.sh``` follwoed by ``` ./start.sh ``` while in the project folder to start the project.
* Once started, the project can be accessed on your localhost using the address: ``` http://127.0.0.1:5000/```
* Alternatively the application can be accessed by visiting 

## Technologies Used

* Python v3.8
* Boostrap
* Flask

## Deployed Link
```
https://phoenix-news.herokuapp.com/
```

## License

<a href="LICENCE.MD" target = "_blank">MIT</a>

Copyright (c) 2021 **Phoenix News Feeds Web Application-Nyambura Kelvin Njuguna**