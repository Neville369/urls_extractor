# urls_extractor
This Python script reads a text file to extract and print all URLs found within its contents using regular expressions. Here's a detailed description:

1. **Importing the Regular Expression Library**:
   - The script imports the `re` module, which provides support for working with regular expressions.

2. **Defining a Function to Print and Return All URLs**:
   - The `get_urls` function takes a list of URLs (`all_urls`) as input.
   - It iterates over each URL in the list and prints it.
   - It returns the list of URLs.

3. **Opening and Reading the Text File**:
   - The script opens a file named `search.txt` in read mode.
   - It reads the entire contents of the file into a string variable named `file_contents`.

4. **Using Regular Expressions to Find All URLs**:
   - The script uses the `re.findall` function with a regex pattern to find all URLs in the `file_contents` string.
   - The regex pattern used (`r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'`) matches typical URL formats.

5. **Getting and Printing All URLs**:
   - The script calls the `get_urls` function with the list of URLs found by the regex.
   - It prints each URL individually within the `get_urls` function.
   - Finally, it prints the list of all URLs.

This script is useful for extracting and displaying all URLs from a given text file, which can be helpful for tasks such as web scraping, data extraction, or content analysis.
