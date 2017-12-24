from django.http import Http404
from django.shortcuts import render , redirect
from Sclubs.models import Club,Comment,Member
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View
from .forms import SignUpForm, SampleForm, CommentForm
from django.template import loader





def index(request):
    all_clubs = Club.objects.all()
    context = {'all_clubs': all_clubs,}
    return render(request, 'Sclubs/index.html', context)


def details(request, club_id):
    try:
        club = Club.objects.get(pk=club_id)
    except Club.DoesNotExist:
        raise Http404("Club does not exist")
    form_errors = {}
    form_values = {"title": "", "body": "", "rating": 0}
    if request.POST:
        print("rating=", request.POST["rating"], type(request.POST["rating"]))
        print("comment=", request.POST["yorum"])
        form_values["title"] = request.POST["title"]
        form_values["body"] = request.POST["yorum"]
        form_values["rating"] = int(request.POST["rating"])
        if len(request.POST["yorum"]) < 10:
            form_errors["body"] = "You comment is too short. It should be at least 10 characters"
        if len(request.POST["title"]) == 0:
            form_errors["title"] = "Title field is required"
        if form_values["rating"] == 0:
            form_errors["rating"] = "Please select a rating"
        if len(form_errors) == 0:
            new_comment = Comment()
            new_comment.title = form_values["title"]
            new_comment.body = form_values["body"]
            new_comment.Club = Club
            new_comment.rating = form_values["rating"]
            new_comment.save()
            form_values["title"] = ""
            form_values["body"] = ""
            form_values["rating"] = 0
            print("SAVED")
    else:  # page loaded first time. no form POST data
        pass
        # print(request.POST["yorum"])
    context = {'club': club, "errors": form_errors,
               "values": form_values}

    return render(request, 'Sclubs/detail.html', {context})

# user accounts

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.bio = form.cleaned_data.get('bio')
            print("avatar", form.cleaned_data.get('avatar'))
            print(request.FILES)
            user.profile.avatar = request.FILES['avatar']
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()

    return render(request, 'Sclubs/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    # return redirect(request.path)
    return redirect("/")


def login_view(request):
    print(request.POST)
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        pass
    # return redirect(request.path)
    return redirect("/")

