from django.urls import path
from app.views import news, news_detail, homePageView

urlpatterns = [
    path('', homePageView, name='home_page_view'),
    path('all/', news, name='news_list'),
    path("<int:id>/", news_detail, name="news_detail"),
]
