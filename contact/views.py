from django.shortcuts import render
from .forms import MessageForm

# Create your views here.

def message(request):
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent to admin!')
        
            return render("/")
        else:
            messages.error(request, 'Failed to send message. Please ensure the form is valid.')
    else:
        form = MessageForm()
        context = {
                'form':form,
                }
        return render(request, 'contact/contact.html', context)
    
    return render(request, 'contact/contact.html')
