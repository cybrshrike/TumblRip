import pytumblr
import json

# Enter your Tumblr API credentials
consumer_key = 'KEY'
consumer_secret = 'SECRET'
oauth_token = 'PASTE WHAT WAS FETCHED BY FETCHACCESSTOKENS'
oauth_secret = 'PASTE WHAT WAS FETCHED BY FETCHACCESSTOKENS'

# Initialize Tumblr client
client = pytumblr.TumblrRestClient(
    consumer_key,
    consumer_secret,
    oauth_token,
    oauth_secret
)

# Fetch likes
def fetch_likes():
    likes = []
    offset = 0
    while True:
        print(f"Fetching likes with offset {offset}...")
        liked_posts = client.likes(offset=offset, limit=20)
        print("Response:", liked_posts)  # Debugging line
        if 'liked_posts' not in liked_posts:
            print("Key 'liked_posts' not found in response.")
            break
        likes.extend(liked_posts['liked_posts'])
        offset += 20
    return likes

# Save likes to a file
def save_likes(likes):
    with open('tumblr_likes.json', 'w', encoding='utf-8') as f:
        json.dump(likes, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    print("Fetching likes...")
    likes = fetch_likes()
    print(f"Fetched {len(likes)} liked posts.")
    save_likes(likes)
    print("Likes saved to tumblr_likes.json")