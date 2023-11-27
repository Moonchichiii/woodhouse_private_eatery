# woodhouse_private_eatery









Layout of the project:

-   **Backend**: This is the project folder / base 

-   **App - Frontend**: The base of the frontend templates index.html / base.html

-   **App Accounts**: To gain access to the private eatery sign up & and login to book your table.

-   **App Bookings**: Handles the booking side of the project. 


- -   **App Menu**: For mangers of the site to easily change the menu and prices on the site. 


for the forms will use bootstraps form tags where i can,for ease of use . 

and also going with bootstrap cdn to make site responsive and out of the box layouts. 

https://django-bootstrap5.readthedocs.io/en/latest/templatetags.html 



namespacing to keep the project nice and clean from messy files, took so long before, i found a way to clean it up... 


from django.urls import include, path

urlpatterns = [
    path("author-polls/", include("polls.urls", namespace="author-polls")),   
    path("bookings/", include("polls.urls", namespace="bookings")),   
]


Where i found the idea for the not making bookings in the past 
https://stackoverflow.com/questions/74227268/how-to-make-a-date-picker-that-does-not-select-previous-dates-in-django


https://stackoverflow.com/questions/35752873/is-it-possible-to-exclude-footer-html-which-is-included-in-base-html-when-i-exte



https://realpython.com/python-time-module/#local-time


