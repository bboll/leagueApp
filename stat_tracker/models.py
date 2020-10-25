from django.db import models

#TODO create either an additional Player class or use existing login class created by django; research required

class Summoner(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=16)
    level = models.IntegerField()
    date_updated = models.DateTimeField(auto_now_add=True)

class League(models.Model):
    pass

class Rules(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    league_id = models.ForeignKey('League', on_delete=models.CASCADE)
    
    #TODO build out ruleset

class Game(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    game_id = models.PositiveIntegerField()

class Match(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    league_id = models.ForeignKey('League', on_delete=models.CASCADE)
    
    #TODO player1 & playe2 as ForeignKey to Player/Account relation; see TODO at top-of-file
