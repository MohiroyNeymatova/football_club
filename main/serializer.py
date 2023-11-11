from rest_framework import serializers
from .models import *


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ['id', 'logo']


class NewsAdBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ['image', 'title']


class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Match
        fields = ['tournament', 'date', 'second_team', 'first_team']


class VideoBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoBanner
        fields = "__all__"


class RatingAdSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Rating
        fields = ['team', 'points']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Rating
        fields = "__all__"


class TeamAdSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Player
        exclude = ['is_main_team']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Product
        fields = "__all__"


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = "__all__"


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__"


class NewsBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsBanner
        fields = "__all__"


class MatchAdSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Match
        exclude = ['ticket_price', 'tournament']


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = New
        fields = "__all__"


class PlayersSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Player
        fields = "__all__"


class ManagementBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagementBanner
        fields = "__all__"


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = "__all__"


class ManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Management
        fields = "__all__"


class ClubBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubBanner
        fields = "__all__"


class ClubPagePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubPagePost
        fields = "__all__"


class AcademyPagePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademyPagePost
        fields = "__all__"


class AcademyBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademyBanner
        fields = "__all__"


class ShopBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopBanner
        fields = "__all__"


class MiniStadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = ['name', 'history', 'area', 'seats', 'sectors', 'location', 'phone_number']


class SingleStadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = ['name', 'history', 'body']