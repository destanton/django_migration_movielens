from django.db import models


class Rater(models.Model):
    age = models.IntegerField
    gender = models.CharField(max_length=20)
    occupation = models.CharField(max_length=40)
    zip_code = models.CharField(max_length=15)


class Item(models.Model):
    movie_title = models.CharField(max_length=150)
    release_date = models.CharField(max_length=30)
    video_release_date = models.CharField(max_length=50)
    imdb_url = models.CharField(max_length=150)
    unknown = models.IntegerField
    action = models.IntegerField
    adventure = models.IntegerField
    animation = models.IntegerField
    children = models.IntegerField
    comdey = models.IntegerField
    crime = models.IntegerField
    documentary = models.IntegerField
    drama = models.IntegerField
    fantasy = models.IntegerField
    film_noir = models.IntegerField
    horror = models.IntegerField
    musical = models.IntegerField
    mystery = models.IntegerField
    romanace = models.IntegerField
    sci_fi = models.IntegerField
    thriller = models.IntegerField
    war = models.IntegerField
    western = models.IntegerField

    def __str__(self):
        return self.movie_title


class Data(models.Model):
    rater_id = models.ForeignKey(Rater)
    item_id = models.ForeignKey(Item)
    rating = models.IntegerField
    time_stamp = models.IntegerField
