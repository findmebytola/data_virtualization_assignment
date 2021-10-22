from django.db import models


class BookInfo(models.Model):
    title = models.CharField(max_length=255)


class Indicator(models.Model):

    def __str__(self) -> str:
        return self.scorecard_name

    SCORE = [
        (0, "Not yet achieved"),
        (1, "Patially achieved"),
        (2, "Fully achieved"),
    ]
    scorecard_name = models.CharField(max_length=255)
    step = models.IntegerField()
    milestone = models.CharField(max_length=255)
    score = models.IntegerField(choices=SCORE)
    narrative = models.TextField(max_length=700)
    year = models.IntegerField()
