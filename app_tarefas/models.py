from django.db import models
from app_marco.models import FollowUp
from app_project.models import Project
from app_user.models import User
from app_status.models import Status
from django.utils import timezone


class Task(models.Model):
    title = models.CharField(max_length=255)
    id_project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name= 'project_of_the_task')
    id_marco = models.ForeignKey(
        FollowUp, on_delete=models.CASCADE, blank=True, null=True)
    goals = models.TextField()
    cost = models.FloatField(blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='state_task')
    responsable = models.ForeignKey(User, on_delete=models.CASCADE)
    dependencies = models.CharField(max_length=255, blank=True, null=True)
    attachment = models.FileField(upload_to='tarefas',blank=True, null=True)
    start = models.DateField()
    end = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
       
    class Meta:
        verbose_name_plural = 'Tarefas a serem realizadas'
    
    