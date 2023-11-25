



from email.policy import default
from tabnanny import verbose
from django.db import models
from django.urls import reverse

class States(models.Model):
    title = models.CharField(max_length=255, verbose_name="State name")
    slug=models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', null=True)
    content= models.TextField(blank=False, verbose_name="State content")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Photos")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Time created")
    time_update=models.DateTimeField(auto_now = True, verbose_name="Time updated")
    is_published = models.BooleanField(default=True, verbose_name="Is published")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Category")
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("states", kwargs={"state_slug": self.slug})
    
    class Meta: #for (s) in admin panel
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
