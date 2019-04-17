import datetime
from haystack import indexes
from .models import stats

class statsIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	team = indexes.CharField(model_attr='team')
	date = indexes.DateTimeField(model_attr='date')
	
	def get_model(self):
		return stats
	
	def index_queryset(self,using=None):
		return self.get_model().objects.all() 

