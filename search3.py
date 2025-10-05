import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def fetch_video_from_network(url):
    """ Fetches the real .mp4 video link from a Twitter/X post using DevTools network interception. """
    
    # Set up Chrome options
    options = Options()
    options.headless = True  # Run the browser in headless mode
    
    # Set up the WebDriver with DevTools for network interception
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    # Open the URL
    driver.get(url)
    
    # Wait for the page to load (wait for video element to be visible)
    try:
        # Adjust the waiting condition to look for the video tag
        video_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'video'))
        )
    except Exception as e:
        print("Failed to load the video element:", e)
        driver.quit()
        return None

    # Enable the DevTools Protocol for monitoring network requests
    driver.execute_cdp_cmd("Network.enable", {})
    
    # Variable to store the video URL
    video_url = None

    # Callback function to capture network responses
    def handle_request(request):
        nonlocal video_url
        if 'video' in request['response']['mimeType']:  # Look for video responses
            video_url = request['response']['url']
            print("Video URL found:", video_url)
    
    # Listen to the network responses
    driver.request_interceptor = handle_request

    # Keep the browser running until we find the video URL
    while video_url is None:
        time.sleep(1)

    driver.quit()

    return video_url

def main():
    print("\nTwitter/X Gif Downloader")
    twitter_url = input("Enter the full Twitter/X post URL: ").strip()

    if not twitter_url.startswith("https://x.com/") and not twitter_url.startswith("https://twitter.com/"):
        print("Invalid URL. Please enter a valid Twitter/X link.")
        return

    video_link = fetch_video_from_network(twitter_url)
    
    if video_link:
        print("\nThe real video link is: \n\n" + video_link)
    else:
        print("\nNo valid video link found.")

if __name__ == "__main__":
    main()
