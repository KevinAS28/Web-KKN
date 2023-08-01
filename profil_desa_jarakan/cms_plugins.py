from cms.plugin_base import CMSPluginBase, CMSPlugin
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext as _
from profil_desa_jarakan import models as jarakan_models

@plugin_pool.register_plugin  # register the plugin
class HomeCardImagePlugin(CMSPluginBase):
    model = jarakan_models.HomeCardImagePlugin
    module = _("Desa Jarakan")
    name = _("Card Image Plugin")
    render_template = "card_plugin.html"
    cache = False

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            
        })
        return context

@plugin_pool.register_plugin  # register the plugin
class CardImagePlugin(CMSPluginBase):
    model = jarakan_models.HomeCardImagePlugin
    module = _("Desa Jarakan")
    name = _("---")
    render_template = "card_plugin.html"
    cache = False

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            
        })
        return context

@plugin_pool.register_plugin  # register the plugin
class CardImageWidePlugin(CMSPluginBase):
    model = jarakan_models.HomeCardImageWidePlugin
    module = _("Desa Jarakan")
    name = _("Card Wide")
    render_template = "wide_card.html"
    cache = False

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            
        })
        return context

@plugin_pool.register_plugin  # register the plugin
class CardHomeBeritaPlugin(CMSPluginBase):
    model = jarakan_models.HomeBeritaCardPlugin
    module = _("Desa Jarakan")
    name = _("Card Berita Home")
    render_template = "berita_home.html"
    cache = False

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            
        })
        return context

@plugin_pool.register_plugin  # register the plugin
class CardRowPlugin(CMSPluginBase):
    # model = jarakan_models.ACardPlugin
    module = _("Custom")
    name = _("Custom Card Rows Plugin")
    render_template = "home_card_row.html"
    cache = False
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            
        })
        return context
 
@plugin_pool.register_plugin  # register the plugin
class PejabatPlugin(CMSPluginBase):
    model = jarakan_models.PejabatCardPlugin
    module = _("Desa Jarakan")
    name = _("Pejabat Plugin")
    render_template = "pejabat_card.html"
    cache = False

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            
        })
        return context

@plugin_pool.register_plugin  # register the plugin
class SmallGalleryPlugin(CMSPluginBase):
    model = jarakan_models.SmallGalleryPlugin
    module = _("Desa Jarakan")
    name = _("Small Galery")
    render_template = "small_gallery.html"
    cache = False

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            
        })
        return context

@plugin_pool.register_plugin  # register the plugin
class PetaLivePlugin(CMSPluginBase):
    model = jarakan_models.PetaLivePlugin
    module = _("Desa Jarakan")
    name = _("Peta Live")
    render_template = "peta_iframe.html"
    cache = False

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            
        })
        return context

@plugin_pool.register_plugin  # register the plugin
class UMKMPlugin(CMSPluginBase):
    model = jarakan_models.UMKMPlugin
    module = _("Desa Jarakan")
    name = _("Card UMKM")
    render_template = "umkm_card.html"
    cache = False
    allow_children = True
    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            
        })
        return context

@plugin_pool.register_plugin  # register the plugin
class WisataPlugin(CMSPluginBase):
    model = jarakan_models.WisataPlugin
    module = _("Desa Jarakan")
    name = _("Card Wisata")
    render_template = "wisata_card.html"
    cache = False
    allow_children = True
    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            
        })
        return context

@plugin_pool.register_plugin  # register the plugin
class ProfilGaleriPlugin(CMSPluginBase):
    model = jarakan_models.ProfilGaleriPlugin
    module = _("Desa Jarakan")
    name = _("Card Profil Galeri")
    render_template = "profil_galeri.html"
    cache = False
    allow_children = True
    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            
        })
        return context

@plugin_pool.register_plugin  # register the plugin
class ProfilArtikelPlugin(CMSPluginBase):
    model = jarakan_models.ProfilArtikelPlugin
    module = _("Desa Jarakan")
    name = _("Card Profil Artikel")
    render_template = "profil_artikel.html"
    cache = False
    allow_children = True
    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            
        })
        return context

@plugin_pool.register_plugin  # register the plugin
class PerangkatDesaPlugin(CMSPluginBase):
    model = jarakan_models.PerangkatDesaPlugin
    module = _("Desa Jarakan")
    name = _("Card Perangkat Desa")
    render_template = "card_perangkat_desa.html"
    cache = False
    allow_children = True
    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            
        })
        return context

@plugin_pool.register_plugin  # register the plugin
class ImageResponsive(CMSPluginBase):
    model = jarakan_models.ImageResponsivePlugin
    module = _("Desa Jarakan")
    name = _("Image Responsive")
    render_template = "image_responsive.html"
    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            
        })
        return context    
