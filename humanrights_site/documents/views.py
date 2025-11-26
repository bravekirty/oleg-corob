import os

import django.views.generic
import django.shortcuts
import django.http
import documents.models


class AllAttachmentsListView(django.views.generic.ListView):
    model = documents.models.Attachment
    template_name = 'documents/all_attachments_list.html'
    context_object_name = 'attachments'
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.select_related('article').order_by('order')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pageTitle'] = "Documents"

        # Get the file ID from URL parameter
        file_id = self.request.GET.get('file')
        if file_id:
            try:
                attachment = documents.models.Attachment.objects.get(id=file_id)
                context['open_file_id'] = attachment.id
                context['open_file_url'] = attachment.file.url
                context['open_file_name'] = attachment.name
                context['open_file_extension'] = os.path.splitext(attachment.file.name)[1].lower()
            except documents.models.Attachment.DoesNotExist:
                pass

        return context