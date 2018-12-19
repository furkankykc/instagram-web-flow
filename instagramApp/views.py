from django.shortcuts import render, redirect

from instagramApp.instaRest import InstagramClient
from .forms import followForm
from .models import instagram

# Create your views here.
instaApi = None


def instagramInit(username, password):
    global instaApi
    if (instaApi != None):
        if instaApi.api.username_id != instaApi.get_userID(username):
            instaApi = InstagramClient(username, password)
    else:
        instaApi = InstagramClient(username, password)


def updateAccount(request, username):
    global instaApi
    print("update account calıstı")
    account = instagram.objects.get(username=username)
    instagramInit(account.username, account.password)
    instagram.objects.get(username=username).updateData(instaApi)
    # print(account)
    return myprofileview(request, username)


def myprofileview(request, username):
    global instaApi
    message = ""

    try:
        account = instagram.objects.get(username=username)
        media = instaApi.getSelfPost()
        followers = instaApi.getFollowers()
        # print(followers)
        followings = instaApi.getFollowings()
    except:
        instagramInit(account.username, account.password)

    if request.method == 'POST':
        if request.POST.get("form_type") == "follow":
            pageName = request.POST['pageName']
            if (pageName == "" or pageName == None):
                message = "Please check username that you write in textbox"
            else:
                if instaApi.followSomeOne(pageName):
                    message = "Request for following is Successful"
                else:
                    message = "There is nobody there that username is %s" % pageName
        elif request.POST.get("form_type") == "feed":
            pageName = request.POST['pageName']
            if (pageName == "" or pageName == None):
                message = "Please check username that you write in textbox"
            else:
                try:
                    other = instaApi.getPosts(pageName)
                except:
                    instagramInit(account.username, account.password)


        elif request.POST.get("form_type") == "photo":
            upload(request)
    else:
        try:
            account = instagram.objects.get(username=username)

            instagramInit(account.username, account.password)
            media = instaApi.getSelfPost()
            followers = instaApi.getFollowers()
            # print(followers)
            followings = instaApi.getFollowings()
        except:
            account.updateData(instaApi)
            return redirect('dashboard')

    return render(request, 'panel/account/account.html', locals())


def registerInstagram(request):
    if (request.method == 'POST'):
        try:
            username = request.POST['username']
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            if (username == "" or name == "" or email == "" or password == ""):
                message = "Formu eksiksiz doldurunuz."
            else:
                return
                # im.main(username,name,email,password)
        except:
            return render(request, 'panel/register.html', locals())
        # eğer veri gelirse yazdır :
        print(username, ":", password)
    return render(request, 'panel/register.html', locals())


def upload(request):
    if (request.method == 'POST'):
        # print(request.POST)
        photo = request.POST['photo']
        message = request.POST['message']
        instaApi.uploadPhoto(photo, message)
    # return updateAccount(request,username)


def index(request):
    if request.method == 'POST':
        folllowForm = followForm(request.POST)
        if folllowForm.is_valid():
            pageName = followForm.cleaned_data['pageName']

            instaApi.followSomeOne(pageName)
    followers = ['follow1', 'follow2', 'follow3']
    followings = ['fwwww1', 'fwww2', 'fwww']

    folllowForm = followForm()
    return render(request, 'panel/index.html', locals())


def followers(request):
    followers = ['follow1', 'follow2', 'follow3']
    return followers


def dashboard(request):
    accounts = instagram.objects.all()
    return render(request, 'panel/dashboard.html', locals())
