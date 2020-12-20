#author: rebeka zhang
#time:2020-12-05
#-*- coding=utf-8 -*-
import pytest

# def test_001():
#     #断言
#     assert 1 + 2 == 3
#
# def test_002():
#     assert 1+ 2 == 0
#
# #封装测试类
# class Test_login:
#     def test_003(self):
#         assert 1+2 == 4

# @pytest.mark.parametrize('inData,a',[(10,20),(30,40)])
# def test_001(inData,a):
#     #断言
#     print('--------test_001----开始')
#     assert inData + a == 3
#     print('--------test_001----结束')
import requests
#获取用户token
tokenData = [{"userName":"J201903070064","password":"362387359"},{"userName":"J201903070064","password":"36238735900"}]
@pytest.mark.parametrize('inData',tokenData)
def test_get_token(inData):
    url = "http://47.96.181.17:9090/rest/toController"

    payload = inData
    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, json=payload)

    # print(response.text.encode('utf8'))
    # print(response.json()['token'])

    # token = response.json()['token']
    assert response.json()['msg'] == '成功'

# if __name__ == "__main__":
#      pytest.main(['test_func.py','-s','-html=F:\\00测试开发课件\\11期\\20200914\\HogwartsSDET11-master\\hogwarts\\songqin\\report\\xt.html']) #-s 输出打印信息
#      #接口参数化