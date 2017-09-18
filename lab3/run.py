#!/usr/bin/python3

from ClientVK import ClientGetID
from ClientVK import ClientGetFriendsAges
from gist import Gist

debug = True
username = "alexdarkstalker98"

get_id = ClientGetID(username).execute()
friends_ages = ClientGetFriendsAges(get_id).execute()

if debug:
    print("ID: ", get_id)
    print("Ages: ", friends_ages)

mygist = Gist(friends_ages)
print(mygist)
title = "Ages of Users "
title_x = "Ages"
title_y = "Users"
mygist.showHist(title,title_x,title_y)
mygist.showBar(title,title_x,title_y )
