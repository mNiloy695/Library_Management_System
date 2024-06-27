from django.urls import path
from . import views
from Books.views import BorrowedBookView

urlpatterns = [
    path('registration/',views.RegistrationView.as_view(),name='registration'),
    path('login/',views.UserLoginView.as_view(),name='login'),
    path('logout/',views.UserLogoutView.as_view(),name='logout'),
    path('deposite/',views.DeposteView.as_view(),name='deposite'),
    path('profile/',BorrowedBookView.as_view(),name='BorrowedBookView'),
]
