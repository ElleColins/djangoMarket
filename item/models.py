from django.db import models


class Item(models.Model):
    objects = None

    def __init__(self):
        self.created_by = None
        self.category = None
        self.id = None

    def delete(self):
        pass


class Category:
    objects = None


def item():
    return None
