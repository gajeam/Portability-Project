ABOUT__FACE_RECOGNITION = "about_you/face_recognition.json"
ABOUT__FRIEND_PEER_GROUP = "about_you/friend_peer_group.json"
ABOUT__ADDRESS_BOOK = "about_you/your_address_books.json"

ADS__INTERESTS = "ads/ads_interests.json"
ADS__UPLOADED_CONTACT_LIST = "ads/advertisers_who_uploaded_a_contact_list_with_your_information.json"
ADS__INTERACTED_WITH = "ads/advertisers_you've_interacted_with.json"

APPS_AND_WEBSITES = 'apps_and_websites/apps_and_websites.json'

COMMENTS = 'comments/comments.json'

EVENTS__EVENT_INVITATIONS = 'events/event_invitations.json'
EVENTS__YOUR_EVENT_RESPONSES = 'events/your_event_responses.json'
EVENTS__YOUR_EVENTS = 'events/your_events.json'

FOLLOWS__FOLLOWED_PAGES = 'following_and_followers/followed_pages.json'
FOLLOWS__FOLLOWING = 'following_and_followers/following.json'
FOLLOWS__UNFOLLOWED_PAGES = 'following_and_followers/unfollowed_pages.json'

FRIENDS__FRIENDS = 'friends/friends.json'
FRIENDS__REJECTED_REQUESTS = 'friends/rejected_friend_requests.json'
FRIENDS__REMOVED = 'friends/removed_friends.json'
FRIENDS__SENT_REQUESTS = 'friends/sent_friend_requests.json'

GROUPS__MEMBERSHIP_ACTIVITY = 'groups/your_group_membership_activity.json'
GROUPS__ADMIN = 'groups/your_groups.json'
GROUPS__POSTS_AND_COMMENTS = 'groups/your_posts_and_comments_in_groups.json'

LIKES_AND_REACTIONS__PAGES = 'likes_and_reactions/pages.json'
LIKES_AND_REACTIONS__POSTS_AND_COMMENTS = 'likes_and_reactions/posts_and_comments.json'

# NOTE: This is missing location data

MARKETPLACE__ITEMS_BOUGHT = 'marketplace/items_bought.json'
MARKETPLACE__ITEMS_SOLD = 'marketplace/items_sold.json'

# NOTE: This is missing messaging data

# NOTE: This is missing one folder called `other_activity`.
# It contains pokes and other miscellanea
# NOTE: There is more data for peopel who run pages

PAYMENT_HISTORY = 'payment_history/payment_history.json'

# NOTE: There are also photo and videos 

POSTS__OTHERS_PEOPLES_POSTS_TO_YOUR_TIMELINE = "posts/other_people's_posts_to_your_timeline.json"
POSTS__YOUR_POSTS = 'posts/your_posts.json'


PROFILE__PROFILE_INFO = 'profile_information/profile_information.json'
PROFILE__UPDATE_HISTORY = 'profile_information/profile_update_history.json'

SAVED_ITEMS_AND_COLLECTIONS = 'saved_items_and_collections/saved_items_and_collections.json'

SEARCH_HISTORY = 'search_history/your_search_history.json'

# NOTE: There are some security login ones I didn't get around to doing

all_files = [
		ABOUT__ADDRESS_BOOK,
		ADS__INTERESTS,
		ADS__UPLOADED_CONTACT_LIST,
		ADS__INTERACTED_WITH,
		APPS_AND_WEBSITES,
		COMMENTS,
		EVENTS__EVENT_INVITATIONS,
		EVENTS__YOUR_EVENT_RESPONSES,
		EVENTS__YOUR_EVENTS,
		FOLLOWS__FOLLOWED_PAGES ,
		FOLLOWS__FOLLOWING,
		FOLLOWS__UNFOLLOWED_PAGES,
		FRIENDS__FRIENDS,
		FRIENDS__REJECTED_REQUESTS,
		FRIENDS__REMOVED,
		FRIENDS__SENT_REQUESTS,
		GROUPS__MEMBERSHIP_ACTIVITY,
		GROUPS__ADMIN,
		GROUPS__POSTS_AND_COMMENTS,
		LIKES_AND_REACTIONS__PAGES,
		LIKES_AND_REACTIONS__POSTS_AND_COMMENTS,
		MARKETPLACE__ITEMS_BOUGHT,
		MARKETPLACE__ITEMS_SOLD,
		PAYMENT_HISTORY,
		POSTS__OTHERS_PEOPLES_POSTS_TO_YOUR_TIMELINE,
		POSTS__YOUR_POSTS ,
		PROFILE__PROFILE_INFO,
		PROFILE__UPDATE_HISTORY,
		SAVED_ITEMS_AND_COLLECTIONS,
		SEARCH_HISTORY
	]