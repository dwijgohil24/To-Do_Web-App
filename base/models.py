from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

#Creating one class or table in db name Task with the following attributes extended from model.models.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True )  #the user who has created the task, applying one to many relation (means one user can have multiple task) using foreign key, with on delete cascade means if the user is deleted all the child task made by him will be deleted, and the value will be shown as null.
    title = models.CharField(max_length=2000) #title of the task 
    description = models.TextField(null = True, blank = True )#description of the task
    complete = models.BooleanField(default=False)#status of the task, if it is complete or not
    created = models.DateTimeField(auto_now_add=True)#when the task was created. AutoNowAdd take the snapshot of the datetime and making it true helps in autopopulate the datetime.

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete']


