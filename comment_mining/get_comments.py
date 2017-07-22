import urllib.request
import json 

get_link = "http://comentarios.emol.com/Comments/Api?action=getComments&url="
link_end = "&format=json&limit=10&order=LIKES"

def get_comments(plain_url):
    plain_comments = []
    json_url = get_link + plain_url + link_end
    with urllib.request.urlopen(json_url) as url:
        data = json.loads(url.read().decode())
        comments = data['comments']
        for com in comments:
            plain_comments.append(com['text'])
    return plain_comments