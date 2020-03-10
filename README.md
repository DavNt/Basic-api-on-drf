# Task101

Joiners task

## Description

Create a REST API using django rest framework
Tools: Python 3, DRF and Django https://www.django-rest-framework.org/


-GET / List end point
- Retrieves data from https://picsum.photos/ and shows it in view.
- Initial data must be loaded via a management command that you can run from a command line and stored in a model.

-GET / id
- Retrieves a picture by id

-POST / 
- Post give a user ability to post new photo
- Structure for post data 
    
        "id": "0",
        "author": "Alejandro Escamilla",
        "width": 5616,
        "height": 3744,
        "url": "https://unsplash.com/...",
        "download_url": "https://picsum.photos/..."
    