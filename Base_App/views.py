from django.shortcuts import render,HttpResponse,redirect
from Base_App.models import ItemList,Items,AboutUs,Feedback,BookTable

#IMPORT STUFFS
import random
import uuid
from django.http import JsonResponse
from .models import SpinReward
from django.utils import timezone

# Create your views here.
def Home_view(request):
    items = Items.objects.all()
    categories = ItemList.objects.all()
    review = Feedback.objects.all()

    food_categories = ItemList.objects.filter(category_type='food')
    snack_categories = ItemList.objects.filter(category_type='snack')

    return render(request, "home.html", {
        'items': items,
        'categories': categories,
        'food_categories': food_categories,
        'snack_categories': snack_categories,
        'review': review
    })

def About_view(request):
    data = AboutUs.objects.all()
    return render(request, "about.html",{'data':data})


def Menu_view(request):
    items = Items.objects.all()
    categories = ItemList.objects.all()  # Renamed variable
    return render(request, "menu.html", {'items': items, 'categories': categories})


def Book_table_view(request):
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        total_person = request.POST.get("total_person")
        booking_date = request.POST.get("booking_date")
        
        if user_name and phone_number and email and total_person and booking_date:
            data = BookTable(user_name=user_name, phone_number=phone_number, email= email, total_person=total_person, booking_date=booking_date)
            data.save()
            
    return render(request, "book_table.html")

def feedback(request):
    if request.method == "POST":
        user_name = request.POST.get("user_name", "").strip()
        description = request.POST.get("description", "").strip()
        rating = request.POST.get("rating", "").strip()
        image = request.FILES.get("image")  # ✅ Capture image from request.FILES

        if user_name and description and rating:
            feedback_entry = Feedback(user_name=user_name, description=description, rating=rating, image=image)
            feedback_entry.save()
            return redirect("feedback")  # ✅ Redirect after saving

    return render(request, "feedback.html")


# the spin function
def spin_wheel(request):

    # 🔒 LIMIT: only 1 spin per day per user (session-based)
    today = str(timezone.now().date())
    last_spin = request.session.get("last_spin_date")

    if last_spin == today:
        return JsonResponse({
            "reward": "You’ve used your spin for today. 😅",
            "code": None
        })

    # 🎯 WEIGHTED REWARDS (important upgrade)
    rewards = [
        ("5% Discount 🎉", "AMALA5", 40),     # 40%
        ("10% Discount 🔥", "AMALA10", 30),   # 30%
        ("Free Drink 🥤", "FREE-DRINK", 20),  # 20%
        ("Try Again 😅", None, 10),           # 10%
    ]

    labels = [r[0] for r in rewards]
    codes = [r[1] for r in rewards]
    weights = [r[2] for r in rewards]

    choice = random.choices(rewards, weights=weights, k=1)[0]

    reward, base_code, _ = choice

    if base_code:
        code = base_code + "-" + str(uuid.uuid4())[:5]

        SpinReward.objects.create(
            code=code,
            reward=reward
        )
    else:
        code = None

    # save spin date
    request.session["last_spin_date"] = today

    return JsonResponse({
        "reward": reward,
        "code": code
    })