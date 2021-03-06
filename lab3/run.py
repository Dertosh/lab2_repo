#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ClientVK import *
from gist import Gist

debug = False
username = "alexdarkstalker98"

get_id = ClientGetID(username).execute()
friends_ages = ClientGetFriendsAges(get_id).execute()

if debug:
    print("ID: ", get_id)
    print("Ages: ", friends_ages)

mygist = Gist(friends_ages)
mygist.printHist()
title = "Ages of Users "
title_x = "Ages"
title_y = "Users"
mygist.showHist(title,title_x,title_y)
#mygist.showBar(title,title_x,title_y )
