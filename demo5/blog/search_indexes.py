from haystack import indexes
from .models import Dynamic

class DynamicIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    def get_model(self):
        return Dynamic

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

