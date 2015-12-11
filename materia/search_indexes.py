from haystack import indexes
from .models import MateriaLegislativa

class MateriaLegislativaIndex(indexes.SearchIndex, indexes.Indexable):
    
    text = indexes.CharField(document=True)

    ementa = indexes.CharField(model_attr='ementa')

    def get_model(self):
        return MateriaLegislativa

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()