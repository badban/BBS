# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response
from app.models import BBS, BBS_user, Category, Comment
from django.http import HttpResponseRedirect, HttpResponse
from django.core.validators import RegexValidator
import datetime
from django import forms
import os
from django.contrib import messages
from django.core.servers.basehttp import FileWrapper


alphanumeric = RegexValidator(r'^[0-9a-zA-Z\_]*$', '请输入字母、数字、或者下划线')

filepath = os.path.dirname(os.path.abspath("__file__"))
IMG_PATH = os.path.join(filepath, "media/upload")



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


def handle_upload_file(f):
    file_name = "%s/%s" %('./media/upload',f.name)
    f_obj = open(file_name,'wb+')
    for chunk in f.chunks():
        f_obj.write(chunk)
    f_obj.close()






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
    img_names = article.imgnames
    names = []
    tempimg_names = img_names.split("*")
    for name in tempimg_names:
        a1 = name.split('.')[-1]
        if a1 == u'jpg' or a1 == u'jpeg' or a1 == u'png':
            names.append(name)
    article.imgnames = names

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
    #new_bbs_id = BBS.objects.count() + 1
    if BBS.objects.count() == 0:
        new_bbs_id = 1
    else:
        maxbbsnum = BBS.objects.latest('id').id
        new_bbs_id = maxbbsnum + 1


    form = PostForm(request.POST)
    # print(form.is_valid())
    if form.is_valid():
        title = form.cleaned_data['title']
        content = form.cleaned_data['content']
        #evevt_date = form.cleaned_data['date']
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    if request.method == 'POST':

        files = request.FILES.getlist('img')
        catagory_id = request.POST.get('category')

        if catagory_id == u'1':
            imgnames = ''
            for f in files:
                destination = open(os.path.join(IMG_PATH, f.name), 'wb+')
                if imgnames == '':
                    imgnames = f.name
                else:
                    imgnames = imgnames + '*' + f.name
                for chunk in f.chunks():
                    destination.write(chunk)
                destination.close()

            print(imgnames)
            new_bbs = BBS.objects.create(
                title=title,
                content=content,
                view_count=1,
                created_date=datetime.datetime.now(),
                update_date=datetime.datetime.now(),
                ranking=0,
                category_id_id=request.POST.get('category'),
                author_id = author.id,
                imgnames = imgnames,
                allfilenames = imgnames,
                # author = request.COOKIES['username'].id
               # img = request.FILES.get('img')
            )

            if new_bbs:
                return HttpResponseRedirect('/detail/' + str(new_bbs_id))
        elif catagory_id ==u'2':
            recent_event_date = request.POST.get('recent_event_date')
            print(recent_event_date )
            event_leader = request.POST.get('event_leader')
            imgnames = ''
            for f in files:
                destination = open(os.path.join(IMG_PATH, f.name), 'wb+')
                if imgnames == '':
                    imgnames = f.name
                else:
                    imgnames = imgnames + '*' + f.name
                for chunk in f.chunks():
                    destination.write(chunk)
                destination.close()

            new_bbs = BBS.objects.create(
                title=title,
                content=content,
                view_count=1,
                created_date=datetime.datetime.now(),
                update_date=datetime.datetime.now(),
                ranking=0,
                category_id_id=request.POST.get('category'),
                author_id=author.id,
                imgnames=imgnames,
                allfilenames=imgnames,
                recent_event_date=recent_event_date,
                event_leader=event_leader,
                # author = request.COOKIES['username'].id
                # img = request.FILES.get('img')
            )

            if new_bbs:
                return HttpResponseRedirect('/detail/' + str(new_bbs_id))
        elif catagory_id ==u'3':
            location = request.POST.get('location')
            imgnames = ''
            for f in files:
                destination = open(os.path.join(IMG_PATH, f.name), 'wb+')
                if imgnames == '':
                    imgnames = f.name
                else:
                    imgnames = imgnames + '*' + f.name
                for chunk in f.chunks():
                    destination.write(chunk)
                destination.close()

            new_bbs = BBS.objects.create(
                title=title,
                content=content,
                view_count=1,
                created_date=datetime.datetime.now(),
                update_date=datetime.datetime.now(),
                ranking=0,
                category_id_id=request.POST.get('category'),
                author_id=author.id,
                imgnames=imgnames,
                allfilenames=imgnames,
                location=location,
                # author = request.COOKIES['username'].id
                # img = request.FILES.get('img')
            )

            if new_bbs:
                return HttpResponseRedirect('/detail/' + str(new_bbs_id))
        elif catagory_id == u'4':
            ebook_abstract = request.POST.get('ebook_abstract')
            ebook_author = request.POST.get('ebook_author')
            ebook_isbn = request.POST.get('ebook_isbn')
            imgnames = ''
            for f in files:
                destination = open(os.path.join(IMG_PATH, f.name), 'wb+')
                if imgnames == '':
                    imgnames = f.name
                else:
                    imgnames = imgnames + '*' + f.name
                for chunk in f.chunks():
                    destination.write(chunk)
                destination.close()

            new_bbs = BBS.objects.create(
                title=title,
                content=content,
                view_count=1,
                created_date=datetime.datetime.now(),
                update_date=datetime.datetime.now(),
                ranking=0,
                category_id_id=request.POST.get('category'),
                author_id=author.id,
                imgnames=imgnames,
                allfilenames=imgnames,
                ebook_abstract=ebook_abstract,
                ebook_author=ebook_author,
                ebook_isbn=ebook_isbn,
                # author = request.COOKIES['username'].id
                # img = request.FILES.get('img')
            )

            if new_bbs:
                return HttpResponseRedirect('/detail/' + str(new_bbs_id))

        else:
            imgnames = ''
            for f in files:
                destination = open(os.path.join(IMG_PATH, f.name), 'wb+')
                if imgnames == '':
                    imgnames = f.name
                else:
                    imgnames = imgnames + '*' + f.name
                for chunk in f.chunks():
                    destination.write(chunk)
                destination.close()

            new_bbs = BBS.objects.create(
                title=title,
                content=content,
                view_count=1,
                created_date=datetime.datetime.now(),
                update_date=datetime.datetime.now(),
                ranking=0,
                category_id_id=request.POST.get('category'),
                author_id=author.id,
                imgnames=imgnames,
                allfilenames=imgnames,
                # author = request.COOKIES['username'].id
                # img = request.FILES.get('img')
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

class UserForm(forms.Form):
    username = forms.CharField()
    headImg = forms.FileField()


def server(request):
    filenamelist = request.GET.get('filenamelist')
    filenamelist = filenamelist.split('*')
    tempnames = []
    for filename in filenamelist:
        a1 = filename.split('.')[-1]
        if a1 != u'jpg' and a1 != u'jpeg' and a1 != u'png':
            tempnames.append(filename)
    filenamelist = tempnames

    if request.method == 'POST':
        if request.POST.get('s_thread'):
            onlyfilename = request.POST.get('s_thread')
            filename = os.path.join(IMG_PATH, onlyfilename)
            wrapper = FileWrapper(file(filename))
            response = HttpResponse(wrapper, content_type='text/plain')
            response['Content-Length'] = os.path.getsize(filename)
            response['Content-Encoding'] = 'utf-8'
            response['Content-Disposition'] = 'attachment;filename=%s' % filename
            return response
    return render(request, 'server.html',{'filenamelist':filenamelist})

def introduction(request):

    return render(request, 'introduction.html')

def connection(request):

    return render(request, 'connection.html')