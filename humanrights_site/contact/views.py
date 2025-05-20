import django.views.generic
import django.urls

class ContactView(django.views.generic.TemplateView):
    template_name = "contact/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pageTitle'] = "Contact"
        return context