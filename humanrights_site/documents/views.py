import django.views.generic
import documents.models


class AllAttachmentsListView(django.views.generic.ListView):
    model = documents.models.Attachment
    template_name = 'documents/all_attachments_list.html'  # You can customize this
    context_object_name = 'attachments'  # This will be the variable name in your template
    paginate_by = 20  # Optional: add pagination with 20 items per page

    def get_queryset(self):
        queryset = super().get_queryset()

        # Add file size information to each attachment
        #queryset = queryset.select_related('article')

        return queryset.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pageTitle'] = "Documents"
        return context


