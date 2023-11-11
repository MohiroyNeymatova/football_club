from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField


class Info(models.Model):
    logo = models.ImageField(upload_to='logos/')
    bio = models.CharField(max_length=250)
    phone = models.IntegerField()
    email = models.EmailField()
    inst = models.URLField()
    tg = models.URLField()
    fb = models.URLField()
    yt = models.URLField()
    tw = models.URLField()


class NewsCategory(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class New(models.Model):
    image = models.ImageField(upload_to='news/')
    title = models.CharField(max_length=250)
    date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Team(models.Model):
    name = models.CharField(max_length=250)
    logo = models.ImageField(upload_to='logos/')

    def __str__(self):
        return self.name


class Tournament(models.Model):
    name = models.CharField(max_length=250)
    logo = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class Match(models.Model):
    first_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team1')
    second_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team2')
    date = models.DateField()
    time = models.TimeField()
    ticket_price = models.DecimalField(max_digits=25, decimal_places=2)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)

    def __str__(self):
        return self.second_team.name


class Rating(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()
    year = models.IntegerField()
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    games_quantity = models.IntegerField()
    wins = models.IntegerField()
    equal = models.IntegerField()
    lost = models.IntegerField()
    goals = models.IntegerField()
    lost_goals = models.IntegerField()

    def __str__(self):
        return self.team.name


class VideoBanner(models.Model):
    video = models.URLField()
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='videos/')

    def __str__(self):
        return self.title


class Position(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Player(models.Model):
    image = models.ImageField(upload_to='team/')
    jersey_number = models.IntegerField()
    name = models.CharField(max_length=250)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    played_games = models.IntegerField()
    played_minutes = models.IntegerField()
    start = models.IntegerField()
    sub_off = models.IntegerField()
    is_main_team = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.ImageField(upload_to='products/')


class Product(models.Model):
    image = models.ManyToManyField(ProductImage)
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=25, decimal_places=2)

    def __str__(self):
        return self.name


class Stadium(models.Model):
    name = models.CharField(max_length=250)
    area = models.IntegerField()
    seats = models.IntegerField()
    sectors = models.IntegerField()
    location = models.CharField(max_length=250)
    phone_number = models.IntegerField()
    history = models.TextField()
    body = RichTextUploadingField(blank=True)

    def __str__(self):
        return self.name


class Sponsor(models.Model):
    logo = models.ImageField(upload_to='sponsors/')


class NewsBanner(models.Model):
    image = models.ImageField(upload_to='banners/')


class TeamBanner(models.Model):
    image = models.ImageField(upload_to='banners/')


class ManagementBanner(models.Model):
    image = models.ImageField(upload_to='banners/')


class Coach(models.Model):
    photo = models.ImageField(upload_to='coaches/')
    name = models.CharField(max_length=250)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Management(models.Model):
    photo = models.ImageField(upload_to='coaches/')
    name = models.CharField(max_length=250)
    bio = models.TextField()

    def __str__(self):
        return self.name


class ClubBanner(models.Model):
    image = models.ImageField(upload_to='banners/')


class ClubPagePost(models.Model):
    title = models.CharField(
        _("Text Title"), max_length=250,
        null=False, blank=False
    )
    body = RichTextUploadingField()

    def __str__(self):
        return self.title


class AcademyBanner(models.Model):
    image = models.ImageField(upload_to='banners/')


class AcademyPagePost(models.Model):
    title = models.CharField(
        _("Text Title"), max_length=250,
        null=False, blank=False
    )
    body = RichTextUploadingField()

    def __str__(self):
        return self.title


class ShopBanner(models.Model):
    bg_image = models.ImageField(upload_to='banners/')
    image = models.ImageField(upload_to='shop/')
    text = models.CharField(max_length=250)


