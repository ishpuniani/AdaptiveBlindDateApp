
import requests
import pandas as pd
import argparse
try:
    # For Python 3.0 and later
    from urllib.parse import quote
except ImportError:
    # Fall back to Python 2's urllib2 and urllib
    from urllib import quote

API_KEY='ygOEqxS2_khcc99_ODjisNpQqAX5JB3pzedPJEJy8UZwdWk7sigevmP8PR_IkbUACZGwX-epxH548ZCWE7VA7p_mbuvlnjD2HFhu2Y4oY8pXeZ06fgC4f6mVmxmnXXYx'


# API constants
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
DEFAULT_LOCATION = 'Dublin'

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--location', dest='location',default=DEFAULT_LOCATION, type=str,help='Search location (default: %(default)s)')
input_values = parser.parse_args()

person = dict()
person['Id']=[]
person['Category']=[]
person['Name']=[]
person['Phone']=[]
person['Imageurl']=[]
person['Address']=[]
person['Latitude']=[]
person['Longitude']=[]
person['Rating']=[]



categories=['escapegames','diyfood','shoppingcenters','bikerentals','bowling','fishing','yoga','museums','tea','golf','hiking','amusementparks','climbing','gokarts','horsebackriding','diners','aquariums','beaches','arcades','movietheaters','lakes','mini_golf','sailing','galleries']

def request(host, path, url_params=None):
    headers = {'Authorization': 'Bearer %s' % API_KEY,}
    url_params = url_params or {}
    url1=API_HOST+SEARCH_PATH
    url = url1.format(API_HOST, quote(SEARCH_PATH.encode('utf8')))
    r=requests.request('GET', url, headers=headers, params=url_params)

    return r.json()


def searchOpenness():
    count=0
    for l in range(len(categories)):
        url_params = {
                'categories':categories[l],
                'location':input_values.location,
        }
        dictOpenness = request(API_HOST, SEARCH_PATH, url_params=url_params)
        dict2 = dictOpenness.get('businesses')
        dict3=[]
    
        for i in range(len(dict2)):
            dict3.append(dict2[i]['rating'])
            dict3.sort(reverse=True)
        for i in range(len(dict3)):
            for j in range(len(dict2)):
                if dict2[j]['rating']==dict3[i] and dict2[j]['name'] not in person['Name']:
                    dictCategory = dict2[j].get('categories')
                    for k in range(len(dictCategory)):
                        if dict2[j]['categories'][k]['title'] not in person['Category'] and dict2[j]['categories'][k]['alias'] in categories:
                            person['Id'].append(count+1)
                            person['Category'].append(dict2[j]['categories'][k]['title'])
                            person['Name'].append(dict2[j]['name'])
                            person['Phone'].append(dict2[j]['display_phone'])
                            person['Imageurl'].append(dict2[j]['image_url'])
                            person['Address'].append(dict2[j]['location']['display_address'])
                            person['Latitude'].append(dict2[j]['coordinates']['latitude'])
                            person['Longitude'].append(dict2[j]['coordinates']['longitude'])
                            person['Rating'].append(dict2[j]['rating'])
                            count+=1
                        
def main():
    searchOpenness()
    pd.DataFrame.from_dict(data=person).to_csv('Activities.csv', header=True,index=False)

if __name__ == '__main__':
    main()
