import sys
import requests
import logging

logging.basicConfig(filename='/Users/bsadkhin/workspace/django/skystrata/skystrata/api/celery_home/log',level=logging.DEBUG)

#TODO ADD ARGPARSE
#TODO JWT ENCODE TOKEN
#TODO SWTICH TO ADMIN ACCOUNT WHEN UPDATING STATE WHICH MEANS A NEW SERIALIZER

def main():
    instance = sys.argv[1]
    token = sys.argv[2]
    url = "http://127.0.0.1:8000/api/v1/instances/" + instance + "/"
    startInstance(url,token)






def getInstanceInfo(url,token):
    response = requests.get(url=url, headers={'Authorization': 'Token {}'.format(token)})
    if response.status_code == 200:
        logging.info("Successful request")
    else:
        logging.error("Failure to get instance" + url + str(response.status_code))
        raise Exception
    try:
        return response.json()
    except:
        raise Exception("Couldn't decode json from response")



#TODO
def markInstanceLaunchFailure(url,token):
    pass


def startInstance(url,token):
    logging.debug("Begin Log")
    logging.info("Token:" + token)
    logging.info("URL:" + url)
    response = getInstanceInfo(url,token)
    logging.info(response)



if __name__ == '__main__':
    main()
