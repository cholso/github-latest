import sys
import json
<<<<<<< HEAD
import requests

# Use python github-latest.py cholso

# Print out the timestamp of the first 'event' 
if __name__=="__main__":
    username = sys.argv[1]

    response = requests.get(f"https://api.github.com/users/{username}/events")
    events = json.loads(response.content)

    print(events[0]['created_at'])
=======

import requests

# Use Like python githubber.py JASchilz
# (or another user name)

if __name__ == "__main__":
    username = sys.argv[1]

    # TODO:
    #
    # 1. Retrieve a list of "events" associated with the given user name
    # 2. Print out the time stamp associated with the first event in that list.

    print("COMPLETE THE TODOs")
    

>>>>>>> 183fd2c5b5f12173edeb4c0aa04e52ecbfacc4cc

