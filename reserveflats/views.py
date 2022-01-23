from django.shortcuts import render, redirect, HttpResponse
from .models import ReserveFlats, StripePayment
from rest_framework import viewsets
from .serializers import ReserveFlatsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from cloudipsp import Api, Checkout
from rest_framework.permissions import IsAuthenticatedOrReadOnly
import stripe
import os
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, send_mail
from .forms import SuccessForm
from website.settings.production import ACME_CHALLENGE_CONTENT

HOST = os.environ.get('HOST')
stripe.api_key = os.environ.get('API_KEY_STRIPE')


def startpage(request):
    StripePayment.objects.all().delete()
    return render(request, './index.html')


def buy(request, id):
    item = ReserveFlats.objects.get(id=id)
    if not item.reserved:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Buy flat #' + str(id),
                    },
                    'unit_amount': int(item.price) * 100,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=HOST + 'success',
            cancel_url=HOST,
        )
    StripePayment(payment_id=session.url.split('/')[4].split('#')[0]).save()
    return redirect(session.url, code=303)


def success(request):
    object_db = StripePayment.objects.get()
    stripe_id = object_db.payment_id
    session_stripe = stripe.checkout.Session.retrieve(stripe_id)
    if session_stripe["payment_status"] == 'paid':
        form = SuccessForm()
        if request.method == 'POST':
            form = SuccessForm(request.POST)
            if form.is_valid():
                flat_str = stripe.checkout.Session.list_line_items(stripe_id, limit=1)['data'][0]['description']
                price_flat = str(int(session_stripe['amount_total'] / 100))
                flat_number = flat_str.split("#")[1]
                name_buyer = request.POST['name'] + " " + request.POST['surname']
                email_buyer = request.POST['email']
                phone_buyer = request.POST['phone']
                form.save()
                html_content = render_to_string('./mail.html', {'flat_number': flat_number})
                email = EmailMessage('Buy flat #' + flat_number, html_content,
                                     'Melody Limited Co. <admin@melody.pp.ua>', [email_buyer])
                email.content_subtype = 'html'
                email.send()
                emailadmin = EmailMessage(flat_str, name_buyer + " купил(a) квартиру №" + str(
                    flat_number) + "\nНа сумму: " + price_flat + "$\nEmail: " + email_buyer + "\nPhone:" + phone_buyer,
                                          'Melody Limited Co. <admin@melody.pp.ua>', ['admin@melody.pp.ua'])
                emailadmin.send()
                StripePayment.objects.all().delete()
                return redirect(HOST)
    else:
        StripePayment.objects.all().delete()
        return redirect(HOST)
    return render(request, './success.html', context={'form': form})


def acme_challenge(request):
    return HttpResponse(ACME_CHALLENGE_CONTENT)


def cancel(request):
    StripePayment.objects.all().delete()
    return redirect(HOST)


class FlatsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ReserveFlats.objects.all()
    serializer_class = ReserveFlatsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['floor', 'id']
