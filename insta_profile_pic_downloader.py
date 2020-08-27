import urllib.request, json

u_name = input('Enter the username to download the instagram profile\n')
link = 'https://www.instagram.com/' + u_name + '/?__a=1'

try:
    with urllib.request.urlopen(link) as url:
        data = json.loads(url.read().decode())
        img_url = data['graphql']['user']['profile_pic_url_hd']
    urllib.request.urlretrieve(img_url, u_name + '_insta_dp.jpg')
    print('insta dp downloaded successfully...')
except urllib.error.HTTPError:
    print('user does not exist')


'''#Used to make requests
import urllib.request

x = urllib.request.urlopen('https://www.google.com/')
print(x.read())
'''
