from cms.plugin_base import CMSPluginBase, CMSPlugin
from cms.plugin_pool import plugin_pool
from polls_cms_integration.models import PollPluginModel
from django.utils.translation import gettext as _
import polls_cms_integration.models as mypoll_models

@plugin_pool.register_plugin  # register the plugin
class PollPluginPublisher(CMSPluginBase):
    model = PollPluginModel  # model where plugin data are saved
    module = _("Polls")
    name = _("Poll Plugin")  # name of the plugin in the interface
    render_template = "polls_cms_integration/poll_plugin.html"
    
    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context



@plugin_pool.register_plugin  # register the plugin
class HomeCardImagePlugin(CMSPluginBase):
    model = mypoll_models.HomeCardImagePlugin
    module = _("Polls")
    name = _("Custom Home Card Image Plugin")
    render_template = "card_plugin.html"
    cache = False

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            
        })
        return context

@plugin_pool.register_plugin  # register the plugin
class CardImagePlugin(CMSPluginBase):
    model = mypoll_models.HomeCardImagePlugin
    module = _("Polls")
    name = _("Custom Card Image Plugin")
    render_template = "card_plugin.html"
    cache = False

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            
        })
        return context


@plugin_pool.register_plugin  # register the plugin
class CardRowPlugin(CMSPluginBase):
    # model = mypoll_models.ACardPlugin
    module = _("Polls")
    name = _("Custom Card Rows Plugin")
    render_template = "home_card_row.html"
    cache = False
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            
        })
        return context


