from django.db import models
from app_user.models import User
from app_project.models import Project
from app_status.models import Status


class FollowUp(models.Model):
    title = models.CharField(max_length=255)
    start = models.DateField()
    end = models.DateField()
    gols = models.TextField()
    cost = models.FloatField(blank=True, null=True)
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, related_name='state_marco')
    id_projet = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='titulos')
    members = models.ManyToManyField(
        User)
    responsable = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='names')
    attachment = models.FileField(upload_to='tarefas', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Marco de tarefas realizadas'
