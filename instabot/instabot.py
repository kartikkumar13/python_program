from instapy import InstaPy
from instapy import smart_run
import json


f = open("password.txt")
password = json.load(f)
insta_username = password['username']  # instagram user name
insta_password = password['password']  # instagram password

session = InstaPy(username=insta_username,
                  password=insta_password, headless_browser=True)

with smart_run(session):
    # setting 50% user will be followed
    session.set_do_follow(True, percentage=50)

    # setting 100% for post comment
    session.set_do_comment(True, percentage=100)

    # what will be comment in post
    session.set_comments(["hey @{} Nice"])

    session.set_quota_supervisor(enabled=True, peak_comments_daily=150, peak_comments_hourly=15, peak_follows_hourly=10, peak_follows_daily=100,
                                 peak_likes_daily=300, peak_likes_hourly=30, sleep_after=['likes', 'follows'])

    session.set_relationship_bounds(
        enabled=True, delimit_by_numbers=True, min_followers=30)

    session.like_by_tags(['trending', 'new'], amount=300)


session.end()
