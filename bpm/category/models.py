from django.db import models
from bpm.base.models import NameDescAbstract

class Category(NameDescAbstract):
    
    def __str__(self):
        return self.name

class SubCategory(NameDescAbstract):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')


    def __str__(self):
        return self.name

class SubSubCategory(NameDescAbstract):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='subsubcategories')

    def __str__(self):
        return self.name
