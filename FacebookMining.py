
import json

import facebook


#we can generate the token by creating a app in developers.facebook.com
token = "-------------------------"
graph = facebook.GraphAPI(token)
#fields = ['first_name', 'location{location}','email','link']
profile = graph.get_object('me',fields='first_name, location, link,email')
#return desired fields
print(profile)
    
 


# In[14]:



import facebook
import json
import requests


token = "------------------------------------------"
graph = facebook.GraphAPI(access_token=token,version="7.0")
post = graph.get_object(id="100772680085702")
print(post)


friends = graph.get_connections("me", "friends")
print(friends)

# Search for places near 1 Hacker Way in Menlo Park, California.
places = graph.search(type='place',
                      center='37.4845306,50.1498183',
                      fields='name,location')

# Each given id maps to an object the contains the requested fields.
for place in places['data']:
    print('%s %s' % (place['name'].encode(),place['location'].get('zip')))

    
    # Get the active user's friends.
#friends = graph.get_connections(id='me', connection_name='location,friends')
#print(friends)



# Write a comment on a post.
 #graph.put_object(parent_object='100772680085702', connection_name='comments',message='Nice!')
#graph.put_comment(object_id='100772680085702', message='Nice...')


# In[ ]:





# In[10]:


import os
import json
import facebook

if __name__ == '__main__':
    token = "-----bftHLOqHMZB1suaihodUGNZA2QlzMVXm4U2dgAV95nuhVuiiMq7gZDZD"
    graph = facebook.GraphAPI(token)
    profile = graph.get_object("me",fields='name,location{location}')
    print(profile)


# In[7]:


import os
import json
import facebook

if __name__ == '__main__':
    token = "-----------ZBVMXihPLWdQZACDfHBU2hXevJO1OVlQqFMNUr90CDwIiezzkNvta7ttvd1suaihodUGNZA2QlzMVXm4U2dgAV95nuhVuiiMq7gZDZD"
    graph = facebook.GraphAPI(token)
    user = graph.get_object("me")
    friends = graph.get_connections(user["id"],"friends")
    print(friends)


# In[5]:


import os
import json
import facebook
import requests

if __name__ == '__main__':
    token = "------------6QZAuVsmr25ZAXILSvixZCxBkGNRhIMdcSoBaVDmaTOYcuQ5JKfYjLyWBkxcKsN51LQaBm6wbftHLOqHMZBZBVMXihPLWdQZACDfHBU2hXevJO1OVlQqFMNUr90CDwIiezzkNvta7ttvd1suaihodUGNZA2QlzMVXm4U2dgAV95nuhVuiiMq7gZDZD"
    graph = facebook.GraphAPI(token)
    posts = graph.get_connections("me","posts")
    #print(friends)
    
    while True: #keep Paginating
        try:
            with open('my_posts.json1','a') as f:
                for post in posts['data']:
                    print(post)
                    f.write(json.dumps(post)+"\n")
                    #get next page
                    posts = requests.get(posts['paging']['next']).json()
        except KeyError:
            #no more pages, break the loop
            break


# In[6]:


import os
import json
import facebook
import requests

if __name__ == '__main__':
    token = "-----------------------6QZAuVsmr25ZAXILSvixZCxBkGNRhIMdcSoBaVDmaTOYcuQ5JKfYjLyWBkxcKsN51LQaBm6wbftHLOqHMZBZBVMXihPLWdQZACDfHBU2hXevJO1OVlQqFMNUr90CDwIiezzkNvta7ttvd1suaihodUGNZA2QlzMVXm4U2dgAV95nuhVuiiMq7gZDZD"
    graph = facebook.GraphAPI(token)
    all_fields =[
        'message',
        'created_time',
        'description',
        'caption',
        'link',
        'place',
        'status_type'
    ]
    all_fields = ','.join(all_fields)
    posts = graph.get_connections('me','posts', fields=all_fields)
    
    while True: #keep Paginating
        try:
            with open('my_posts2.json1','a') as f:
                for post in posts['data']:
                    print(post)
                    f.write(json.dumps(post)+"\n")
                    #get next page
                    posts = requests.get(posts['paging']['next']).json()
        except KeyError:
            #no more pages, break the loop
            break


# In[ ]:




