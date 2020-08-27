#importing libraries 
import urllib.request, json

#u_name gets the username whose profile picture to be downloaded
u_name = input('Enter the username to download the instagram profile\n')

#link provides user profile page data in json
link = 'https://www.instagram.com/' + u_name + '/?__a=1'

#when user exists
try:
    with urllib.request.urlopen(link) as url:
        data = json.loads(url.read().decode())
        img_url = data['graphql']['user']['profile_pic_url_hd']
    #saves profile picture in the same directory
    urllib.request.urlretrieve(img_url, u_name + '_insta_dp.jpg')
    print('insta dp downloaded successfully...')

#when user does not exist
except urllib.error.HTTPError:
    print('user does not exist')
