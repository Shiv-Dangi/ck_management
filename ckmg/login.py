from django.contrib import auth

def accountLoginView(request):
    context= {}
    context['photo_list'] = Gallary.objects.all()
    context['admission_list'] = Admission.objects.all()
    context['program_list'] = Program.objects.all()
    context.update(csrf(request))
    return render_to_response('iips_site/account_login.html', context)

def accountAuthView(request):
    username = request.POST.get('username','')
    #group = request.POST.get('group','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username,password=password)
    
    if user is not None:
      auth.login(request, user)
      return HttpResponseRedirect('/account')
    else:
      return HttpResponseRedirect('/account/invalid')

    

def accountInvalidView(request):
    return render_to_response('iips_site/account_invalid.html')

def accountLogoutView(request):
    auth.logout(request)
    return render_to_response('iips_site/account_logout.html')


def accountRegisterView(request):

    if request.method == 'POST':

        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/account/register_success")
    else:
        form = MyRegistrationForm()
    return render(request, "iips_site/account_register.html", {
        'form': form,
    })


def accountRegisterSuccessView(request):
    return render_to_response('iips_site/account_register_success.html')