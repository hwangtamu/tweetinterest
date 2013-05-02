__author__ = 'han'
import urllib
import simplejson, json


def get_id(q):
    user = urllib.urlopen('https://api.twitter.com/1/users/show.json?screen_name=' + q +'&include_entities=true')
    d = simplejson.loads(user.read())
    return d['id_str']


def get_tweets(q,dir):
    data = {}
    search = urllib.urlopen('https://api.twitter.com/1/statuses/user_timeline.json?'
                            + 'include_entities=true&include_rts=true&screen_name=' + str(q) + '&count=101')
    d = simplejson.loads(search.read())
    if len(d) > 1:
        for tweet in d:
            data[tweet['created_at'][:20]] = tweet['text']
        with open(dir + get_id(q) + '.json', 'w') as f:
            json.dump(data, f)




