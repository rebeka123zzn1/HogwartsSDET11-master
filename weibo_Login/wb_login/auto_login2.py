#pip install tencentcloud-sdk-python

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ocr.v20181119 import ocr_client, models
import base64
import json
SecretId='xxxxxxxx'#自己去腾讯云上看，需要实名认证
SecretKey='xxxxxxxxxx'
def get_json(path):
    try:
        cred = credential.Credential(SecretId, SecretKey) #密钥
        httpProfile = HttpProfile()
        httpProfile.endpoint = "ocr.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = ocr_client.OcrClient(cred, "ap-shanghai", clientProfile)

        req = models.GeneralAccurateOCRRequest()#这个通用还是高精度自己看着来
        #对本地图片进行base64转码【本地图片解析需要先转成base64编码】
        with open(path, 'rb') as f:
            # base64_data = base64.b64encode(f.read())
            # s = base64_data.decode()
            # ImageBase64_value = 'data:image/jpeg;base64,%s'%s
            # #params是字符串，以下进行拼接
            # params = '{"ImageBase64":"' + ImageBase64_value + '"}' #以图片Base64编码发送请求

            base64data = base64.b64encode(f.read())  # 得到 byte 编码的数据
            base64data = str(base64data, 'utf-8')  # 重新编码数据
            params = '{"ImageBase64":"' + base64data + '"}'

        req.from_json_string(params)
        resp = client.GeneralAccurateOCR(req)#GeneralAccurateOCR#GeneralBasicOCR#高精度和通用
        # A=resp.TextDetections
        # for line in A:
        #     print(line.DetectedText)
        # resp = resp.to_json_string()
        return resp
    except TencentCloudSDKException as err:
        print(err)



if __name__ == '__main__':
    import glob
    import os
    path_pic=r'F:\00测试开发课件\11期\20200914\HogwartsSDET11-master\weibo_Login\wb_login\image\yan1.jpg'
    path_save='tengxun_OCR_23'
    if not os.path.exists(path_save):
        os.mkdir(path_save)
    extensions=['jpg', 'JPG', 'jpeg', 'JPEG']
    for extension in extensions:
        for path in glob.glob(os.path.join(path_pic, '*.'+extension)):
            path_txt = path_save + '/' + path.split('/')[-1].split('.')[0] + '.txt'
            resp = get_json(path)
            results = resp.TextDetections
            print(results)
            with open(path_txt,'w') as file:
                for line in results:
                    file.write(line.DetectedText)
                    file.write('\n')