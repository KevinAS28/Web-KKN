from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField
import mypoll.models as mypoll_models

# class CardImagePlugin(CMSPluginBase):
#     model = mypoll_models.CardPluginModel
#     name = _("CardImage Plugin")
#     render_template = "card_plugin.html"
#     cache = False

#     def render(self, context, instance, placeholder):
#         context.update({
#             'instance': instance,
#             'placeholder': placeholder,
#         })
#         return context

# plugin_pool.register_plugin(CardImagePlugin)