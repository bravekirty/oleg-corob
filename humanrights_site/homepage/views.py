import django.views.generic
import django.shortcuts
import django.urls

import articles.models

class HomeView(django.views.generic.ListView):
    model = articles.models.Article
    template_name = "homepage/home.html"
    context_object_name = "articles"
    queryset = articles.models.Article.objects.order_by('-created_at')[:3]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pageTitle'] = "Home"
        return context


class AboutView(django.views.generic.TemplateView):
    def get(self, request, *args, **kwargs):
        return django.shortcuts.redirect(django.urls.reverse("homepage:home"))


    # class StaticPageView(django.views.generic.TemplateView):
#     template_name = "static/{}.html"
#
#     def get_template_names(self):
#         page_name = self.kwargs.get('page_name')
#         return [self.template_name.format(page_name)]

