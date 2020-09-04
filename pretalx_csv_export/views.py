from django.views.generic import TemplateView

from pretalx.common.mixins.views import PermissionRequired


class SettingsView(PermissionRequired, TemplateView):
    permission_required = 'orga.change_settings'
    template_name = 'pretalx_csv_export/settings.html'

    def get_permission_object(self):
        return self.request.event


class ExportView(PermissionRequired, TemplateView):
    permission_required = 'orga.view_schedule'
    template_name = 'pretalx_csv_export/export.csv'

    def get_permission_object(self):
        return self.request.event
