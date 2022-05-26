# API KEY and Search Engine ID from Google custom search service
api_key = "AIzaSyC9IvwwN4w5XnlNWaEqZ7ljd0ezN-8G_ec"
search_engine_id = "62a6fb145cb951abf"

# Install google-api-python-client module
from apiclient.discovery import build

# Use build function to use Google service: customsearch version 1
resourse = build("customsearch", "v1", developerKey=api_key).cse()

# Create an empty dictionary
FoundData = []

for i in range(101, 151, 10):
    # Use list function to query the keyword
    try:
        result = resourse.list(q="zalo", cx=search_engine_id, start=i).execute()

        # Add each found items to FoundData
        FoundData += result['items']
    except Exception as exc:
        print("There was a problem: %s" % (exc))

# Loop over the dictionary
for i, item in enumerate(FoundData):
        try:
            long_description = item["pagemap"]["metatags"][0]["og:description"]
        except KeyError:
            long_description = "N/A"
        # get the title
        title = item.get("title")
        # page snippet
        snippet = item.get("snippet")
        # alternatively, you can get the HTML snippet (bolded keywords)
        html_snippet = item.get("htmlSnippet")
        # extract the page url
        link = item.get("link")
        # print the results
        print("="*10, f"Result #{i+1}", "="*10)
        print("Title:", title)
        print("Description:", snippet)
        print("Long description:", long_description)
        print("URL:", link, "\n")    

