import requests
from bs4 import BeautifulSoup
import os

def extract_video_streams(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if request was successful
        if response.status_code == 200:
            # Parse HTML content
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find all the elements containing video streams
            video_elements = soup.find_all('video')
            
            # Extract video names and video source links
            video_info = []
            for video in video_elements:
                # Extract video name
                video_name = video.get('title', 'Video Name not available')
                
                # Extract video source link
                video_src = video.find('source').get('src')
                
                video_info.append({'name': video_name, 'link': video_src})
                
            return video_info
        else:
            print("Failed to fetch the page.")
            return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def main():
    print("Welcome to the Video Stream Extractor!")
    while True:
        url = input("Please enter the URL of the website with video streams (or 'quit' to exit): ")
        if url.lower() == 'quit':
            print("Goodbye!")
            break
        else:
            video_streams = extract_video_streams(url)
            if video_streams:
                print("Video Streams:")
                for video in video_streams:
                    print(f"Name: {video['name']}")
                    print(f"Link: {video['link']}")
                    print("\n")
            else:
                print("No video streams found or unable to extract video streams.")

if __name__ == "__main__":
    main()
