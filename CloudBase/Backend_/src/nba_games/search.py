from django_elasticsearch_dsl import DocType, Index
from .models import teaminfo
posts = Index('posts')

@posts.doc_type
class statsDocument(DocType):
	class Meta:
		model=teaminfo

		fields=[
			'teamcode',
			'teamname',
			'officialSite',
		]