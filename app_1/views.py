from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import User
from .forms import NewsForm


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def news(request):
    users = User.objects.all()
    return render(request, 'news.html', {'newss': users})


def details(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, 'detail.html', {'user': user})


class Create(LoginRequiredMixin, CreateView):
    model = User
    form_class = NewsForm
    template_name = 'create.html'
    success_url = reverse_lazy('app1:news')


def update(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.name = request.POST.get('name', user.name)
        user.short_info = request.POST.get('short_info', user.short_info)
        user.description = request.POST.get('description', user.description)

        if 'image' in request.FILES:
            user.image = request.FILES['image']

        user.save()
        messages.success(request, "Yangilik muvaffaqiyatli yangilandi! ✅")
        return redirect('app1:details', id=user.id)

    return render(request, 'update.html', {'user': user})


def delete(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, "Foydalanuvchi muvaffaqiyatli o‘chirildi!")
        return redirect('app1:news')
    return render(request, 'delete.html', {'user': user})
