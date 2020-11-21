import json
import urllib

queries=0
f = open(r'C:\Users\716907\.spyder-py3\test_queries.txt','r',encoding="utf8")

for line in f.readlines():

    queries=queries+1
    query=''
    words=line.split()
    qid= words[0]
    
    for word in words[1:]:
        query= query+word+'+'
        
    query=query[:-1]
    query_args= {'q':query}
    encoded_args = urllib.parse.quote_plus(query)
    
# change the url according to your own corename and query
    inurl = 'http://18.188.124.203:8983/solr/LM/select?q='+encoded_args+'&defType=edismax&qf=text_en+text_de+text_ru&fl=id%2Cscore&wt=json&indent=true&rows=20'
    outfn ='C:\\Users\\bhakti\\'+str(queries)+'.txt'
    

# change query id and IRModel name accordingly
    IRModel='LM'
    outf = open(outfn, 'a+',encoding="utf8")
    data = urllib.request.urlopen(inurl)
# if you're using python 3, you should use
# data = urllib.request.urlopen(inurl)

    docs = json.load(data)['response']['docs']
    print(docs)
# the ranking should start from 0 and increase
    rank = 0
    for doc in docs:
        outf.write(qid + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + IRModel + '\n')
        rank += 1
    outf.close()
