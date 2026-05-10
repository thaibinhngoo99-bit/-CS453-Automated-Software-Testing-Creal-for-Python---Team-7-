from django.conf.urls import url

from test_app.views.home import Home
from test_app.views.ajax import Ajax

app_name = "test_app"

urlpatterns = [
    url(regex=r"^$", view=Home, name="home"),
    url(regex=r"^ajax$", view=Ajax, name="ajax"),
]
