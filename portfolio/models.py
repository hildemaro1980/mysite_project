from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from django.db.models.fields import CharField, TextField, DateField, URLField
from django.db.models.fields.files import ImageField
from datetime import date

class Project(TranslatableModel):
    translations = TranslatedFields(
        title = CharField(max_length=100),
        description = TextField(),
        image = ImageField(upload_to='portfolio/images/',blank=True),
        url = URLField(blank=True),
        date = DateField(default=date.today),
    )
   # class Meta:
   #     ordering = ["-translations"]

    def __str__(self) -> str:

        return self.title


#def __str__(self) -> str:
        #return self.title