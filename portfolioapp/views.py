from django.shortcuts import render, redirect
from .models import AboutMe
from .models import ContactForm
from django.http import HttpResponse
from django.contrib import messages



# Create your views here.


def home(request):

    #for data rander
    aboutmeall = AboutMe.objects.get(id=1)

    #for contact form
    if request.method == 'POST':
        form = ContactForm()
        
        namev = request.POST.get('name')
        emailv = request.POST.get('email')
        subjectv = request.POST.get('subject')
        messagev = request.POST.get('message')
        
        form.first_name = namev
        form.email_add = emailv
        form.subject_name = subjectv
        form.message = messagev

        # if form.is_valid():
        #     post = form.save(commit = False)
        #     post.save()
        #     return HttpResponse("Message submitted successfully")
        # else:
        #     return render(request, "index.html", {'form':form})

        form.save()
        return redirect('home')
        # return HttpResponse("Message submitted successfully")
        # submitmessage = print("Message submitted successfully")
    #end contact form

    context = {'about': aboutmeall}
    return render(request, 'index.html', context)



# def contact(request):  
#     if request.method == 'POST':
#         form = ContactForm()

#         namev = request.POST.get('name')
#         emailv = request.POST.get('email')
#         subjectv = request.POST.get('subject')
#         messagev = request.POST.get('message')

#         form.first_name = namev
#         form.email_add = emailv
#         form.subject_name = subjectv
#         form.message = messagev

#         form.save()
#         return HttpResponse('thanks')

#     return render(request, "index.html")