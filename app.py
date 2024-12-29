from flask import Flask, request, jsonify
from aliyun_face_recognition import detect_face, compare_faces
from database import init_db, register_user, get_all_users

app = Flask(__name__)

# 初始化数据库
init_db()

@app.route('/register', methods=['POST'])
def register():
    """用户注册接口"""
    user_id = request.form['user_id']
    file = request.files['file']
    image_path = f'uploads/{user_id}.jpg'
    file.save(image_path)

    # 检测人脸
    face_data = detect_face(image_path)
    if not face_data:
        return jsonify({"message": "未检测到人脸"}), 400

    # 保存用户信息到数据库
    register_user(user_id, image_path)
    return jsonify({"message": f"用户 {user_id} 注册成功"})

@app.route('/recognize', methods=['POST'])
def recognize():
    """人脸识别接口"""
    file = request.files['file']
    image_path = 'uploads/temp.jpg'
    file.save(image_path)

    # 获取所有用户并逐一比较
    users = get_all_users()
    best_match = None
    best_score = float('inf')

    for user_id, user_image_path in users:
        response = compare_faces(image_path, user_image_path)
        score = response.get('Data', {}).get('Confidence', 0)
        if score > best_score:
            best_score = score
            best_match = user_id

    if best_match:
        return jsonify({"message": f"匹配用户: {best_match}, 相似度: {best_score}"})
    else:
        return jsonify({"message": "未找到匹配用户"}), 404

if __name__ == "__main__":
    app.run(debug=True)
