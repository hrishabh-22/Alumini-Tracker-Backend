from django.urls import path, include
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('user/', include('api.user.urls')),
    path('message/', include('api.allmessage.urls')),
    path('article/', include('api.article.urls')),
    path('project/', include('api.project.urls')),
    path('recommendation/', include('api.recommendation.urls'))
]
