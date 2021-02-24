from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.
# from django.core.exceptions import PermissionDenied
from .forms import CsRegisterForm
from django.views.generic import CreateView
 
class CsRegisterView(CreateView):
    model = User
    template_name = 'users/register_cs.html'
    form_class = CsRegisterForm

    def get(self, request, *args, **kwargs):
        # if not request.session.get('agreement', False):
        #     raise PermissionDenied
        request.session['agreement'] = False
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        messages.success(self.request, "회원가입 성공.")
        return redirect('users:login')

    def form_valid(self, form):
        self.object = form.save()
        return redirect(self.get_success_url())