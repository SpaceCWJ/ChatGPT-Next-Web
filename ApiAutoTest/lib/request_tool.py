import requests


class RequestsTool:
    @classmethod
    def do_request(cls, method, url, headers=None, params=None, json=None, data=None):
        if method == 'get':
            res = requests.get(url=url, params=params, headers=headers, verify=False)
            return res
        elif method == 'post':
            res = requests.post(url=url, json=json, data=data, headers=headers, verify=False)
            return res
        elif method == 'put':
            res = requests.post(url=url, json=json, data=data, headers=headers, verify=False)
            return res
        elif method == 'delete':
            res = requests.post(url=url, json=json, data=data, headers=headers, verify=False)
            return res
