
lm = LdaModel(corpus=corpus, num_topics=20, id2word=dictionary)
lm = lm.load('/tmp/model.ldamodel')

random_document = doc[1]
print(random_document)
#Process
#train_texts = list(build_texts(doc))
#train_texts = process_texts(train_texts)
#print(train_texts)
random_vec = dictionary.doc2bow(random_document.lower().split())
matched = lm[random_vec]
matched = sorted(matched,key=lambda x: float(x[1]),reverse=True)
for topicid,freq in matched:
    topic = lm.show_topic(topicid, topn=5)
    print(topic,freq)

#Trying topic labels
print('Trying topic labels')
my_ids = []
for topicid, c_v in top_topics:
    my_ids.append(topicid)
t = ' '.join([word for word, prob in lm.show_topic(top_topics[0][0])])
#print('topic ',top_topics[0][0],t)
#print(lm.show_topic(top_topics[0][0]))
