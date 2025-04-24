from bson import ObjectId
from djongo import models

class ObjectIdField(models.Field):
    def get_prep_value(self, value):
        if not isinstance(value, ObjectId):
            return ObjectId(value)
        return value

class User(models.Model):
    id = ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    class Meta:
        db_table = "users"

class Team(models.Model):
    id = ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100)
    members = models.JSONField()
    class Meta:
        db_table = "teams"

class Activity(models.Model):
    id = ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    class Meta:
        db_table = "activity"

class Leaderboard(models.Model):
    id = ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    class Meta:
        db_table = "leaderboard"

class Workout(models.Model):
    id = ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        db_table = "workouts"
