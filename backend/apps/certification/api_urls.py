from django.urls import path

from rest_framework.routers import SimpleRouter

from backend.apps.certification import views

router = SimpleRouter()
router.register("managelink", views.AdminLinkViewSet, base_name='managelink')

app_name = 'certification'
urlpatterns = [
    path('verification/<uuid:pk>/', views.ClientUpdateLinkView, name='verification'),
] + router.urls
print(urlpatterns)
