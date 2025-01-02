from django.contrib import admin
from django.urls import path
from home import views

# django admin changes
admin.site.site_header = "Login to Administration"
admin.site.site_title = "Welocome to Dashboard"
admin.site.index_title = "Welocome to Portal"


urlpatterns = [
    path('', views.home, name='home')
]
