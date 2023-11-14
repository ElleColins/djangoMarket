from django.shortcuts import render, redirect

from item.models import Category, item

from .forms import SignupForm


def index(request):
    # items = item.objects.filter(is_sold=False)[0:6]
    # categories = Category.objects.all()

    return render(request, 'core/index.html', {
        # 'categories': categories,
        # 'items': items,
    })


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })
