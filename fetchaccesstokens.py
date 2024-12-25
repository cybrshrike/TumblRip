import requests
from requests_oauthlib import OAuth1Session

# Tumblr API credentials
consumer_key = 'KEY'
consumer_secret = 'SECRET'

# Step 1: Obtain request token
request_token_url = "https://www.tumblr.com/oauth/request_token"
oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)
response = oauth.fetch_request_token(request_token_url)

# Extract request token
resource_owner_key = response.get('oauth_token')
resource_owner_secret = response.get('oauth_token_secret')

print("Request Token:", resource_owner_key)
print("Request Secret:", resource_owner_secret)

# Step 2: Direct user to authorize URL
base_authorization_url = "https://www.tumblr.com/oauth/authorize"
authorization_url = oauth.authorization_url(base_authorization_url)
print("Visit this URL to authorize the app:", authorization_url)

# Step 3: Manually Extract Verifier Code
print("\nAfter authorizing the app, Tumblr will redirect you to the callback URL.")
print("Look for the 'oauth_verifier' parameter in the URL and paste it below.")
verifier = input("Enter the OAuth verifier code: ")

# Step 4: Fetch access token
access_token_url = "https://www.tumblr.com/oauth/access_token"
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=resource_owner_key,
    resource_owner_secret=resource_owner_secret,
    verifier=verifier
)
access_token_data = oauth.fetch_access_token(access_token_url)

# Extract access token and secret
access_token = access_token_data.get('oauth_token')
access_token_secret = access_token_data.get('oauth_token_secret')

print("Access Token:", access_token)
print("Access Secret:", access_token_secret)