from django.shortcuts import render
from django.views.generic import ListView
from app.models import News
import logging

logger = logging.getLogger(__name__)

# Create your views here.
class NewsList(ListView):
    model = News

    def get_queryset(self):
        logger.debug(f"Request to NewsList from user: {self.request.user.id} with params: {self.request.GET}")
        logger.info("NewsList.get_queryset called")
        try:
            news = News.objects.select_related("region").all()
        except Exception as exc:
            logger.error(str(exc))
            raise
        if not news:
            logger.warning("News list is empty")
        import q; q(news); q(news[0])
        return news