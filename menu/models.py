from django.db import models

from base.models.helpers.date_time_model import DateTimeModel


# Create your models here.

class MenuModel(DateTimeModel):
    dishes = models.OneToOneField('dishes.DishesModel', on_delete=models.CASCADE, related_name="menu_dishes")

    # def __str__(self):
    #     return self.name