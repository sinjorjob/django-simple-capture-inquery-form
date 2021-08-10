from django.views.generic.edit import FormView
from contact.forms import ContactForm
from django.urls import reverse
from django.shortcuts import render
from django.views.generic.base import TemplateView


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/message/'

    def is_valid(self, form):
        #SimpleCaptchaを使用してフォームを検証する。
        if form.is_valid():
            human = True


    def form_valid(self, form):
        response = form.send_email()
        self.success_url = reverse('message', kwargs=
                        {'visitor':form.cleaned_data['name'], 
                            'result':response})
        return super().form_valid(form)


class MessageView(TemplateView):
    template_name = 'message.html'
    
    
    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['result'] = self.kwargs['result']
        context['visitor'] = self.kwargs['visitor']

        return render(request, self.template_name, context)