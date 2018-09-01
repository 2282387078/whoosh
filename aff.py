from whoosh.index import create_in 
from whoosh.fields import *
from jieba.analyse import ChineseAnalyzer
analyzer = ChineseAnalyzer()
schema = Schema(title = TEXT(stored = True),path = ID(stored=True),content=TEXT(stored=True,analyzer=analyzer))
ix = create_in('path',schema) #（这里的'indexer'实际上是一个目录，因此按照这个步骤来会出错，你得先创建目录，译者注）
writer = ix.writer() 
writer.add_document(title=u'First document',path=u'/a', content = u'this is the first document we’ve add!')
writer.add_document(title=u'Second document', path=u'/b', content=u'The second one is even more interesting!') 
writer.commit()



from whoosh.qparser import QueryParser 
with ix.searcher() as searcher: 
    query = QueryParser('content', ix.schema).parse('one')
    results = searcher.search(query)
    results[0]
    print(results[0])
    {'title': u'First document', 'path': u'/a'}