from django.contrib import admin
from .models import Question,Choice, Voter, Vote

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Voter)
admin.site.register(Vote)
# Register your models here.
