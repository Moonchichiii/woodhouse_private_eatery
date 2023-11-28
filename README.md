# Woodhouse Bookings ***private eatery***

**👉 [Link to Live Project]([https://woodhouse-6b4519e75518.herokuapp.com](https://woodhouse-6b4519e75518.herokuapp.com))**


![screenshot](/readmecontent/images/topof.png)


------

# Table of Contents
 

1. [Project Goals](#project-goals)
2. [External User’s Goal](#external-users-goal)
3. [User Stories](#user-stories)
4. [Features](#features)
5. [Technologies Used](#technologies-used)
6. [Design and Planning Stages](#design-and-planning-stages)
7. [Dependencies](#dependencies)
8. [Building out the Backend](#building-out-the-backend)
9. [Development Environment: Gitpod](#development-environment-gitpod)
10. [Testing](#testing)
11. [Database Management: ElephantSQL PostgreSQL](#database-management-elephantsql-postgresql)
12. [Hosting Static Assets: Cloudinary](#hosting-static-assets-cloudinary)
13. [Deployment](#deployment)
14. [Credits & Tutorials](#credits-&-tutorials)
  

---



## Project Goals

  

This restaurant site is designed for efficiency, enabling users to register username and password. Once registered, they can book, edit, or delete their reservations.

  

Additionally incorporated a functionality for staff, to have the capability to create reservations for guests and also manage them by editing or deleting them

if needed. Handle a menu change to site on the same page, and login at the same login as guests,will be redirected to management page instead, when logged in as staff.

  

In terms of design, a minimalist website that's simple to navigate, and use of contrast in mind, also responsive so easily accessible across various devices.


---

  

### External User’s Goal


Looking for an intuitive and accessible booking experience, without to many options keeping it simple,  

Easy Booking dashboard Enables guests to conveniently make online reservations for their preferred number of guests, on  

flexible scheduling offers guests the flexibility to choose their preferred booking date and time slot, adding convenience to their planning. 

instant confirmation provides to reassure customers about their reservation details.

---

## User Stories
 

As a guest, upon first arrival, I can easily register using a simple sign-up form based on a username and password I choose.

 

Once logged in, my booking_id is linked to my created user account. After registration, i'm redirected to the booking dashboard where all

my bookings are displayed. Here, I can quickly edit or cancel any of my bookings.

  

I can still navigate around the entire site as a return button appears in place of the signup/login button,

allowing me to easily navigate back to the booking dashboard.

  

- Making a Reservation

  

If I have an existing booking, it's displayed as soon as I log in to the dashboard. If there are no bookings linked to my account, I can create a new reservation. The dashboard gives me the flexibility to edit or cancel any reservation, letting me adjust my plans as needed.



The logout option is conveniently located on the dashboard and returns me to the starting point of the website.

  
  

- As management

  

As a staff member, I log in with predefined credentials and am redirected to the admin panel. I need to effectively manage guests' reservations, including the ability to create, edit, or cancel bookings, and update the menu and prices.

  

---

[Back to top](#)  

## Features

  

- Date/Time-based bookings

  

- Edit or Cancel at any point

  

- Contact staff via Contact form

  

- Location inidication Map

  

**Staff Features:**

  

- Delete user account on the booking dashboard

  

- Manage bookings and update menu content

  
  
**Future Features:**

- Multiple table occupancies

  

---

  

## Technologies Used

  

- HTML

- CSS

- JavaScript

- Python + Django

  -----
  

**Frameworks:**

- Bootstrap

  

---

[Back to top](#)
  

## Design and Planning Stages

![Balsamiq](/readmecontent/images/1.png)

![Balsamiq](/readmecontent/images/2.png)

![Balsamiq](/readmecontent/images/3.png)   

After that used Justinmind to draw up the layout, and then a prebuild using codepen.io

![](/readmecontent/images/layoutplan.png)   

![](/readmecontent/images/)   

![](/readmecontent/images/)   


  

(screenshots from justinmind and codepen.io here :)

  
[Back to top](#)
---

  

## Dependencies

  
  

**Dependencies:** Part of my setup involved incorporating a range of dependencies, crucial for the functionality of my project.
  

-  `asgiref==3.7.2`: Essential for ASGI support, enabling asynchronous capabilities in Django projects.

-  `cloudinary==1.36.0`: Integrates Cloudinary services for managing and delivering media files in the cloud.

-  `coverage==7.3.1`: Tool for measuring code coverage to ensure thorough testing.

-  `dj-database-url==2.1.0`: Simplifies database configuration by using a URL.

-  `dj3-cloudinary-storage==0.0.6`: Django storage backend for Cloudinary, aiding in media asset management.

-  `Django==4.1`: The core Django web framework, providing the structure and tools for building the application.

-  `django-cors-headers==4.3.0`: Manages Cross-Origin Resource Sharing (CORS) in Django applications, important for API security.

-  `django-environ==0.11.2`: Helps manage environment variables in Django.

-  `django-filter==23.3`: Adds filtering capability to Django applications, useful for refining querysets.

-  `gunicorn==21.2.0`: A Python WSGI HTTP Server for UNIX, used for deploying Django applications.

-  `psycopg2-binary==2.9.7`: PostgreSQL adapter for Python, allowing Django to interact with PostgreSQL databases.

-  `python-decouple==3.8`: Separates settings parameters from code, making configuration more secure and scalable.

-  `pytz==2023.3.post1`: Brings timezone support to Python and Django.

-  `sqlparse==0.4.4`: A non-validating SQL parser for Python, useful for formatting SQL queries.

-  `urllib3==1.26.16`: A powerful HTTP client for Python, used to make requests to web services.

-  `django-bootstrap5==23.3`: Integrates Bootstrap 5 with Django for responsive web design.

-  `requests==2.31.0`: Simplifies making HTTP requests in Python, essential for API interactions.

  

---
[Back to top](#)
  

## Building out the Backend

I employed namespacing to maintain a clean project structure, free from cluttered files, this approach will keep the file organization clean. 

`from django.urls import include, path

urlpatterns = [

path("author-polls/", include("polls.urls", namespace="author-polls")),

path("bookings/", include("polls.urls", namespace="bookings")),

]`

- This project urls layout 

urlpatterns = [

    path('', include('frontend.urls', namespace='frontend')), 
    path('accounts/', include('accounts.urls', namespace='accounts')), 
    path('bookings/', include('bookings.urls', namespace='bookings')), 
    path('menu/', include('menu.urls', namespace='menu')), 
]
 

***Backend:*** This is the project folder / base.
  
App - ***Frontend:*** The base of the frontend templates, including index.html / base.html.
  
App ***Accounts:*** To gain access to the private eatery, sign up & and login to book your table.

App ***Bookings:*** Handles the booking side of the project.

App ***Menu:*** For managers of the site to easily change the menu and prices on the site.  

For the forms, I will use Bootstrap's form tags where I can, for ease of use. Also, going with Bootstrap CDN to make the site responsive and provide out-of-the-box layouts.
  

For security reasons i concealed the `SECRET_KEY`, which have been changed during the development, and also all other `API_KEYS` and updated it since the project's inception. I also revised my `settings.py` to prepare it for future deployment on Heroku.  

**Discovering `.env` and Implementation:** I discovered the utility of using `.env` with `decouple` for streamlined management in `settings.py`. This approach allowed for shorter, more manageable lines in the configuration file.

  
[Back to top](#)

---
  

## Development Environment: Gitpod

  

- Gitpod ide for the so don't have install everything on my computer and i jump in and edit from anywhere.   

---

## Testing


- Html Validation

- Css Validation

- Responsive

***Coverage***

 - [Coverage report](/readmecontent/images/coverage.png)

Commands: 

1. coverage run --source='.' manage.py test
2. coverage report
3. coverage html


  
[Back to top](#)
---
  
## Database Management: ElephantSQL PostgreSQL

- https://www.elephantsql.com

create and account and then you can create your own database, to use in your project,   

---

  

## Hosting Static Assets: Cloudinary

- Cloudinary hosts static assets like stylesheets, JavaScript files, images, and videos, optimizing media file management and performance.

- https://cloudinary.com  

---
 

## Deployment
 

- setting up the settings.py before.

- then pushing it to the main.



- https://www.heroku.com

  - Heroku provides a platform for easy deployment and scaling of the application.

-  **Steps for Deployment:**


***Connect the Heroku app to the GitHub repository***

Configure environment variables in Heroku, including `DISABLE_COLLECTSTATIC=1`.

Deploy the application from the main branch

Use the Heroku CLI to manage and scale the application.

  
[Back to top](#)
---

  

## Credits & Tutorials

  

<details>  <summary>Documentation and Tutorials</summary>

  

- Django Documentation: [Forms](https://docs.djangoproject.com/en/4.2/topics/forms/) and [Messages](https://docs.djangoproject.com/en/4.2/ref/contrib/messages/)

- Stack Overflow: [Using AuthenticationForm in Django](https://stackoverflow.com/questions/8421200/using-authenticationform-in-django)

- For preventing past date bookings: [Stack Overflow Discussion](https://stackoverflow.com/questions/74227268/how-to-make-a-date-picker-that-does-not-select-previous-dates-in-django)

- For the login_view concept: [Django Forum Thread](https://forum.djangoproject.com/t/redirecting-user-to-page-after-login/14603/9)

- Utilizing `include` tags for the login flow: [W3Schools Tutorial](https://www.w3schools.com/django/showdjango.php?filename=demo_templates_include2)

- Implementing `exclude` tags: [Stack Overflow Query](https://stackoverflow.com/questions/35752873/is-it-possible-to-exclude-footer-html-which-is-included-in-base-html-when-i-exte)

</details>

[Back to top](#)
