from django.db import models
from django.utils.translation import ugettext_lazy as _

from datetime import datetime

from region.models import Region, City


class UserCard(models.Model):
    code = models.IntegerField(_("Card code"))
    fist_name = models.CharField(_("First name"), max_length=255,
        blank=True, null=True)
    secon_name = models.CharField(_("Second name"), max_length=255,
        blank=True, null=True)
    last_name = models.CharField(_("Last name"), max_length=255,
        blank=True, null=True)
    oblast = models.ForeignKey(Region, blank=True, null=True,
        verbose_name=_("Oblast"))
    address = models.TextField(_("Address"), blank=True, null=True)
    city = models.ForeignKey(City, max_length=100,
        blank=True, null=True)
    post_code = models.CharField(_("Post code"), blank=True,
        null=True, max_length=10)
    work_phone = models.CharField(_("Work phone"), blank=True,
        null=True, max_length=50)
    inner_phone = models.CharField(_("Internal phone"), blank=True,
        null=True, max_length=50)
    home_phone = models.CharField(_("Home phone"), blank=True,
        null=True, max_length=50)
    mobile_phone = models.CharField(_("Mobile phone"), blank=True,
        null=True, max_length=50)
    email = models.EmailField(_("Email"), blank=True, null=True)
    second_email = models.EmailField(_("Second email"), blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    last_visit = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to="patients/photo",
        blank=True, null=True)
    note = models.TextField(_("Note"), blank=True, null=True)
    staff_code = models.CharField(_("Staff code"), max_length=255,
        blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Patient card")
        verbose_name_plural = _("Patients cards")
        ordering = ("-code",)

    def __unicode__(self):
        return ("%s %s %s") % (
            self.fist_name,
            self.secon_name,
            self.last_name
        )


class Visits(models.Model):
    patient = models.ForeignKey(UserCard, verbose_name=_("patient"))
    visit_time = models.DateTimeField(default=datetime.now)
    note = models.TextField(_("Note"), blank=True, null=True)

    class Meta:
        verbose_name = _("Visit")
        verbose_name_plural = _("Visits")


