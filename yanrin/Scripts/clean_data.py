import psycopg2
from time import strptime
try:
    conn = psycopg2.connect("dbname=jaideepsingh user=jaideepsingh")
    cur = conn.cursor()
    '''
    jaideepsingh=# select count(*) from news where date = '1970-01-01' and publication='Talking Points Memo';
      2599
    jaideepsingh=# select count(*) from news where publication='Talking Points Memo';
      5214
    '''
    cur.execute('''select id,url from news where date = '1970-01-01' and publication='Talking Points Memo';''')
    rows = cur.fetchall()
    for id,url in rows:
        print(id)
        date = url.split('/')[4][:8]
        try:
            print(int(date))
            year = date[:4]
            month = date[4:6]
            cur.execute('''update news set date=%(date)s,year=%(year)s,month=%(month)s where id=%(id)s;''',\
            {'id':id,'date':date,'year':year,'month':month})
        except Exception as error:
            print('yo ',error)
            continue
    '''
    jaideepsingh=# select count(*) from news where publication='Guardian';
      8681
    jaideepsingh=# select count(*) from news where date = '1970-01-01' and publication='Guardian';
        40
    '''
    cur.execute('''select id,url from news where date = '1970-01-01' and publication='Guardian';''')
    rows = cur.fetchall()
    for id, url in rows:
        if 'theguardian' in url:
            print(id)
            date = url.split('/')[-4:-1]
            day = date[2]
            year = date[0]
            month = str(strptime(date[1], '%b').tm_mon)
            date = date[0]+'-'+month+'-'+date[2]
            #print(date)
            cur.execute('''update news set date=%(date)s,year=%(year)s,month=%(month)s where id=%(id)s;''', \
                        {'id': id, 'date': date, 'year': year, 'month': month})
    conn.commit()
    cur.close()
    conn.close()
except (psycopg2.DatabaseError) as error:
        print(error)
finally:
    if conn is not None:
        conn.close()

#Final news count : 142565