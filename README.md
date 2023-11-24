# woodhouse_private_eatery










































namespacing to keep the project nice and clean from messy files, took so long before, i found a way to clean it up... 


from django.urls import include, path

urlpatterns = [
    path("author-polls/", include("polls.urls", namespace="author-polls")),   
    path("bookings/", include("polls.urls", namespace="bookings")),   
]


Where i found the idea for the not making bookings in the past:
- https://stackoverflow.com/questions/74227268/how-to-make-a-date-picker-that-does-not-select-previous-dates-in-django


where i came across the login_view: 
- https://forum.djangoproject.com/t/redirecting-user-to-page-after-login/14603/9


include tags useful for the login flow to remove the login and sign up buttons : 
- https://www.w3schools.com/django/showdjango.php?filename=demo_templates_include2

Exclude tags: 
- https://stackoverflow.com/questions/35752873/is-it-possible-to-exclude-footer-html-which-is-included-in-base-html-when-i-exte


