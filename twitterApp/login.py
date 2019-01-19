import twitterApp.constants
import oauth2
import urllib.parse as urlparse
import json

consumer = oauth2.Consumer(twitterApp.constants.CONSUMER_KEY, twitterApp.constants.CONSUMER_SECRET)
client = oauth2.Client(consumer)


response, content = client.request(twitterApp.constants.REQUEST_TOKEN_URL, 'POST')
if response.status != 200:
    print("An error occurred getting the response from Twitter")


request_token = dict(urlparse.parse_qsl(content.decode('utf-8')))

print("Go to the following site in your browser")
print("{}?oauth_token={}".format(twitterApp.constants.AUTHORIZATION_URL, request_token['oauth_token']))


oauth_verifier = input("Enter the PIN")

token = oauth2.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
token.set_verifier(oauth_verifier)
client = oauth2.Client(consumer, token)


response, content = client.request(twitterApp.constants.ACCESS_TOKEN_URL, 'POST')
access_token = dict(urlparse.parse_qsl(content.decode('utf-8')))

print(access_token)

authorized_token = oauth2.Token(access_token['oauth_token'], access_token['oauth_token_secret'])
authorized_client = oauth2.Client(consumer, authorized_token)

response, content = authorized_client.request('https://api.twitter.com/1.1/search/tweets.json?q=computers+filter:images', 'GET')
if response.status != 200:
    print("An error occurred when searching")

tweets = json.loads(content.decode('utf-8'))

for tweet in tweets['statuses']:
    print(tweet['text'])
