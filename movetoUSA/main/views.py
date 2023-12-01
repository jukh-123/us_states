


from webbrowser import get
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *
from django.shortcuts import get_object_or_404
from .forms import *
from django.views.generic import ListView
# Create your views here.

posts = States.objects.all()

def index(request):
    context={
        'posts':posts,
        'title': 'Main Page',
        'cat_selected':0
    }
    return render(request, 'main/index.html', context=context)



class StatesMain(ListView):
    model=States
    template_name='main/states_main.html'
    context_object_name='posts'
    title='States page'
    
    def get_context_data(self, *args, object_list=None, **kwargs):
        context=super().get_context_data(*args, **kwargs)
        context['title']=self.title
        return context
    
    def get_queryset(self):
        return States.objects.filter(is_published=True)



def show_states(request, state_slug):
    post=get_object_or_404(States, slug=state_slug)
    photos_descriptions = ImagesForStates.objects.filter(state_id=post.id)
    context={
        'post':post,
        'title': post.title,
        'photos_and_descriptions': photos_descriptions,
    }
    
    return render(request, 'main/post.html', context=context)
    
def show_category(request, cat_id):
    posts = States.objects.filter(cat_id=cat_id)
    cats = Category.objects.filter(id=cat_id)
    cat_id_list = []
    for i in cats:
        cat_id_list.append(i.id)
    if cat_id not in cat_id_list:
        raise Http404()
    else:
        context={
        'posts':posts,
        'title':list(cats)[0].name,
        'cats':cats,
        }
        return render(request, 'main/states_main.html', context=context)

# class StatesCategory(ListView):
#     model=Category
#     template_name='main/states_main.html'
#     context_object_name='posts'
    
#     def get_queryset(self):
#         return States.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context=super().get_context_data(**kwargs)
#         title='States'
        
#         context['title']=title
#         return context
    
def show_map(request):
    paths = ModelForMap.objects.all()
    context={
        'title':'Map',
        'paths':paths,
        
    }
    return render(request, 'main/map_page.html', context=context)
    

def archive(request, year):
    if year > 2023:
        uri = reverse('home')
        return redirect(uri) # ця сторінка переїхала на сторінку "home", permenent=True значить назавжди


    return HttpResponse(f'<h1>Archive for {year} year</h1>')

def login(request):
    return HttpResponse('login page')
    
def add_page(request):
    if request.method == 'POST':
        form=AddPostForm(request.POST, request.FILES)
        files = request.FILES.getlist("file_field")
        
        if form.is_valid()==True:
            f = form.save()
            for i in files:
                ImagesForStates.objects.create(state = f, photo = i)
            return redirect('states_main')

    else:
        form=AddPostForm()
        imageform = FileFieldForm()
            
    return render(request, 'main/add_page.html', {'title':'Add page', 'form':form, "imageform":imageform})

def about(request):
    return render(request, 'main/about_us.html', {'title':'About us'})

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>PAGE DOESNT EXIST</h1>')