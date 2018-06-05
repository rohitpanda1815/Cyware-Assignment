from __future__ import unicode_literals
from datetime import datetime,date
from django.db import models
from django.contrib.auth.models import User

class User(User):
    timestamp = models.DateTimeField(default=datetime.now(),blank=True,null=True)

