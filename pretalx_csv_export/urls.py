from django.urls import re_path

from . import views

urlpatterns = [
    re_path(
        r'^orga/event/(?P<event>[^/]+)/plugins/csv_settings',
        views.SettingsView.as_view(),
        name='settings',
    ),
    re_path(
        r'^orga/event/(?P<event>[^/]+)/plugins/export.csv',
        views.ExportView.as_view(),
        name='export',
    ),
]
