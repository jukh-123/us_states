



from email.policy import default
from tabnanny import verbose
from django.db import models
from django.urls import reverse
import django.dispatch

class States(models.Model):
    title = models.CharField(max_length=255, verbose_name="State name")
    slug=models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', null=True)
    content= models.TextField(blank=False, verbose_name="State preview text")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Main photo", blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Time created")
    time_update=models.DateTimeField(auto_now = True, verbose_name="Time updated")
    is_published = models.BooleanField(default=True, verbose_name="Is published")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Category")
    jobs = models.CharField(max_length=255, verbose_name="State main jobs", default="jobs title")
    salary = models.IntegerField(verbose_name="State average annual income", default=1000)
    lowest_annual_income = models.IntegerField(verbose_name="State lowest annual income", default=100)
    living_expenses = models.CharField(max_length=5, verbose_name="Living expenses in $$$", default="$")
    taxes = models.CharField(max_length=255, verbose_name="State tax link", default="This field will set by itself", blank=True)
    def save(self, *args, **kwargs):
        self.taxes = f"https://taxfoundation.org/location/{self.slug}/"
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("states", kwargs={"state_slug": self.slug})
    
    class Meta: #для stateS у адмін панелі
        verbose_name='State'
        verbose_name_plural="States"
        ordering = ['title', 'time_create']

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='Category')
    slug=models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', null=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_id": self.pk})
    
    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'
        ordering=['id']


class ImagesForStates(models.Model):
    state = models.ForeignKey(States, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Photos")
    description = models.TextField(blank=False, verbose_name="State content", default="Some description for photo")
    photo_header = models.CharField(max_length=255, verbose_name="Header for photo", default="Nature")

class ModelForMap(models.Model):
    state = models.ForeignKey(States, on_delete=models.CASCADE)
    svg_path = models.TextField(blank=True)
    