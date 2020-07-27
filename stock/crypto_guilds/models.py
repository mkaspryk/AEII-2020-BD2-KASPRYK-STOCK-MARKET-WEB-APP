from django.db import models

class Guild(models.Model):
    guild_name = models.CharField(max_length=50)
    
