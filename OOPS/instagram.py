"""
Create a class named InstagramProfile that represents a user's Instagram profile.

Properties (Attributes):
name (string)
username (string)
age (int)
followers (int)
profile_picture (string - can just be a text URL or file name)

Behaviors (Functions):
post_video() → prints "Posted a video!"
post_picture() → prints "Posted a picture!"
like() → prints "Liked a post!"
comment() → prints "Commented on a post!"
add_story() → prints "Added a new story!"
"""

class InstagramProfile:
    name=""
    username=""
    age = 0
    followers = 0
    profile_pic = ""
    
    def __init__(self, name, username, age, followers, profile_pic):
        self.name = name
        self.username = username
        self.age = age
        self.followers = followers
        self.profile_pic = profile_pic
    def post_video():
        print("Posted a video!")
    def post_picture():
        print("Posted a picture!")
    def like():
        print("Liked a post!")
    def comment():
        print("Commented on a post")
    def add_story():
        print("Added a new story!")

#driver code
Aarav = InstagramProfile("Aarav", "av", "16", "1200", "yes")
print(Aarav.name)
print(Aarav.username)
Aarav.comment()
Aarush = InstagramProfile("Aarush", "arv", "16", "600", "yes")
print(Aarush.name)
print(Aarush.username)
Aarush.add_story()