import re

# Author: Joshua Rubin-Garcia
# Function: Extracts the direct .mp4 link from a Twitter (X) post's HTML.

def extract_mp4_links(filename):
    """ Extracts all .mp4 links from the given HTML file and prioritizes tweet videos. """
    mp4_links = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            matches = re.findall(r'https?://[^"]+\.mp4', line)
            mp4_links.extend(matches)

    # Filter for tweet videos (avoid UI assets)
    tweet_videos = [link for link in mp4_links if "video.twimg.com" in link]

    if tweet_videos:
        return tweet_videos[0]  # Return first valid tweet video link
    elif mp4_links:
        return mp4_links[0]  # Fallback (in case of incorrect filtering)
    else:
        return None


def main():
    filename = "data/data.txt"  # Ensure this is the correct HTML file
    video_link = extract_mp4_links(filename)

    if video_link:
        print("\nThe link to the mp4 provided is: \n\n" + video_link)
    else:
        print("\nNo valid .mp4 link found.")

main()
