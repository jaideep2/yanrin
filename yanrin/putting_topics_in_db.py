import psycopg2
import sys
from sql.statements import create_new_record, update_news_id, find_record
date = sys.argv[1]

def insert_new_row(cur, topic_name, date):
    cur.execute(create_new_record,
                {'name': topic_name, 'type': 'All', 'startdate': date, 'enddate': date, 'news_ids': '{0}'})
    print('new row done')


def update_row(cur, topic_name, date, news_id, row_id):
    cur.execute(update_news_id, {'news_ids': '%s' % news_id, 'id' : row_id})
    print('rows updated')


def insert_into_relevant_topic(cur, topic_name, date):
    cur.execute(find_record, {'name': topic_name, 'date': date})
    rows = cur.fetchall()
    if not rows:
        # if topic name doesnt exist for current date insert new topic with news_ids = 0 and given date
        insert_new_row(cur, topic_name, date)
    else:
        # if topic exists append news_id to said topic
        for news_id in [r[0] for r in rows]:
            update_row(cur, topic_name, date, news_id, rows[0][0])


def main():
    try:
        conn = psycopg2.connect("dbname=jaideepsingh user=jaideepsingh")
        cur = conn.cursor()
        #print('in main')
        #init(cur)
        #update_news_id(cur)
        topic_name = 'Test1'
        insert_into_relevant_topic(cur, topic_name, date)
        conn.commit()
        cur.close()
        conn.close()
        print('db closed')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    main()