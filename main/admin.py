from django.contrib import admin
from .models import *

admin.site.register([Comment, Like, News, Posts, Stories, UserProfile])