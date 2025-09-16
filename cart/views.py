from django.shortcuts import render, get_object_or_404, redirect
from movies.models import Movie
from .utils import calculate_cart_total
from .models import Order, Item, Feedback
from django.contrib.auth.decorators import login_required
from django.contrib import messages
def index(request):
    cart_total = 0
    movies_in_cart = []
    cart = request.session.get('cart', {})
    movie_ids = list(cart.keys())
    if (movie_ids != []):
        movies_in_cart = Movie.objects.filter(id__in=movie_ids)
        cart_total = calculate_cart_total(cart, movies_in_cart)
    template_data = {}
    template_data['title'] = 'Cart'
    template_data['movies_in_cart'] = movies_in_cart
    template_data['cart_total'] = cart_total
    return render(request, 'cart/index.html',
        {'template_data': template_data})
def add(request, id):
    get_object_or_404(Movie, id=id)
    cart = request.session.get('cart', {})
    cart[id] = request.POST['quantity']
    request.session['cart'] = cart
    return redirect('cart.index')
def clear(request):
    request.session['cart'] = {}
    return redirect('cart.index')
@login_required
def purchase(request):
    cart = request.session.get('cart', {})
    movie_ids = list(cart.keys())
    if (movie_ids == []):
        return redirect('cart.index')
    movies_in_cart = Movie.objects.filter(id__in=movie_ids)
    cart_total = calculate_cart_total(cart, movies_in_cart)
    order = Order()
    order.user = request.user
    order.total = cart_total
    order.save()
    for movie in movies_in_cart:
        item = Item()
        item.movie = movie
        item.price = movie.price
        item.order = order
        item.quantity = cart[str(movie.id)]
        item.save()
    request.session['cart'] = {}
    template_data = {}
    template_data['title'] = 'Purchase confirmation'
    template_data['order_id'] = order.id
    template_data['show_feedback_modal'] = True
    return render(request, 'cart/purchase.html',
        {'template_data': template_data})

def submit_feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        feedback_text = request.POST.get('feedback_text', '').strip()
        
        if feedback_text:  # Only save if there's feedback text
            feedback = Feedback()
            feedback.name = name if name else None
            feedback.feedback_text = feedback_text
            if request.user.is_authenticated:
                feedback.user = request.user
            feedback.save()
            messages.success(request, 'Thank you for your feedback!')
        else:
            messages.warning(request, 'Please provide feedback text.')
    
    return redirect('cart.feedback_list')

def feedback_list(request):
    feedbacks = Feedback.objects.all().order_by('-date')
    template_data = {}
    template_data['title'] = 'Customer Feedback'
    template_data['feedbacks'] = feedbacks
    return render(request, 'cart/feedback_list.html',
        {'template_data': template_data})
# Create your views here.
