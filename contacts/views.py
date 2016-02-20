# Create your views here.
from django.views.generic import ListView
from contacts.models import Contact
from django.views.generic import CreateView
from django.core.urlresolvers import reverse
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
import forms
from django.http import HttpResponse
from django.views.generic import View


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class LoggedInMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)

class HelloView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, World")

class ListContactView(LoggedInMixin,ListView):

    model = Contact
    template_name = 'contact_list.html'


class CreateContactView(LoggedInMixin,CreateView):
    model = Contact
    template_name = 'edit_contact.html'
    def get_success_url(self):
        return reverse('contacts-list')


class UpdateContactView(LoggedInMixin,UpdateView):

    model = Contact
    template_name = 'edit_contact.html'
    def get_success_url(self):
        return reverse('contacts-list')

    def get_context_data(self, **kwargs):
        context = super(UpdateContactView, self).get_context_data(**kwargs)
        
        context['action'] = reverse('contacts-edit',
                                    kwargs={'pk': self.get_object().id})


        return context

class DeleteContactView(LoggedInMixin,DeleteView):

    model = Contact
    template_name = 'delete_contact.html'

    def get_success_url(self):
        return reverse('contacts-list')

class ContactView(LoggedInMixin,DetailView):

    model = Contact
    template_name = 'contact.html'

class EditContactAddressView(LoggedInMixin,UpdateView):

    model = Contact
    template_name = 'edit_addresses.html'
    form_class = forms.ContactAddressFormSet

    def get_success_url(self): 
        return reverse('contacts-list')
