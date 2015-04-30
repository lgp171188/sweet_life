from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers
from app.views import (
    LabelViewSet,
    ReadingViewSet,
    ListLabelsView
)

router = routers.DefaultRouter()
router.register(r'labels', LabelViewSet)
router.register(r'readings', ReadingViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'sweet_life.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', ListLabelsView.as_view(), name='list_labels'),
    url(r'^api/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
