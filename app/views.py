from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from django.shortcuts import get_object_or_404

from app.forms import UserForm
from app.models import Book
import numpy as np
import pickle

from django.conf import settings
import os

# Construct the absolute path to the .pkl files
popular_df_path = os.path.join(settings.BASE_DIR, 'app', 'popular.pkl')
pt_path = os.path.join(settings.BASE_DIR, 'app', 'pt.pkl')
books_path = os.path.join(settings.BASE_DIR, 'app', 'books.pkl')
similarity_scores_path = os.path.join(settings.BASE_DIR, 'app', 'similarity_scores.pkl')

# Load the files
popular_df = pickle.load(open(popular_df_path, 'rb'))
pt = pickle.load(open(pt_path, 'rb'))
books = pickle.load(open(books_path, 'rb'))
similarity_scores = pickle.load(open(similarity_scores_path, 'rb'))

@login_required
def user_logout(request):
    logout(request)
    return redirect('/')

def logine(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']  
        user = authenticate(username=username,password=password)
        
        if user: 
            if user.is_active:
                login(request,user)
                return redirect('/')
            else:
                return HttpResponse("Account is not found")
        else:
            print("Some trie to login failed")
            print(f'username {username} and password {password}')
            return HttpResponse("Invalid detail suplied")
    return render(request,'login.html')

def singup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserForm()
    return render(request,'singin.html')

def update(request):
    try:
        for i in range(len(popular_df)):
            book_name = popular_df['Book-Title'].iloc[i]
            author = popular_df['Book-Author'].iloc[i]
            image_url = popular_df['Image-URL-M'].iloc[i]
            votes =popular_df['num_ratings'].iloc[i]
            rating =  popular_df['avg_ratings'].iloc[i]
            try:
                Book.objects.create(name = book_name, author=author ,rating=rating,votes=votes, pic_url=image_url)
            except:
                pass
    except:
        pass
    return redirect('/')

def index(request):
    # data ={}
    try:
        book = Book.objects.all()
        if request.method == 'GET':
            st = request.GET.get('search')
            print(st,'search')
            if st != None:
                book = Book.objects.filter(name__icontains=st)
                print(book,'book')
        data ={
            'books_data':book
        }
    except:
        pass

    return render(request,'index.html',context=data)


@login_required
def recomands(request):
    data = []
    if request.method == 'POST':
        user_input = request.POST['name']
        
        if user_input in pt.index:
            index = np.where(pt.index==user_input)[0][0]
            similar_items = sorted(list(enumerate(similarity_scores[index])),key=lambda x:x[1],reverse=True)[1:5]
        
            for i in similar_items:
                item = []
                temp_df = books[books['Book-Title'] == pt.index[i[0]]]
                item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
                item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
                item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
                
                data.append(item)

    data ={
            'data':data
        }
    print(data)
    return render(request,'recommend.html',context=data)

@login_required
def recomand(request,id):
    data = []
    # obj = Book.objects.get(id=id)
    obj = get_object_or_404(Book,id=id)
    if not obj:
        obj = get_object_or_404(Book,name=id)
        
    user_input = obj.name
    if user_input in pt.index:
        index = np.where(pt.index==user_input)[0][0]
        similar_items = sorted(list(enumerate(similarity_scores[index])),key=lambda x:x[1],reverse=True)[1:5]
        
        for i in similar_items:
            item = []
            temp_df = books[books['Book-Title'] == pt.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
                
            data.append(item)

    data ={
            'data':data
        }
    print(data)
    return render(request,'recommend.html',context=data)






    # books_data =[]
    # for i in range(len(popular_df)):
    #     books_data.append({
    #         'book_name': popular_df['Book-Title'].iloc[i],
    #         'author': popular_df['Book-Author'].iloc[i],
    #         'image': popular_df['Image-URL-M'].iloc[i],
    #         'votes': popular_df['num_ratings'].iloc[i],
    #         'rating': popular_df['avg_ratings'].iloc[i],
    #         })
        
    # print(popular_df)
    # data = {
    #     'books_data' : books_data
    # }
    # return render(request,'index.html',context=data)
    
    
    ##########################
            # for i in range(len(popular_df)):
            # book_name = popular_df['Book-Title'].iloc[i]
            # author = popular_df['Book-Author'].iloc[i]
            # image_url = popular_df['Image-URL-M'].iloc[i]
            # votes =popular_df['num_ratings'].iloc[i]
            # rating =  popular_df['avg_ratings'].iloc[i]
            # Book.objects.create(name = book_name, author=author ,rating=rating,votes=votes, pic_url=image_url)
