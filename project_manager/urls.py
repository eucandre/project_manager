from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('app_user.urls')),
    path('projects/', include('app_project.urls'), name='projects'),
    path("organs/", include("app_orgaos.urls"), name="ogans"),
    path("fields/", include("app_areas.urls"), name="fields"),
    path("status/", include("app_status.urls"), name="status"),
    path("tasks/", include("app_tarefas.urls"), name="task"),
    path("functions/", include("app_funcoes.urls"), name="functions"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
