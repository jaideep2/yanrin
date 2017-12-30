from flask import render_template
from yanrin import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Jaideep'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/news/<date>')
def show_summary(date):
    date = date
    topics = [
        {
            'name': 'north_korea',
        },
        {
            'name': 'gun_violence',
        },
        {
            'name': 'google',
        },
        {
            'name': 'star_wars',
        },
        {
            'name': 'syrian',
        },
        {
            'name': 'climate_change',
        },
        {
            'name': 'nuclear',
        }
    ]
    summary = '''Pyongyang, North Korea Last September, I made my first visit to North Korea, granted a rare glimpse of what goes on beyond the demilitarized zone, in one of the most mysterious places on Earth. North Korea's diplomats insisted on reading out a statement of protest while being heckled by defectors, who the North Koreans referred to as "Human scum" before storming out of the room. A scathing United Nations report last year, based in large part on testimony from hundreds of defectors, portrayed North Korea as a brutal state "That does not have any parallel in the contemporary world." 'Hermit Kingdom' North Korea has strongly denied the allegations of murder, torture, sexual violence, slavery, and mass starvation.'''
    return render_template('news.html', title='Todays News Summary', date=date, topics=topics, summary=summary)
