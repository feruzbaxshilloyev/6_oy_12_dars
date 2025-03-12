from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from .serializers import UserSerializer
from django.shortcuts import render, get_object_or_404
from .models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        short_info = request.POST.get('short_info')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        if not name or not short_info or not description or not image:
            messages.error(request, "Barcha maydonlarni to‘ldiring!")
            return redirect('create')

        new_user = User(name=name, short_info=short_info, description=description, image=image)
        new_user.save()

        messages.success(request, "Foydalanuvchi muvaffaqiyatli yaratildi!")
        return redirect('home')

    return render(request, 'create.html')


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
    news = get_object_or_404(User, id=id)
    return render(request, 'detail.html', {'news': news})


def search(request):
    return render(request, 'search.html')


class RegisterAPI(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPI(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)


class ProfileAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def update(request, id):
    user = get_object_or_404(User, id=id)

    if request.method == 'POST':
        data = request.POST.copy()
        files = request.FILES
        serializer = UserSerializer(user, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()

            if 'image' in files:
                user.image = files['image']
                user.save()

            messages.success(request, "Muvaffaqiyatli yangilandi!")
            return redirect('details', id=user.id)
        else:
            messages.error(request, "Ma’lumotlarni yangilashda xatolik!")

    return render(request, 'update.html', {'user': user})


def delete(request, id):
    if request.method == 'POST':
        user = get_object_or_404(User, id=id)
        user.delete()
        messages.success(request, "Muvaffaqiyatli foydalanuvchi o‘chirildi!")
        return redirect('home')

    return render(request, 'delete.html')


class RegisterAPI(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            return Response({"message": "Foydalanuvchi muvaffaqiyatli ro‘yxatdan o‘tdi"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPI(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return Response({"message": "Login muvaffaqiyatli bajarildi"}, status=status.HTTP_200_OK)
        return Response({"error": "Login yoki parol noto‘g‘ri"}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"message": "Tizimdan chiqdingiz"}, status=status.HTTP_200_OK)


class ProfileAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Profil muvaffaqiyatli yangilandi"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
