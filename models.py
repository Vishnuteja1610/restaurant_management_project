from django.db import models

class Resturant(models.Model):
    opening_days = models.CharField(
        max_length=50,
        help_text="Comma-separated days, e.g. 'Mon,Tue,Wed,Thu,Fri'"
    )