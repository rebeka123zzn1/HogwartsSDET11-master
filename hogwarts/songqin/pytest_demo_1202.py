import requests

from random import randint

import pprint
import json

#获取用户token
def get_token():
    url = "http://47.96.181.17:9090/rest/toController"

    payload = "{\"userName\":\"J201903070064\",\"password\":\"362387359\"}"
    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    # print(response.text.encode('utf8'))
    # print(response.json()['token'])

    token = response.json()['token']
    return token

#新增用户
def new_user(token, inbodyData):
    url = "http://47.96.181.17:9090/rest/ac01CrmController"

    #payload = {"aac003": "张三", "aac004": "1", "aac011": "21", "aac030": f"135{randint(11111111,99999999)}", "aac01u": "88002255", "crm003": "1", "crm004": "1", "crm00a": "2018-11-11", "crm00b": "aaaaaa", "crm00c": "2019-02-28", "crm00d": "bbbbbb" }
    bodyData = json.loads(inbodyData)
    bodyData['aac030'] =f"135{randint(11111111,99999999)}"
    payload = bodyData

    headers = {
        'X-AUTH-TOKEN': token,
        'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, json=payload)

    # print(response.text.encode('utf8'))
    return response.json()
    # print(response.json()['token'])

    #token = response.json()['token']
    #
# if __name__=='__main__':
#     token =get_token()
#     reps = new_user(token)
# # print(reps.request.headers)
#     pprint.pprint(reps.json())
#
#     if reps.json()['message'] == '成功':
#         print(f'-----接口成功,总共耗时{reps.elapsed.total_seconds()}s---')
#     else:
#         print(f'-----接口失败,总共耗时{reps.elapsed.total_seconds()}s---')

    # todo: 后续优化：1. 封装，2， 结合excel 测试用例，yaml 用例，3，结合pytest框架，4，导出allure报告，5，优化报告，6-调试，7，Jenkins, 8-邮件通知

#断言--判断该请求是否成功 assert 到时候用框架来用
#打印json



