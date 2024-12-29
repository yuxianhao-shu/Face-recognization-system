
from aliyunsdkcore.client import AcsClient
from aliyunsdkfacebody.request.v20191230.CompareFaceRequest import CompareFaceRequest
from aliyunsdkfacebody.request.v20191230.DetectFaceRequest import DetectFaceRequest
import base64

# 配置阿里云账号信息
client = AcsClient('<YourAccessKeyId>', '<YourAccessKeySecret>', 'cn-hangzhou')

def encode_image(image_path):
    """将图片转换为 Base64 编码"""
    with open(image_path, 'rb') as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

def detect_face(image_path):
    """检测人脸"""
    image_base64 = encode_image(image_path)
    request = DetectFaceRequest()
    request.set_ImageData(image_base64)
    request.set_MaxFaceNum(1)  # 只检测一张人脸
    response = client.do_action_with_exception(request)
    return response

def compare_faces(image_path_1, image_path_2):
    """比较两张人脸的相似度"""
    image1_base64 = encode_image(image_path_1)
    image2_base64 = encode_image(image_path_2)
    request = CompareFaceRequest()
    request.set_ImageDataA(image1_base64)
    request.set_ImageDataB(image2_base64)
    response = client.do_action_with_exception(request)
    return response
