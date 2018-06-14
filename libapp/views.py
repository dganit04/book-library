from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from models import Item
from forms import bookForm

# an example of form model, I chose forms.py because I could add help_text, placeholder...
# class bookForm(ModelForm):
#     class Meta:
#         model = Item
#         fields = ['title', 'description', 'author', 'pic']

def index(request):
    print 'home'
    items = Item.objects.all()
    itemsLen = len(items)
    itemsWithClass = [{'id': 0, 'title': '', 'description': '', 'author': '', 'pic': '', 'class': ''} for x in range(itemsLen)]
    for idx, val in enumerate(items):
        itemsWithClass[idx]['id'] = val.id
        itemsWithClass[idx]['title'] = val.title
        itemsWithClass[idx]['description'] = val.description
        itemsWithClass[idx]['author'] = val.author
        itemsWithClass[idx]['pic'] = val.pic
        itemsWithClass[idx]['class'] = val.author.split(' ')[0]
    return render(request, 'library/index.html', { # show this view when getting to this page
        'items': itemsWithClass
    })

def item_detail(request, id):
    try:
        item = Item.objects.get(id=id)
        print 'item detail ', id
    except Item.DoesNotExist:
        raise Http404('This item does not exist, stop trying!')
    return render(request, 'library/item_detail.html', { # gets here at first
        'item': item,
    })

def item_create_update(request, id):
    print 'item_create_update ', id
    createNew = id == 'a'
    if createNew:
        item = Item(title='', description='', author='', pic='')
        form = bookForm()
        print 'create new form'
    else:
        item = Item.objects.get(id=id)
        form = bookForm(initial={'title': item.title, 'description': item.description, 'author': item.author, 'pic': item.pic})
        print 'update exisiting form'
    if request.method == 'POST':
        form = bookForm(request.POST)
        print 'form-update-create-POST'
        if form.is_valid():  # coming from save button click
            print 'form update-create valid'
            item.author = form.cleaned_data['author']
            item.description = form.cleaned_data['description'] or 'No Description'
            item.title = form.cleaned_data['title']
            item.pic = form.cleaned_data['pic'] or 'img/img3.jpeg'
            item.save()
            return HttpResponseRedirect(reverse('index')) # you won't see 'form' in url
        else:
            print 'form Not Valid'
            return render(request, 'library/item_create_update.html', { # stay if not valid
                'form': form
            })
    else:  # when getting to page at first - Stay
        print 'Initial update-create page ', id
        return render(request, 'library/item_create_update.html', {
            'form': form
        })

# def item_form(request):
#     print 'item_form'
#     if request.method == 'POST': # getting here only after clicking 'submit'
#         form = bookForm(request.POST)
#         print 'form-POST '
#         if form.is_valid():  # coming from save button click
#             print 'form valid'
#             author = form.cleaned_data['author']
#             description = form.cleaned_data['description'] or 'No Description'
#             title = form.cleaned_data['title']
#             pic = form.cleaned_data['pic'] or 'img/img3.jpeg'
#             query = Item(title=title, description=description, author=author, pic=pic)
#             query.save()
#             return HttpResponseRedirect(reverse('index')) # you won't see 'form' in url
#         else:
#             print 'form Not Valid'
#             return render(request, 'library/item_form.html', { # stay if not valid
#                 'form': form
#             })
#
#     else:  # empty form to fill, coming here initially
#         print 'initial form'
#         form = bookForm()
#         return render(request, 'library/item_form.html', {
#             'form': form
#         })

# def item_update(request, id):
#     try:
#         item = Item.objects.get(id=id)
#         form = bookForm(initial={'title': item.title, 'description': item.description, 'author': item.author, 'pic': item.pic})
#         print 'update ', id
#     except Item.DoesNotExist:
#         raise Http404('This item does not exist, stop trying!')
#     if request.method == 'POST':
#         form = bookForm(request.POST)
#         print 'form-update-POST'
#         if form.is_valid():  # coming from save button click
#             print 'form update valid'
#             item.author = form.cleaned_data['author']
#             item.description = form.cleaned_data['description'] or 'No Description'
#             item.title = form.cleaned_data['title']
#             item.pic = form.cleaned_data['pic'] or 'img/img3.jpeg'
#             # query = Item(title=title, description=description, author=author, pic=pic)
#             # query.save()
#             item.save()
#             return HttpResponseRedirect(reverse('index')) # you won't see 'form' in url
#         else:
#             print 'form Not Valid'
#             return render(request, 'library/item_update.html', { # stay if not valid
#                 'form': form
#             })
#     else:  # when getting to page at first - Stay
#         print 'Initial update page ', id
#         return render(request, 'library/item_update.html', {
#             'form': form
#         })

def item_delete(request, id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        raise Http404('This item does not exist, stop trying!')
    print 'item_delete ', id
    if request.method == 'POST':
        print 'Delete-POST'
        item = Item.objects.get(id=id)
        item.delete()
        return HttpResponseRedirect(reverse('index')) # you won't see 'delete/id' in url
    else:  # when getting to page at first - Stay
        print 'Initial delete page'
        return render(request, 'library/item_delete.html', {
            'item': item,
        })

def reset(request): # load initial books
    print 'Reset'
    dict_library = [
        {'title': 'My First Garden', 'description': 'All my veggies', 'author': 'Amanda J.', 'pic': 'img/img1.jpeg'},
        {'title': 'My First Car', 'description': 'All cars', 'author': 'Amanda J.', 'pic': 'img/img2.jpeg'},
        {'title': 'My First Hobbie', 'description': 'All my hobbies', 'author': 'Nancy W.', 'pic': 'img/img3.jpeg'},
        {'title': 'My First machine', 'description': 'My woodshop', 'author': 'Jack L.', 'pic': 'img/img9.jpeg'},
        {'title': 'My First Collection', 'description': 'All my collections', 'author': 'Amanda J.', 'pic': 'img/img10.jpeg'},
        {'title': 'My First art', 'description': 'All my paintings', 'author': 'Amanda J.', 'pic': 'img/img11.jpeg'},
        {'title': 'My First date', 'description': 'All my dances', 'author': 'Jack L.', 'pic': 'img/img12.jpeg'},
        {'title': 'If you give a mouse a cookie', 'description': 'Yummy cookie', 'author': 'Amanda J.', 'pic': 'img/img13.jpeg'},
        {'title': 'The joy of giving', 'description': 'The story about helping', 'author': 'Amanda J.', 'pic': 'img/img14.jpeg'},
        {'title': 'Judy Moody', 'description': 'The princess', 'author': 'Don D.', 'pic': 'img/img15.jpeg'},
        {'title': 'I was so mad', 'description': 'When I heard the story', 'author': 'Amanda J.', 'pic': 'img/img16.jpeg'},
        {'title': 'Chicka Chicka', 'description': 'The magician ', 'author': 'Don D.', 'pic': 'img/img17.jpeg'},
        {'title': 'All My Friends', 'description': 'I am so blessed', 'author': 'Amanda J.', 'pic': 'img/img18.jpeg'},
        {'title': 'Winnie the Pooh', 'description': 'its all about the bear', 'author': 'Amanda J.', 'pic': 'img/img19.jpeg'},
        {'title': 'Franky the frog', 'description': 'Who became a prince', 'author': 'Amanda J.', 'pic': 'img/img20.jpeg'},
        {'title': 'Maria the brave mermaid', 'description': 'Under the sea', 'author': 'Don D.', 'pic': 'img/img21.jpeg'},
        {'title': 'I love you', 'description': 'Because you are my best friend', 'author': 'Don D.', 'pic': 'img/img22.jpeg'}
    ]

    Item.objects.all().delete() # delete whatever we have currently in database
    # Feed new info
    for k in dict_library:
        # for each one in the above dictionary - save it as a database item
        title = k.get('title')
        description = k.get('description')
        author = k.get('author')
        pic = k.get('pic')
        query = Item(title=title, description=description, author=author, pic=pic)
        query.save()
    return HttpResponseRedirect(reverse('index')) # you won't see 'reset' in url
