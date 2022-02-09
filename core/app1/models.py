from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(
        max_length = 255
    )

    def __str__(self):
        return self.name

class Product(models.Model):

    title = models.CharField(
        verbose_name=_("title"),
        help_text=_("Required"),
        max_length=255,
    )
    category =models.ForeignKey(Category,on_delete=models.RESTRICT)
    description = models.TextField(verbose_name=_("description"),help_text=_("Not Required"),
    blank=True)
    slug = models.SlugField(max_length=255)
    regular_price = models.DecimalField(
        verbose_name=_("Regular Price"),
        help_text=_('Maximum 999.99'),
        error_messages={
            "name":{
                "max_length":_("The price can't be that"),

            },
        },
        max_digits=5,
        decimal_places=2,
    )
    discount_price = models.DecimalField(
        verbose_name=_("Discount Price"),
        help_text=_('Maximum 999.99'),
        error_messages={
            "name":{
                "max_length":_("The price can't be that"),

            },
        },
        max_digits=5,
        decimal_places=2,
    )
    is_active = models.BooleanField(
        verbose_name=_("Product Visibility"),
        help_text = _("Change visibility"),
        default=True,
    )
    created_at = models.DateTimeField(_("Created_at"),auto_now_add=True,editable=False)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

    def __str__(self):
        return self.title
