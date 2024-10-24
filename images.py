import os
import requests

# List of image URLs
image_urls = ['',]

# Save location on macOS
save_dir = "/Users/user/Documents/images"

# Create the location if the directory doesn't exist
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Function to download image(s)
def download_image(url, save_dir):
    try:
        # Get the image content from the url
        response = requests.get(url, stream=True)
        response.raise_for_status() # Raise an error for bad status codes

        # Extract the image filename from the URL
        filename = os.path.join(save_dir, url.split('/')[-1])

        # Save the image to the specified directory
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Downloaded: {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")

# Download all images
for url in image_urls:
    download_image(url, save_dir)
