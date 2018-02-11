from django.apps import AppConfig
from django.utils.translation import ugettext_lazy


class PluginApp(AppConfig):
    name = 'pretalx_csv_export'
    verbose_name = 'CSV exports for pretalx'

    class PretalxPluginMeta:
        name = ugettext_lazy('CSV exports for pretalx')
        author = 'Tobias Kunze'
        description = ugettext_lazy('Exports in CSV and related formats for pretalx')
        visible = True
        version = '0.0.0'

    def ready(self):
        from . import signals  # NOQA


default_app_config = 'pretalx_csv_export.PluginApp'
