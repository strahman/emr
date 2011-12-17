from django.db import models
from django.utils.translation import ugettext_lazy as _

class Region(models.Model):
    region = models.CharField(_("Title"), max_length=100)

    class Meta:
        verbose_name = _("Region")
        verbose_name_plural = _("Regions")

    def __unicode__(self):
        return self.region


class City(models.Model):
    region = models.ForeignKey(Region)
    city = models.CharField(_("City"), max_length=100)
    lat = models.CharField(max_length=20, blank=True, null=True)
    lng = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = _("City")
        verbose_name = _("Cities")

    def __unicode__(self):
        return self.city
