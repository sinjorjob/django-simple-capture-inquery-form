from django import forms
from captcha.fields import CaptchaField, CaptchaTextInput
from django.core.mail import send_mail  #追加
from config import settings  #追加
from django.urls import reverse  #追加
import smtplib  #追加


class ContactForm(forms.Form):

    name = forms.CharField(label="氏名")
    email = forms.EmailField(label="連絡先アドレス")
    subject = forms.CharField(label="タイトル")
    message = forms.CharField(label="お問い合わせ内容", 
                            widget=forms.Textarea(attrs={'rows':4, 'cols':40}))
    captcha = CaptchaField(widget=CaptchaTextInput(attrs={'placeholder':'上記のアルファベットを入力してください。'}))
  

    #ここから下を追加
    def send_email(self):

        subject = '[Inquiry Form] from %s' % settings.SITE_URL + reverse('contact_form')
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        body = """
        氏名: %s
        メールアドレス: %s
        問い合わせ内容: %s
        """ %(name, email, message)
        sender = email
        receipient = settings.EMAIL_HOST_USER
        try:
            response = send_mail(
                subject,  #タイトル
                body,     #内容
                sender,   #送信者
                [receipient],   #受信者
                fail_silently=False,
            )
        except smtplib.SMTPException:
            pass
        return response 