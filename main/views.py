from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
import datetime


@api_view(['GET'])
def get_logo(request):
    data = LogoSerializer(Info.objects.last(), many=False).data
    return Response(data)


@api_view(['GET'])
def get_news_ad_banner(request):
    data = NewsAdBannerSerializer(New.objects.all().order_by('-id')[:3], many=True).data
    return Response(data)


@api_view(['GET'])
def get_calendar_ad(request):
    data = CalendarSerializer(Match.objects.all().order_by('-id')[:3], many=True).data
    return Response(data)


@api_view(['GET'])
def get_video_banner(request):
    data = VideoBannerSerializer(VideoBanner.objects.all().order_by('-id')[:4], many=True).data
    return Response(data)


@api_view(['GET'])
def get_rating_ad(request):
    data = RatingAdSerializer(Rating.objects.filter(tournament_id=1, year=2023).order_by('-points'), many=True).data
    return Response(data)


@api_view(['GET'])
def get_rating(request, pk):
    year = request.POST['year']
    data = RatingSerializer(Rating.objects.filter(tournament_id=pk, year=year).order_by('-points'), many=True).data
    return Response(data)


@api_view(['GET'])
def get_team_ad(request):
    data = TeamAdSerializer(Player.objects.all().order_by('-id')[:3], many=True).data
    return Response(data)


@api_view(['GET'])
def get_shop_ad(request):
    data = ProductSerializer(Product.objects.all().order_by('-id')[:6], many=True).data
    return Response(data)


@api_view(['GET'])
def get_sponsors(request):
    data = SponsorSerializer(Sponsor.objects.all(), many=True).data
    return Response(data)


@api_view(['GET'])
def get_info(request):
    data = InfoSerializer(Info.objects.last(), many=False).data
    return Response(data)


@api_view(['GET'])
def get_news_banner(request):
    data = NewsBannerSerializer(NewsBanner.objects.last(), many=False).data
    return Response(data)


@api_view(['GET'])
def get_match_ad(request):
    dt_now = datetime.datetime.now()
    data = MatchAdSerializer(Match.objects.filter(date=dt_now), many=True).data
    return Response(data)


@api_view(['GET'])
def get_news(request):
    data = NewsSerializer(New.objects.all().order_by('-id'), many=True).data
    return Response(data)


@api_view(['GET'])
def get_all_players(request):
    data = PlayersSerializer(Player.objects.all(), many=True).data
    return Response(data)


@api_view(['GET'])
def get_players_by_position(request, pk):
    data = PlayersSerializer(Player.objects.filter(position=pk), many=True).data
    return Response(data)


@api_view(['GET'])
def get_management_banner(request):
    data = ManagementBannerSerializer(ManagementBanner.objects.last(), many=False).data
    return Response(data)


@api_view(['GET'])
def get_coaches(request):
    data = CoachSerializer(Coach.objects.all(), many=True).data
    return Response(data)


@api_view(['GET'])
def get_management(request):
    data = ManagementSerializer(Management.objects.all(), many=True).data
    return Response(data)


@api_view(['GET'])
def get_club_banner(request):
    data = ClubBannerSerializer(ClubBanner.objects.last(), many=False).data
    return Response(data)


@api_view(['GET'])
def get_club_page_post(request):
    data = ClubPagePostSerializer(ClubPagePost.objects.last(), many=False).data
    return Response(data)


@api_view(['GET'])
def get_academy_banner(request):
    data = AcademyBannerSerializer(AcademyBanner.objects.last(), many=False).data
    return Response(data)


@api_view(['GET'])
def get_academy_page_post(request):
    data = AcademyPagePostSerializer(AcademyPagePost.objects.last(), many=False).data
    return Response(data)


@api_view(['GET'])
def get_shop_banner(request):
    data = ShopBannerSerializer(ShopBanner.objects.last(), many=False).data
    return Response(data)


@api_view(['GET'])
def get_shop(request):
    data = ProductSerializer(Product.objects.all(), many=True).data
    return Response(data)


@api_view(['GET'])
def get_all_stadiums(request):
    data = MiniStadiumSerializer(Stadium.objects.all(), many=True).data
    return Response(data)


@api_view(['GET'])
def get_stadium_by_id(request, pk):
    data = SingleStadiumSerializer(Stadium.objects.get(id=pk), many=False).data
    return Response(data)
