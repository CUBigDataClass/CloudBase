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
			'found',
			'city',
			'arena',
			'owner',
			'general_manager',
			'head_coach',
			'g_league',
			'championships',
			'retired_numbers',
				
		]