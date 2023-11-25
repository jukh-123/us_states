


from django import template
from main.models import *


register = template.Library()


@register.simple_tag()
def get_categories(filter=None):
    if filter==None:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


@register.inclusion_tag("main/list_categories.html")
def show_categories(sort=None):
    if sort==None:
        cats=Category.objects.all()
    else:
        cats=Category.objects.order_by(sort)
    
    return {"cats":cats}

@register.inclusion_tag("main/list_menu.html")
def show_menu():
    menu = [{'title': 'Main page', 'url_name':'home', 'font_awesome_class':'fas fa-home'},
        {'title': 'States', 'url_name':'states_main', 'font_awesome_class':'fas fa-city'},
        {'title': 'Add page', 'url_name':'add_page', 'font_awesome_class':'fas fa-plus'},
        {'title': 'About', 'url_name':'about', 'font_awesome_class':'fas fa-address-card'},
        {'title': 'Login', 'url_name':'login', 'font_awesome_class':'fas fa-user'} ,      
    ]
    return {"menu":menu}
