import os
import pytest
import requests
from requests.auth import HTTPBasicAuth
import json
import urllib
import urllib3
import logging



DEFAULT_REVERSE_PROXY_NAME="default"


''' Defaulting to the dev lab credentials '''
def applianceCredentials():
    _user = os.environ.get('ISAM_APPLIANCE_USER', 'admin')
    _password = os.environ.get('ISAM_APPLIANCE_PASSWORD', 'admin')
    return _user,_password


def reverseProxyUnderReview():
    rp=os.environ.get('ISAM_REVERSE_PROXY', DEFAULT_REVERSE_PROXY_NAME)
    return rp

def host_and_port():
    host_and_port = os.environ.get('ISAM_APPLIANCE_HOST_AND_PORT', 'localhost:9443')
    return host_and_port


def reqHeaders():
    _with_accept_headers = {'Content-type': 'application/json', 'Accept' : 'application/json'}
    return _with_accept_headers


def logResponse(response):
    print "HTTP status code " + str(response.status_code)
    print (json.dumps(response.json(), indent=4, sort_keys=True))

def getJunctions(reverseProxy): 
    url = 'https://{host_and_port}/wga/reverseproxy/{reverseproxy_id}/junctions'.format(reverseproxy_id=reverseProxy, host_and_port=host_and_port())
    headers = {'Content-type': 'application/json'}
    user, password = applianceCredentials()
    resp = requests.get(url, verify=False , auth=HTTPBasicAuth(user,password), headers=headers)
    if resp.status_code != 200:
        raise ApiError('LIST_JUNCTIONS_URL status code is  {}'.format(resp.status_code))
    return resp.json()

def asParams(junction_id):
    params = {'junctions_id': junction_id}
    return params


@pytest.fixture
def all_junction_data():
    return getJunctions(reverseProxyUnderReview()).items()



def test_junctions_to_backends_use_ssl(all_junction_data):
     user, password = applianceCredentials()
     for key, junctions in all_junction_data:
        for junction in junctions:
            url = 'https://{host_and_port}/wga/reverseproxy/{reverseproxy_id}/junctions'.format(reverseproxy_id=reverseProxyUnderReview(), host_and_port=host_and_port())
            response=requests.get(url, headers=reqHeaders(), verify=False , auth=HTTPBasicAuth(user, password), params=asParams(junction['id'])) 
            if response.status_code == 200:
                assert(response.json()['junction_type'] == 'SSL') 
            else:
                raise ApiError('Unable to find this junction some went wrong in the input to this function HTTP status is  {}'.format(resp.status_code))
     



def test_reverseproxy_has_http_off():
    user, password = applianceCredentials()
    url = 'https://{host_and_port}/wga/reverseproxy/{reverseproxy_id}/configuration/stanza/server/entry_name/http'.format(reverseproxy_id=reverseProxyUnderReview(), host_and_port=host_and_port())
    response=requests.get(url, headers=reqHeaders(), verify=False , auth=HTTPBasicAuth(user, password)) 
    if response.status_code == 200:
        for key, value in response.json().items():         
            assert(value[0]) == 'no'
    else:
        raise ApiError('Unable to find server stanza entry') 