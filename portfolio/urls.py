from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('greeting/', views.greeting, name='greeting'),
    # path('goodbye/', views.goodbye, name='goodbye'),
    # path('adult/<int:age>/', views.adult, name='adult'),

#     path('simple/', views.simple, name='simple'),
#     path('dynamic/<str:name>/', views.dynamic, name='dynamic'),

#     path('statics/', views.statics, name='static')

    # path('', views.index, name='index'),
    # path('herencia/', views.herencia, name='herencia'),
    # path('ejemplo/', views.ejemplo, name='ejemplo'),
    # path('otra/', views.otra, name='otra')

    path('', views.index, name='index'),
    path('portfolio/', views.portfolio, name='portfolio'),

    path('projects/', include('projects.urls'))
]
