from django.shortcuts import render
from app.models import BBS, BBS_user, Category, Comment
from django.http import HttpResponseRedirect, HttpResponse
from django.core.validators import RegexValidator
import datetime
from django import forms
from django.contrib import messages

alphanumeric = RegexValidator(r'^[0-9a-zA-Z\_]*$', '请输入字母、数字、或者下划线')

class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=16,)
    password = forms.CharField(label='password')

class RegForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(label='password')
    password2 = forms.CharField(label='password2')
    email = forms.CharField(label='email')

class PostForm(forms.Form):
    # category = forms.ChoiceField(label='category')
    title = forms.CharField(label='title')
    content = forms.CharField(label='content')



def index(request):
    articles = BBS.objects.all()
    categories = Category.objects.all()
    comments = Comment.objects.all()
    now = datetime.datetime.now()
    user_count = BBS_user.objects.count()  # 用户数量
    bbs_count = BBS.objects.count() # 帖子数量
    comment_count = Comment.objects.count() # 评论数量
    user = request.COOKIES.get('username')
    new_bbs_id = bbs_count + 1
    # user = BBS_user.objects.all().filter(username=cookie)
    # categorie = Category.objects.get()
    return render(request, 'index.html', {
        'articles': articles,
        'categories': categories,
        'comments': comments,
        'now': now,
        'user_count': user_count,
        'bbs_count': bbs_count,
        'comment_count': comment_count,
        # 'cookie': cookie,
        'user': user,
        'new_bbs_id': new_bbs_id,
    })

def detail(request, bbs_id):
    # print(bbs_id)

    article = BBS.objects.get(id=bbs_id)
    comments = Comment.objects.all().filter(article_id=bbs_id)
    user = request.COOKIES.get('username')
    view_count = BBS.objects.get(id=bbs_id).view_count
    view_count += 1
    BBS.objects.filter(id=bbs_id).update(view_count=view_count)
    # now = timezone.now()
    # post_time = BBS.objects.get(id=bbs_id).created_date
    # time = (now - post_time).seconds
    categories = Category.objects.all()
    # user = BBS_user.objects.all().filter(username=cookie)

    # comment_user = Comment.objects.get()
    return render(request, 'detail.html', {
        'article': article,
        'comments': comments,
        'user': user,
        'view_count': view_count,
        # 'time': time,
        'categories': categories
    })


def reg(request):
     # if request.method == 'GET':
    #     print('GET')
    #     return render(request, 'reg.html', context_instance=RequestContext(request))
    # print('hello')
    # if request.method == 'POST':

    form = RegForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']
         #添加到数据库
        BBS_user.objects.create(username= username, password=password, email=email)
        response = HttpResponseRedirect('/index/')
        #将username写入浏览器cookie,失效时间为3600
        request.session['login_bool'] = True
        login_bool = True
        response.set_cookie('username', username, 3600)
        return response
     # return render(request, 'login.html', {'form': form,})


    return render(request, 'reg.html', {'form': form,})



def login(request):
    # if request.method != 'POST':
    #     print('get')
    #     return render(request, 'login.html', context_instance=RequestContext(request))
    #
    # if request.method == 'POST':
    #     print('post')
    # try:
    # if request.method == 'POST':
    print('post')
    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        print('password')
        user = BBS_user.objects.filter(username__exact = username,password__exact = password)

        if user:
            print('user')
            response = HttpResponseRedirect('/index/')
            #将username写入浏览器cookie,失效时间为3600
            # request.session['login_bool'] = True
            login_bool = True
            # response.set_cookie('user_id', B, 3600)
            response.set_cookie('username', username, 3600)
            return response
        else:
            #比较失败，还在login
            return HttpResponseRedirect('/login/')
# else:
#     form = LoginForm()
    return render(request, 'login.html', {'form': form,})
    # username=request.POST.get('username')
    # password = request.POST.get('password')
    # user = BBS_user.objects.filter(username__exact = username,password__exact = password)
    # if user:
    #     request.session['login_bool'] = user
    #     return render(request, 'index-bac.html', {
    #         'login_bool': user,
    #         'user': user
    #     })
    # else:
    #     print('chongdingx')
    #     return HttpResponseRedirect('/login/')

    #     else:
    #         #比较失败，还在login
    #         messages.add_message(request, messages.WARNING, '账号或密码错误，请重新输入')
    #         return HttpResponseRedirect('/login/')
    # except:
    #      messages.add_message(request, messages.WARNING, '该用户不存在，请重新输入')
    #      return HttpResponseRedirect('/login/')
    # return render(request, 'login.html')


    # username = request.POST.get('username')
    # password = request.POST.get('password')
    # user = auth.authenticate(username=username, password=password)
    # print(username, password)
    # if user is not None: # and user.is_active:
    #     auth.login(request, user)
    #     return HttpResponseRedirect('/')
    # else:
    #     return render(request, 'login.html', {'login_err': 'Wrong username or password!'})

def logout(request):
    response = HttpResponseRedirect('/index/')
    response.delete_cookie('username')
    return response

def reply(request, bbs_id):
    content = request.POST.get('content')
    username = request.COOKIES['username']
    user = BBS_user.objects.get(username=request.COOKIES['username'])
    messages.add_message(request, messages.INFO, content)
    Comment.objects.create(content=content, date=datetime.datetime.now(), user_id_id=user.id, article_id_id=bbs_id)
    return HttpResponseRedirect('/detail/' + bbs_id)
    # return render(request, 'detail-bac.html')

def user(request):
    user = BBS_user.objects.get(username=request.COOKIES['username'])
    articles = BBS.objects.filter(author_id=user.id)
    categories = Category.objects.all()
    return render(request, 'userInfo.html', {
        'user': user,
        'articles': articles,
        'categories': categories
    })

def post(request):
    user = request.COOKIES.get('username')
    categories = Category.objects.all()
    author = BBS_user.objects.get(username=request.COOKIES['username'])
    new_bbs_id = BBS.objects.count() + 1

    form = PostForm(request.POST)
    # print(form.is_valid())
    if form.is_valid():
        title = form.cleaned_data['title']
        content = form.cleaned_data['content']

    # title = request.POST.get('title')
    # content = request.POST.get('content')

        new_bbs = BBS.objects.create(
            title=title,
            content=content,
            view_count=1,
            created_date=datetime.datetime.now(),
            update_date=datetime.datetime.now(),
            ranking=0,
            category_id_id=request.POST.get('category'),
            author_id = author.id
            # author = request.COOKIES['username'].id
        )
        if new_bbs:
            return HttpResponseRedirect('/detail/' + str(new_bbs_id))
    return render(request, 'post.html', {
        'categories': categories,
        'user': user
    })

def category(request):
    categories = Category.objects.all()
    user = request.COOKIES.get('username')
    return render(request, 'category.html', {
        'categories': categories,
        'user': user
    })

def node(request, category_id):
    articles = BBS.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    return render(request, 'node.html', {'articles': articles, 'categories': categories})

def search(request, keyword):
    categories = Category.objects.all()
    articles = BBS.objects.filter(title__contains=keyword)
    return render(request, 'search.html', {
        'ketword': keyword,
        'articles': articles,
        'categories': categories
    })

def notifications(request):
    user = BBS_user.objects.get(username=request.COOKIES['username'])
    comments = Comment.objects.filter(article_id__author=user.id)
    # Comment.objects.update(is_read=1)
    return render(request, 'notifications.html', {
        'comments': comments,
    })



