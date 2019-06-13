from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^orga/event/(?P<event>[^/]+)/plugins/csv_settings',
        views.SettingsView.as_view(),
        name='settings',
    ),
    url(
        r'^orga/event/(?P<event>[^/]+)/plugins/export.csv',
        views.ExportView.as_view(),
        name='export',
    ),
]
