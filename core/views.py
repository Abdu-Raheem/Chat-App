from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User, ServiceRequest, ChatMessage
from .forms import UserRegisterForm, ServiceRequestForm, ChatMessageForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def user_dashboard(request):
    if request.user.is_customer:
        print("*"*100)
        print(request.user.is_customer)
        print("*"*100)
        return redirect('customer_dashboard')
    elif request.user.is_agent:
        print("*"*100)
        print(request.user.is_agent)
        print("*"*100)
        return redirect('agent_dashboard')
    else:
        return redirect('admin:index')
    

@login_required
def customer_dashboard(request):
    if not request.user.is_customer:
        return redirect('agent_dashboard')
    
    requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'customer_dashboard.html', {'requests': requests})


@login_required
def agent_dashboard(request):
    if not request.user.is_agent:
        return redirect('customer_dashboard')
    
    pending_requests = ServiceRequest.objects.filter(agent=request.user, status='pending')
    active_requests = ServiceRequest.objects.filter(agent=request.user, status='accepted')
    return render(request, 'agent_dashboard.html', {
        'pending_requests': pending_requests,
        'active_requests': active_requests
    })


@login_required
def create_service_request(request):
    if not request.user.is_customer:
        return redirect('agent_dashboard')
    
    agents = User.objects.filter(is_agent=True)
    
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            agent_id = request.POST.get('agent')
            agent = get_object_or_404(User, id=agent_id)
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.agent = agent
            service_request.save()
            messages.success(request, 'Service request created successfully!')
            return redirect('customer_dashboard')
    else:
        form = ServiceRequestForm()
    
    return render(request, 'service_request.html', {'form': form, 'agents': agents})


@login_required
def update_request_status(request, request_id, status):
    service_request = get_object_or_404(ServiceRequest, id=request_id, agent=request.user)
    
    if status in ['accepted', 'rejected']:
        service_request.status = status
        service_request.save()
        messages.success(request, f'Request {status} successfully!')
    
    return redirect('agent_dashboard')


@login_required
def chat(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    
    # Check if user is part of this request
    if request.user not in [service_request.customer, service_request.agent]:
        return redirect('dashboard')
    
    # Only allow chat if request is accepted
    if service_request.status != 'accepted':
        return redirect('dashboard')
    
    messages = ChatMessage.objects.filter(request=service_request).order_by('timestamp')
    
    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.request = service_request
            chat_message.sender = request.user
            chat_message.save()
            return redirect('chat', request_id=request_id)
    else:
        form = ChatMessageForm()
    
    return render(request, 'chat.html', {
        'service_request': service_request,
        'messages': messages,
        'form': form,
        'other_user': service_request.agent if request.user == service_request.customer else service_request.customer
    })