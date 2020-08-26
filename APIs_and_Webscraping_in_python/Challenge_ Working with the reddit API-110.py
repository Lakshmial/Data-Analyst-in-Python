## 2. Authenticating with the API ##

#Retrieve the /r/python subreddit's top posts for the past day

headers={"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
#To retrieve only the top posts for the past day, pass in a query parameter t (for "time") and set its value to the string day.
params={"t":"day"}
response = requests.get("https://oauth.reddit.com/r/python/top",headers=headers,params=params)
#Use the json method on the response to get the JSON response data.
python_top=response.json()

## 3. Getting the Most Upvoted Post ##

python_top_articles=python_top["data"]["children"]
most_upvoted=""
most_upvotes=0
for articles in python_top_articles:
    ar=articles['data']
    if ar['ups']>=most_upvotes:
        most_upvotes=ar['ups']
        most_upvoted=ar['id']

## 4. Getting Post Comments ##

response=requests.get("https://oauth.reddit.com/r/python/comments/4b7w9u",headers=headers)
comments=response.json()

## 5. Getting the Most Upvoted Comment ##

comments_list= comments[1]["data"]["children"]
most_upvoted_comment=''
most_upvotes_comment=0
for comments in comments_list:
    co=comments['data']
    if co['ups']>=most_upvotes_comment:
        most_upvotes_comment = co['ups']
        most_upvoted_comment = co['id']

## 6. Upvoting a Comment ##

payload={'dir':1,"id":'d16y4ry'}
response=requests.post("https://oauth.reddit.com/api/vote",json=payload,headers=headers)
status=response.status_code