import requests
from bs4 import BeautifulSoup

def extract_streams(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if request was successful
        if response.status_code == 200:
            # Parse HTML content
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find all the elements containing the streams
            stream_elements = soup.find_all('a', href=True)
            
            # Extract the links
            stream_links = [link['href'] for link in stream_elements]
            
            # Generate downloadable links if needed
            downloadable_links = [link if link.startswith('http') else f"{url}/{link}" for link in stream_links]
            
            return downloadable_links
        else:
            print("Failed to fetch the page.")
            return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def main():
    print("Welcome to the Stream Extractor!")
    while True:
        url = input("Please enter the URL of the website with streams (or 'quit' to exit): ")
        if url.lower() == 'quit':
            print("Goodbye!")
            break
        else:
            downloadable_links = extract_streams(url)
            if downloadable_links:
                print("Downloadable Links:")
                for link in downloadable_links:
                    print(link)
            else:
                print("No streams found or unable to extract streams.")

if __name__ == "__main__":
    main()
