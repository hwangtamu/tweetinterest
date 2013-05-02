__author__ = 'han'
import simplejson, json, urllib, csv
with open('data/results/userresult2.json', 'r') as f:
    for i in f:
        d = simplejson.loads(i)

for id in d.keys()[:10]:
    user = urllib.urlopen('https://api.twitter.com/1/users/show.json?user_id='
                          + str(id) + '&TwitterAPI&include_entities=true')
    u = simplejson.loads(user.read())

    d[id]['url'] = 'https://twitter.com/' + u['screen_name']
with open('data/results/user_url.json', 'w') as g:
    json.dump(d, g)

#with open('laosiji.json', 'w') as csvfile:
