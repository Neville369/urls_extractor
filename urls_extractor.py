import re

# Function to return all URLs
def get_urls(all_urls):
    for url in all_urls:
        print(url)
    return all_urls

# Open the text file
with open('search.txt', 'r') as file:
    # Read the file contents
    file_contents = file.read()

    # Use regular expressions to find all URLs
    all_urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', file_contents)

    # Get and print all the URLs
    urls = get_urls(all_urls)
    print(urls)  
