from django.dispatch import receiver
from django.urls import resolve, reverse
from django.utils.translation import gettext_lazy as _
from pretalx.common.signals import register_data_exporters
from pretalx.orga.signals import nav_event


@receiver(nav_event, dispatch_uid="csv_nav")
def navbar_info(sender, request, **kwargs):
    url = resolve(request.path_info)
    return [
        {
            "label": _("CSV export"),
            "icon": "heart",
            "url": reverse(
                "plugins:pretalx_csv_export:settings", kwargs={"event": sender.slug}
            ),
            "active": "pretalx_csv_export" in url.namespace,
        }
    ]


@receiver(register_data_exporters, dispatch_uid="exporter_csv_submissions")
def register_data_exporter(sender, **kwargs):
    from .exporter import CSVExporter

    return CSVExporter
