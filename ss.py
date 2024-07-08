from apify_client import ApifyClient

# Initialize the ApifyClient with your API token
client = ApifyClient("apify_api_xCQ7X8xFLYyY5quAuMKRrRaI3Kb0gT0zzA5F")

# Prepare the Actor input
run_input = {

    "startUrls": [
        {
            "url": "https://www.reddit.com/r/LUMS/"
        }
    ],
    "debugMode": False,
    "includeNSFW": True,
    "maxComments": 100,
    "maxCommunitiesCount": 1,
    "maxItems": 100,
    "maxPostCount": 100,
    "maxUserCount": 200,
    "proxy": {
        "useApifyProxy": True,
        "apifyProxyGroups": ["RESIDENTIAL"],
    },
    "scrollTimeout": 40,
    "searchComments": True,
    "searchCommunities": False,
    "searchPosts": True,
    "searchUsers": False,
    "searches": [
        
        "cafe",
        "food"
        
    ],
    "skipComments": False,
    "skipUserPosts": False,
    "sort": "top",
    "time": "all"
}

# Run the Actor and wait for it to finish
run = client.actor("FgJtjDwJCLhRH9saM").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
