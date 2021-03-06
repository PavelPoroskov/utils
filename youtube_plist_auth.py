## START BOILERPLATE CODE

# Sample Python code for user authorization

import httplib2
import os
import sys

import pprint
from datetime import datetime

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
CLIENT_SECRETS_FILE = "client_secrets.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
YOUTUBE_READ_WRITE_SSL_SCOPE = "https://www.googleapis.com/auth/youtube.force-ssl"
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"

# This variable defines a message to display if the CLIENT_SECRETS_FILE is
# missing.
MISSING_CLIENT_SECRETS_MESSAGE = "WARNING: Please configure OAuth 2.0" 

# Authorize the request and store authorization credentials.
def get_authenticated_service(args):
  flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE, scope=YOUTUBE_READ_WRITE_SSL_SCOPE,
    message=MISSING_CLIENT_SECRETS_MESSAGE)

  storage = Storage("youtube-api-snippets-oauth2.json")
  credentials = storage.get()

  if credentials is None or credentials.invalid:
    credentials = run_flow(flow, storage, args)

  # Trusted testers can download this discovery document from the developers page
  # and it should be in the same directory with the code.
  return build(API_SERVICE_NAME, API_VERSION,
      http=credentials.authorize(httplib2.Http()))


#args = argparser.parse_args()
args = argparser.parse_args(sys.argv[2:])
service = get_authenticated_service(args)

def print_results(results):
   print(results)

#  pp = pprint.PrettyPrinter()
#  pp.pprint(results)

#   print(type(results))

   for i in results["items"]:
     s = i["snippet"]

     date_string = s["publishedAt"]

#     date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S %z" )
#     date = datetime.strptime(date_string, "%Y%m%dT%H%M%S.%fZ" )
     date = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%fZ" )
                                            
#                                            "%Y-%m-%dT%H:%M:%S.%f%z"
#     date = datetime.strptime(date_string)
#     datetime.
     title = s["title"]
     nItems = i["contentDetails"]["itemCount"]

     print( date.year, title, nItems )


# Build a resource based on a list of properties given as key-value pairs.
# Leave properties with empty values out of the inserted resource.
def build_resource(properties):
  resource = {}
  for p in properties:
    # Given a key like "snippet.title", split into "snippet" and "title", where
    # "snippet" will be an object and "title" will be a property in that object.
    prop_array = p.split('.')
    ref = resource
    for pa in range(0, len(prop_array)):
      is_array = False
      key = prop_array[pa]
      # Convert a name like "snippet.tags[]" to snippet.tags, but handle
      # the value as an array.
      if key[-2:] == '[]':
        key = key[0:len(key)-2:]
        is_array = True
      if pa == (len(prop_array) - 1):
        # Leave properties without values out of inserted resource.
        if properties[p]:
          if is_array:
            ref[key] = properties[p].split(',')
          else:
            ref[key] = properties[p]
      elif key not in ref:
        # For example, the property is "snippet.title", but the resource does
        # not yet have a "snippet" object. Create the snippet object here.
        # Setting "ref = ref[key]" means that in the next time through the
        # "for pa in range ..." loop, we will be setting a property in the
        # resource's "snippet" object.
        ref[key] = {}
        ref = ref[key]
      else:
        # For example, the property is "snippet.description", and the resource
        # already has a "snippet" object.
        ref = ref[key]
  return resource

# Remove keyword arguments that are not set
def remove_empty_kwargs(**kwargs):
  good_kwargs = {}
  if kwargs is not None:
    for key, value in kwargs.iteritems():
      if value:
        good_kwargs[key] = value
  return good_kwargs

### END BOILERPLATE CODE

# Sample python code for playlists.list

def addResults( bigList, results):

   for i in results["items"]:
     s = i["snippet"]

     date_string = s["publishedAt"]
     date = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%fZ" )
     title = s["title"]
     nItems = i["contentDetails"]["itemCount"]
     

#     print( date.year, title, nItems )
     bigList.append({
      'date': date.year,
      'title': title,
      'itemCount':nItems,
      'channelTitle': s["channelTitle"]
      })


def playlists_list_by_channel_id(service, **kwargs):
  kwargs = remove_empty_kwargs(**kwargs) # See full sample for function

  # results = service.playlists().list(
  #   **kwargs
  # ).execute()

  # print_results(results)

  bigList = []

  playlists = service.playlists()
  request = playlists.list(**kwargs)

  while not (request is None):
    results = request.execute()

#    print_results(results)
    addResults( bigList, results )

    request = playlists.list_next(request, results)

  bigList.sort(key=lambda item: (item["title"], item["date"]) )

  for item in bigList:
    # s = "" + str(item["date"]) + "; " + item["title"] + "; " + str(item["itemCount"])
    # s = s + "; " + str(item["channelTitle"])
    s = u'' + unicode(item["date"]) + u'; ' + item["title"] + u'; ' + unicode(item["itemCount"])
    s = s + u'; ' + item["channelTitle"]
    s = s.encode('utf-8')
    print( s )



# playlists_list_by_channel_id(service,
#     part='snippet,contentDetails',
#     channelId='UCENeeLCbbDNAP-664-t26FA',
#     maxResults=25)
  
playlists_list_by_channel_id(service,
    part='snippet,contentDetails',
    channelId=sys.argv[1],
    maxResults=25)


