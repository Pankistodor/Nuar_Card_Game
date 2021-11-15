from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView

from Nuar_Card_Game.Nuar_Card_Game.settings import ADMIN_EMAIL as email

from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('signup')
    template_name = 'signup.html'

    def form_valid(self, form):
        self.send_mail_ls(email)
        return super().form_valid(form)

    def send_mail_ls(self, email):
        send_mail(
            'Регистрация',
            'Регистрация прошла успешно!',
            [email],
            fail_silently=False
        )
