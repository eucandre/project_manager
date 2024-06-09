from django.db import models
from app_user.models import User
from app_areas.models import Field
from app_status.models import Status


class Project(models.Model):
    title = models.CharField(max_length=255)
    start = models.DateField()
    end = models.DateField()
    cost = models.CharField(max_length=15,blank=True, null=True)
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, related_name='state_project')
    gols = models.TextField()
    field = models.ManyToManyField(Field, related_name='field')
    mebmers = models.ManyToManyField(
        User)
    responsable = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='responseble')
    attachment = models.FileField(upload_to='tarefas', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/projects/%i/" % (self.pk)

    class Meta:
        verbose_name_plural = 'Projetos'
