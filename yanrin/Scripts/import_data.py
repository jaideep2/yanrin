'''
To run: python import_data.py ../../files/articles3.csv
'''
import csv
import psycopg2
import sys
csv.field_size_limit(sys.maxsize)

ranks = {
    'Breitbart':2,
    'Business Insider':3,
    'Fox News':4,
    'Atlantic':5,
    'New York Post':5,
    'Talking Points Memo':6,
    'Buzzfeed News':6,
    'National Review':7,
    'Guardian':7,
    'Vox':7,
    'CNN':7,
    'New York Times':8,
    'Washington Post':8,
    'Reuters':9,
    'NPR':10,
}

sql_statement = """INSERT INTO news(title, publication, author, date, year, month, url, content, rank)
VALUES (%(title)s,%(publication)s,%(author)s,%(date)s,%(year)s,%(month)s,%(url)s,%(content)s,%(rank)s) RETURNING id;"""

file_location = sys.argv[1]
lines = 1
try:
    conn = psycopg2.connect("dbname=jaideepsingh user=jaideepsingh")
    cur = conn.cursor()
    with open(file_location, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            if len(row)==10:
                print(row[0])
                title       = row[2]
                publication = row[3]
                author      = row[4]
                date        = row[5] if row[5] != 'nan' else '1970-01-01'
                year        = int(row[6].split('.')[0]) if row[6] else int(date.split('-')[0])
                month       = int(row[7].split('.')[0]) if row[7] else int(date.split('-')[1])
                url         = row[8]
                content     = row[9]
                rank        = ranks[publication]
                cur.execute(sql_statement, {'title':title,'publication':publication,'author':author,'date':date,\
                                            'year':year,'month':month,'url':url,'content':content,'rank':rank})

    conn.commit()
    cur.close()
    conn.close()
except (Exception, psycopg2.DatabaseError) as error:
        print(error)
finally:
    if conn is not None:
        conn.close()