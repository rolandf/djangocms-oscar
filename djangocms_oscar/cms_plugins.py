from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from oscar.apps.customer import history

from . import models


class FeaturedProductPlugin(CMSPluginBase):
    module = _("Shop")
    model = models.FeaturedProduct
    name = _("Featured product")
    admin_preview = True

    def get_render_template(self, context, instance, placeholder):
        return 'djangocms_oscar/plugins/featured_product/{}/product.html'.format(instance.template)

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


class ViewedProducts(CMSPluginBase):
    module = _("Shop")
    name = _("Recently Viewed Products")
    model = models.ViewedProducts
    admin_preview = True

    def get_render_template(self, context, instance, placeholder):
        return 'djangocms_oscar/plugins/viewed_products/{}/viewed_products.html'.format(instance.template)

    def render(self, context, instance, placeholder):
        request = context['request']
        products = history.get(request)
        if instance.limit > 0:
            products = products[:instance.limit]
        context.update({'products': products,
                        'request': request,
                        'instance': instance})
        return context


plugin_pool.register_plugin(ViewedProducts)
plugin_pool.register_plugin(FeaturedProductPlugin)
