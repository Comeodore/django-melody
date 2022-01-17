from django.db import models

class ReserveFlats(models.Model):
    id = models.IntegerField(verbose_name="Номер квартиры", primary_key=True)
    floor = models.IntegerField(verbose_name="Этаж")
    price = models.FloatField(verbose_name="Цена квартиры ($)")
    reserved = models.BooleanField(verbose_name="Резерв")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "квартиру"
        verbose_name_plural = "квартиры"
        ordering = ['id']

class StripePayment(models.Model):
    payment_id = models.CharField(max_length=255)
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.payment_id)


class SuccessPaymentUser(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя покупателя')
    surname = models.CharField(max_length=255, verbose_name='Фамилия покупателя')
    email = models.EmailField(max_length=255, verbose_name='Email покупателя')
    phone = models.CharField(max_length=255, verbose_name='Телефон покупателя')
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
