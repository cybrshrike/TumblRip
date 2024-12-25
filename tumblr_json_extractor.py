import os
import json
import requests
import re

# Load the JSON file
with open('tumblr_likes.json', 'r', encoding='utf-8') as f:
    likes = json.load(f)

# Create output folders
os.makedirs("tumblr_media/images", exist_ok=True)
os.makedirs("tumblr_media/videos", exist_ok=True)
os.makedirs("tumblr_media/text_posts", exist_ok=True)

# Sanitize filenames to avoid illegal characters
def sanitize_filename(filename):
    return re.sub(r'[\/:*?"<>|]', '_', filename)

# Process each post
for post in likes:
    post_type = post.get('type')
    post_id = post.get('id')
    blog_name = post.get('blog_name', 'unknown_blog')

    if post_type == 'photo':
        # Download images
        photos = post.get('photos', [])
        for i, photo in enumerate(photos):
            image_url = photo.get('original_size', {}).get('url')
            if image_url:
                try:
                    print(f"Downloading image: {image_url}")
                    response = requests.get(image_url)
                    response.raise_for_status()
                    # Save the image
                    image_filename = f"tumblr_media/images/{sanitize_filename(blog_name)}_post_{post_id}_photo_{i + 1}.jpg"
                    with open(image_filename, 'wb') as img_file:
                        img_file.write(response.content)
                except Exception as e:
                    print(f"Failed to download image: {image_url}, Error: {e}")

    elif post_type == 'video':
        # Download videos
        video_url = post.get('video_url')
        if video_url:
            try:
                print(f"Downloading video: {video_url}")
                response = requests.get(video_url)
                response.raise_for_status()
                # Save the video
                video_filename = f"tumblr_media/videos/{sanitize_filename(blog_name)}_post_{post_id}_video.mp4"
                with open(video_filename, 'wb') as video_file:
                    video_file.write(response.content)
            except Exception as e:
                print(f"Failed to download video: {video_url}, Error: {e}")

    elif post_type == 'text':
        # Save text content
        post_title = post.get('title', f"post_{post_id}")
        text_content = post.get('body', 'No content available')

        # Combine title and username into the filename
        text_filename = sanitize_filename(f"{blog_name}_{post_title}.txt")
        text_file_path = os.path.join("tumblr_media/text_posts", text_filename)

        try:
            print(f"Saving text post: {text_file_path}")
            with open(text_file_path, 'w', encoding='utf-8') as text_file:
                text_file.write(f"Blog: {blog_name}\n")
                text_file.write(f"Post ID: {post_id}\n")
                text_file.write(f"Title: {post_title}\n")
                text_file.write(f"{'-' * 40}\n")
                text_file.write(text_content)
        except Exception as e:
            print(f"Failed to save text post ID {post_id}, Error: {e}")

print("Download completed. Check the 'tumblr_media' folder for your files.")