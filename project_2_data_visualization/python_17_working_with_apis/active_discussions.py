from operator import itemgetter

import requests
import plotly.express as px

# Make an API call and check the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a new API for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    response_dict = r.json()

    # Build a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'owner': response_dict['by'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants']
    }
    submission_dicts.append(submission_dict)

# Process submission information.
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)

submission_links, comments, hover_texts = [], [], []
for submission_dict in submission_dicts:
    submission_title = submission_dict['title']
    submission_url = submission_dict['hn_link']
    submission_link = f"<a href='{submission_url}'>{submission_title}</a>"
    submission_links.append(submission_link)

    comments.append(submission_dict['comments'])

    #Build hover texts.
    hover_text = f"{submission_dict['owner']}<br />{submission_dict['title']}"
    hover_texts.append(hover_text)

# Make visualization.
title = "Most Active Discussions Recently Happening on Hacker News"
labels = {'x': 'Submission', 'y': 'Comments'}
fig = px.bar(x=submission_links, y=comments, title=title, labels=labels, 
             hover_name=hover_texts)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
                  yaxis_title_font_size=20)

fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)

fig.show()