from eventex.subscriptions.forms import SubscriptionForm
from django.http import HttpResponse
from django.shortcuts import render
from django.template import context


def subscribe(request):
    context = {'form': SubscriptionForm()}
    return render(request, 'subscriptions/subscription_form.html', context)

