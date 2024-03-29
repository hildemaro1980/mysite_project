from django.db import models
import datetime
from parler.models import TranslatableModel, TranslatedFields

from django.db.models.fields import CharField, TextField, DateField
from django.db.models.fields.files import ImageField

#class Post(models.Model):
class Post(TranslatableModel):
    translations = TranslatedFields(
    title = CharField(max_length=100),
    description = TextField(),
    image = ImageField(upload_to ="blog/images"),
    date = DateField(default=datetime.date.today),
    )

    def __str__(self) -> str:
        return self.title
