from django.utils import timezone
from articles.models import Article


def get_latest_articles(request):
    return {
        'latest_articles': Article.objects.filter(
            created_at__lte=timezone.now()
        ).order_by('-created_at')[:4]
    }