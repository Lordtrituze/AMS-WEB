from django.urls import path
from app.views.login_view import view

urlpatterns = [
    path('login/', view.login_get, name='login_get'),
    path('login_post/', view.login_page_post, name='login_post'),
    path('logout/', view.logout_view, name='logout'),
    path('home/', view.home_page, name='home_page'),
]
