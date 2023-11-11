from django.urls import path
from .views import *


urlpatterns = [
    path('get_logo/', get_logo),
    path('get_news_ad_banner/', get_news_ad_banner),
    path('get_calendar_ad/', get_calendar_ad),
    path('get_video_banner/', get_video_banner),
    path('get_rating_ad/', get_rating_ad),
    path('get_rating/<int:pk>/', get_rating),
    path('get_team_ad/', get_team_ad),
    path('get_shop_ad/', get_shop_ad),
    path('get_sponsors/', get_sponsors),
    path('get_info/', get_info),
    path('get_news_banner/', get_news_banner),
    path('get_match_ad/', get_match_ad),
    path('get_news/', get_news),
    path('get_all_players/', get_all_players),
    path('get_players_by_position/<int:pk>/', get_players_by_position),
    path('get_management_banner/', get_management_banner),
    path('get_coaches/', get_coaches),
    path('get_management/', get_management),
    path('get_club_banner/', get_club_banner),
    path('get_club_page_post/', get_club_page_post),
    path('get_academy_page_post/', get_academy_page_post),
    path('get_academy_banner/', get_academy_banner),
    path('get_shop_banner/', get_shop_banner),
    path('get_shop/', get_shop),
    path('get_all_stadiums/', get_all_stadiums),
    path('get_stadium_by_id/<int:pk>/', get_stadium_by_id)
]