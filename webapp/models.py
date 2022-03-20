from django.db import models
from django.contrib.auth.models import User

class Device(models.Model):

    EXCELLENT = 'EX'
    GOOD = 'GO'
    BAD = 'BA'
    CONDITION_CHOICES = [
        (EXCELLENT, 'Excelente'),
        (GOOD, 'Buena'),
        (BAD, 'Mala'),
    ]

    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    serial = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    condition = models.CharField(
        max_length=2,
        choices=CONDITION_CHOICES,
        default=EXCELLENT
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.type} {self.brand} {self.model}"


class Borrow(models.Model):

    REQUESTED = 'REQ'
    APPROVED = 'APR'
    ON_ROUTE = 'ONR'
    DELIVERED = 'DEL'
    RETURNED = 'RET'
    STATUS_CHOICES = [
        (REQUESTED, 'Pendiente'),
        (APPROVED, 'Aprobado'),
        (ON_ROUTE, 'En ruta'),
        (DELIVERED, 'Entregado'),
        (RETURNED, 'Devuelto'),
    ]

    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="borrows",
        limit_choices_to={'groups__name': 'docentes'}
    )
    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE,
        related_name="requests"
    )
    carrier = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="jobs",
        limit_choices_to={'groups__name': 'mensajeros'},
        null=True,
        blank=True,
    )
    status = models.CharField(
        max_length=3,
        choices=STATUS_CHOICES,
        default=REQUESTED
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.username} solicitó {self.device.type} {self.device.brand} {self.device.model}"