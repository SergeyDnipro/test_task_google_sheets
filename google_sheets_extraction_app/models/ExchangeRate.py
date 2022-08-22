from django.db import models


class ExchangeRate(models.Model):
    from_code = models.PositiveSmallIntegerField(default=840)
    to_code = models.PositiveSmallIntegerField(default=980)
    rate = models.DecimalField(max_digits=6, decimal_places=2, default=1.0)
    date_of_rate = models.CharField(max_length=30, null=True, blank=True)
