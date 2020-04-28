from django.shortcuts import render,redirect
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.utils.datastructures import MultiValueDictKeyError
from django.urls import reverse
from django.core.paginator import Paginator

from dict.models import Word,Comment,Favorite
from dict.forms import CommentForm,CrudForm

# Create your views here.

def index(request):
    num_words = Word.objects.all().count()
    context = {
        'num_words': num_words,
    }
    return render(request, 'index.html', context=context)

class WordListView(generic.ListView):
    model = Word
    context_object_name = 'word_list'
    template_name = 'word/word_list.html'

    def get_queryset(self):
        return Word.objects.all()[:10]

    def get_context_data(self, **kwargs):
        context = super(WordListView, self).get_context_data(**kwargs)
        return context

class WordDetailView(generic.DetailView):
    model = Word
    template_name = 'word/word_detail.html'

def word_detail(request, pk):
    word = get_object_or_404(Word, pk=pk)
    word_comments = num_words = Comment.objects.filter(word_id = word.id)
    
    if word.esyn:
        syns = word.esyn.split('; ')
        word.esyn = syns
    if word.eant:
        ants = word.eant.split('; ')
        word.eant = ants

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment()
            comment.word_id = word.id
            comment.comment = form.cleaned_data['comment']
            comment.user_id = request.user.id 
            comment.save()

            return HttpResponseRedirect(request.path)
    else:
        form = CommentForm()
 
    isFavorite = False

    if request.user.is_authenticated:
        favorite = Favorite.objects.filter(word_id = word.id, user_id = request.user.id)
        if(favorite):
            isFavorite = True
        else:
            isFavorite = False
    context = {
        'form': form,
        'word' : word,
        'comments' : word_comments,
        'isFavorite': isFavorite,
    }
    return render(request,'word/word_detail.html',context)

#-----------Search----------------------------------------------------------------------
def search_detail(request):
    search = request.GET['search']
    mode = request.GET['mode']
    if mode == 'word':
        results = Word.objects.filter(eentry__startswith = search)[:15]
        for x in results:
            if(x.esyn):
                syns = x.esyn.split('; ')
                x.esyn = syns
            if(x.eant):
                ants = x.eant.split('; ')
                x.eant = ants
        context = {
            'results' : results
        }
        return render(request,'search.html',context)
    if mode == 'synonym':
        results = Word.objects.filter(esyn__startswith = search)[:15]
        for x in results:
            if(x.esyn):
                syns = x.esyn.split('; ')
                x.esyn = syns
            if(x.eant):
                ants = x.eant.split('; ')
                x.eant = ants
        context = {
            'results' : results
        }
        return render(request,'search.html',context)
    if mode == 'antonym':
        results = Word.objects.filter(eant__startswith = search)[:15]
        for x in results:
            if(x.esyn):
                syns = x.esyn.split('; ')
                x.esyn = syns
            if(x.eant):
                ants = x.eant.split('; ')
                x.eant = ants
        context = {
            'results' : results
        }
        return render(request,'search.html',context)
    if mode == 'thaieng':
        results = Word.objects.filter(tentry__startswith = search)[:15]
        for x in results:
            if(x.esyn):
                syns = x.esyn.split('; ')
                x.esyn = syns
            if(x.eant):
                ants = x.eant.split('; ')
                x.eant = ants
        context = {
            'results' : results
        }
        return render(request,'search.html',context)

#-----------Search----------------------------------------------------------------------
#-----------Favorite----------------------------------------------------------------------
def favorite(request, pk):
    word = get_object_or_404(Word, pk=pk)
    favorite = Favorite()
    favorite.word_id = word.id
    favorite.user_id = request.user.id
    favorite.save()
    return HttpResponseRedirect(request.GET.get('next'))

def unfavorite(request, pk):
    word = get_object_or_404(Word, pk=pk)
    favorite = Favorite.objects.filter(word_id = word.id, user_id = request.user.id)
    favorite.delete()
    return HttpResponseRedirect(request.GET.get('next'))

def myfavorites(request):
    favorites = Favorite.objects.filter(user_id = request.user.id)
    context = {
        'favorites': favorites,
    }
    return render(request, 'myfavorites.html',context)
#-----------Favorite----------------------------------------------------------------------

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

#CRUD-------------------------------------------------------------------------

def create_crud(request):
    context = {}

    form = CrudForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "crud/create_crud.html", context)

def list_crud(request):
    context = {}

    context["dataset"] = Word.objects.all().order_by("-id")

    return render(request, "crud/list_crud.html", context)

def update_crud(request,pk):
    context = {}

    obj = get_object_or_404(Word, pk = pk)
    form = CrudForm(request.POST or None, instance = obj)
    if request.user.is_superuser:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        context["form"] = form
        return render(request, "crud/update_crud.html", context)

def delete_crud(request,pk):
    context = {}
    obj = get_object_or_404(Word, pk = pk)
    if request.user.is_superuser:
        if request.method == "POST":
            obj.delete()
            return HttpResponseRedirect("/")
        return render(request, "crud/delete_crud.html", context)

#CRUD-------------------------------------------------------------------------
#comment-------------------------------------------------------------------------
def delete_comment(request, pk):
    context = {}
    comment = get_object_or_404(Comment, pk = pk)
    if comment.user == request.user or request.user.is_superuser:
        if request.method == "POST":
            comment.delete()
            return HttpResponseRedirect('/')
    return render(request, "delete_comment.html", context)

def admin_delete_comment(request):
    context = {}
    context["commentdata"] = Comment.objects.all()
    return render(request, "admin_delete_comment.html", context)
    
#comment-------------------------------------------------------------------------