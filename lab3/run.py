#!/usr/bin/python3

from ClientVK import ClientGetID
from ClientVK import ClientGetFriendsAges
from gist import Gist

debug = False
username = "alexdarkstalker98"

get_id = ClientGetID(username).execute()
friends_ages = ClientGetFriendsAges(get_id).execute()

if debug:
    print("ID: ", get_id)
    print("Ages: ", friends_ages)

print(Gist(friends_ages))
