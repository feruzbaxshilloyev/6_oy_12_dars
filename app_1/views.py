from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import User


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def news(request):
    users = User.objects.all()
    return render(request, 'news.html', {'users': users})


def details(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, 'detail.html', {'user': user})


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        short_info = request.POST.get('short_info')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        if not all([name, short_info, description, image]):
            messages.error(request, "Barcha maydonlarni to‘ldiring!")
            return redirect('create')

        User.objects.create(name=name, short_info=short_info, description=description, image=image)
        messages.success(request, "Foydalanuvchi muvaffaqiyatli yaratildi!")
        return redirect('news')

    return render(request, 'create.html')


def update(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.name = request.POST.get('name', user.name)
        user.short_info = request.POST.get('short_info', user.short_info)
        user.description = request.POST.get('description', user.description)
        if 'image' in request.FILES:
            user.image = request.FILES['image']
        user.save()
        messages.success(request, "Foydalanuvchi muvaffaqiyatli yangilandi!")
        return redirect('details', id=user.id)
    return render(request, 'update.html', {'user': user})


def delete(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, "Foydalanuvchi muvaffaqiyatli o‘chirildi!")
        return redirect('news')
    return render(request, 'delete.html', {'user': user})
