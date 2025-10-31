import os

import django.views.generic
import django.shortcuts
import django.http
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


class AttachmentDetailView(django.views.generic.DetailView):
    model = documents.models.Attachment
    template_name = 'documents/attachment_detail.html'
    context_object_name = 'attachment'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pageTitle'] = f"Document - {self.object.name}"
        return context


def attachment_file_view(request, pk):
    """
    View to display attachment file in the PDF viewer
    """
    try:
        attachment = documents.models.Attachment.objects.get(pk=pk)

        # Check if it's a PDF file
        file_extension = os.path.splitext(attachment.file.name)[1].lower()
        is_pdf = file_extension == '.pdf'

        context = {
            'attachment': attachment,
            'is_pdf': is_pdf,
            'pageTitle': f"Viewing - {attachment.name}",
        }

        return django.shortcuts.render(request, 'documents/attachment_file_view.html', context)

    except documents.models.Attachment.DoesNotExist:
        return django.http.HttpResponseNotFound("Attachment not found")