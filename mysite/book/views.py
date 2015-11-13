from book.models import Book,Author
from django.shortcuts import render_to_response
from django.template import RequestContext
def search(request):
    h=Author.objects.all()
    e=RequestContext(request,{"author_list":h})
    if request.method == "POST":
        post=request.POST['search']
        p=Author.objects.filter(Name = post)
        for i in p:
            q=Book.objects.filter(AuthorID=i.AuthorID)
            c=RequestContext(request,{"book_list":q})
            return render_to_response("sunyan1.html",c,e)
    return render_to_response("sunyan1.html",e)
def look(request):
    ID = request.GET["id"]
    p=Book.objects.filter(Title = ID)
    for i in p:
        q=Author.objects.filter(AuthorID = i.AuthorID)
        c=RequestContext(request,{"book":i})
        for j in q:
            d=RequestContext(request,{"author":j})
            return render_to_response("sunyan2.html",c,d)
def delete(request): 
    ID = request.GET["id"]
    Book.objects.filter(Title = ID).delete()
    return render_to_response("sunyan.html")
def save_book(request):
    if request.POST:
        post = request.POST
        try:
            Author.objects.get(AuthorID= post["AuthorID"])
        except Author.DoesNotExist:
            return render_to_response("sunyan5.html")
        new_book = Book(
            Title = post["Title"],
            ISBN = post["ISBN"],
            Publisher = post["Publisher"],
            PublishDate = post["PublishDate"],
            Price = post["Price"],
            AuthorID = Author.objects.get(AuthorID= post["AuthorID"]),
            )    
        new_book.save()
    return render_to_response("sunyan3.html")
def save_author(request):
    if request.POST:
        post = request.POST
        new_author = Author(
            AuthorID = post["AuthorID"],
            Name = post["Name"],
            Age = post["Age"],
            Country = post["Country"],
            )    
        new_author.save()
    return render_to_response("sunyan4.html")
def updata(request):
    ID = request.GET["id"]
    p=Book.objects.get(Title = ID)
    if request.POST:
        post = request.POST
        p.Price = post["Price"]
        p.PublishDate = post["PublishDate"]
        p.Publisher = post["Publisher"]
        p.AuthorID = Author.objects.get(AuthorID= post["AuthorID"])
        p.save()
    return render_to_response("sunyan6.html")
