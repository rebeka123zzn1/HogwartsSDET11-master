#!/usr/bin/python3
#coding:utf-8

"""
desc: 调用腾讯OCRapi实现文本识别
#@Readme : 请控制在1M内，支持JPG、PNG、BMP格式
"""

import base64, hashlib, json, random, string, time
from urllib import parse, request


def GetAccessToken(formdata, app_key):
    '''
    获取签名
    :param formdata:请求参数键值对
    :param app_key:应用秘钥
    :return:返回接口调用签名
    '''
    dic = sorted(formdata.items(), key=lambda d: d[0])
    sign = parse.urlencode(dic) + '&app_key=' + app_key
    m = hashlib.md5()
    m.update(sign.encode('utf8'))
    return m.hexdigest().upper()

# 改成你自己的API账号、密码-可用改为全局变量
app_id = '2160574077'
app_key = 'fswbDM7NmcZKP9zB'
def RecogniseGeneral(app_id, time_stamp, nonce_str, image, app_key):
    '''
    腾讯OCR通用接口
    :param app_id:应用标识，正整数
    :param time_stamp:请求时间戳（单位秒），正整数
    :param nonce_str: 随机字符串，非空且长度上限32字节
    :param image:原始图片的base64编码
    :return:
    '''
    host = 'https://api.ai.qq.com/fcgi-bin/ocr/ocr_generalocr'
    formdata = {'app_id': app_id, 'time_stamp': time_stamp, 'nonce_str': nonce_str, 'image': image}
    app_key = app_key
    sign = GetAccessToken(formdata=formdata, app_key=app_key)
    formdata['sign'] = sign
    req = request.Request(method='POST', url=host, data=parse.urlencode(formdata).encode('utf8'))
    response = request.urlopen(req)
    if (response.status == 200):
        json_str = response.read().decode()
        #print('腾讯OCR通用接口返回结果：',json_str)
        jobj = json.loads(json_str)
        datas = jobj['data']['item_list']
        recognise = {}
        for obj in datas:
            recognise[obj['itemstring']] = obj
        return recognise


def Recognise(img_path):
    with open(file=img_path, mode='rb') as file:
        base64_data = base64.b64encode(file.read())
        base64_data = str(base64_data, 'utf-8')
    nonce = ''.join(random.sample(string.digits + string.ascii_letters, 32))
    stamp = int(time.time())
    recognise = RecogniseGeneral(app_id=app_id, time_stamp=stamp, nonce_str=nonce, image=base64_data,
                                 app_key=app_key)  # 替换成自己的app_id,app_key
    # 提取出来看
    for k, v in recognise.items():
        print('腾讯OCR通用接口返回结果：',k, v)

    return recognise

# 腾讯优图的API比较复杂的就是生成签名

if __name__ == '__main__':
    img_path = r'F:\local_git\image\yan1.jpg'
    recognise_dic = Recognise(img_path)
    for k, value in recognise_dic.items():
        print('图片识别内容：',k)
        for v in value['itemcoord']:
            print('内容坐标：',v)