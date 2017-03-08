from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

try:
    from djangocms_text_ckeditor.fields import HTMLField
except ImportError:
    from django.db.models.fields import TextField as HTMLField


# Add additional choices through the ``settings.py``.
# Use DJANGOCMS_OSCAR_PRODUCT_TEMPLATES
# or DJANGOCMS_OSCAR_VIEWED_TEMPLATES
def get_templates(plugin_label):
    choices = [
        ('default', _('Default')),
    ]
    choices += getattr(
        settings,
        'DJANGOCMS_OSCAR_{}_TEMPLATES'.format(plugin_label),
        [],
    )
    return choices


class FeaturedProduct(CMSPlugin):
    plugin_label = 'PRODUCT'

    title = models.CharField(
        verbose_name=_('Title'),
        max_length=255,
        blank=True,
    )
    product = models.ForeignKey('catalogue.Product',
                                verbose_name=_("Choose product"))
    description = HTMLField(verbose_name=_("Product description or advertising"),
                                           blank=True)
    template = models.CharField(
        verbose_name=_('Template'),
        choices=get_templates(plugin_label),
        default=get_templates(plugin_label)[0][0],
        max_length=255,
    )

    def __unicode__(self):
        return unicode(self.product)


class ViewedProducts(CMSPlugin):
    plugin_label = 'VIEWED'

    title = models.CharField(
        verbose_name=_('Title'),
        max_length=255,
        blank=True,
    )
    limit = models.IntegerField(default=0,
                                verbose_name=_('Limit'),
                                help_text=_("Show only the given number of recently "
                                            "viewed products. Set zero to show all."))
    template = models.CharField(
        verbose_name=_('Template'),
        choices=get_templates(plugin_label),
        default=get_templates(plugin_label)[0][0],
        max_length=255,
    )