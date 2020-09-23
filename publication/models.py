from django.db import models
from django.contrib.auth.models import User
from core.models import BaseModel

class Publication(BaseModel):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="publication",
        verbose_name="Владелец"
    )
    description = models.TextField(
        null=True,blank=True,
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to="publications",
        verbose_name="Картинка"
    )

