create_new_record = """INSERT INTO topics(name, type, startdate, enddate, news_ids)
VALUES (%(name)s,%(type)s,%(startdate)s,%(enddate)s,%(news_ids)s) RETURNING id;"""

update_news_id = """update topics set news_ids = array_append(news_ids,%(news_ids)s) where id=%(id)s;"""

find_record = """select id from topics where name = %(name)s and startdate = %(date)s;"""