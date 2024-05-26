from flask import Flask, render_template, jsonify, request, redirect, url_for
import subprocess
import json

app = Flask(__name__)

# 전역 변수를 초기화합니다.
card_info = {}
validation_result = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
    global card_info, validation_result
    card_info = {
        "card_number_1": request.form['card_number_1'],
        "card_number_2": request.form['card_number_2'],
        "card_number_3": request.form['card_number_3'],
        "card_number_4": request.form['card_number_4'],
        "expiry_month": request.form['expiry_month'],
        "expiry_year": request.form['expiry_year']
    }
    print("카드 정보를 성공적으로 받았습니다.")
    
    # card_info를 JSON 문자열로 변환합니다.
    card_info_json = json.dumps(card_info)
    
    # subprocess를 사용하여 main.py를 실행하고 결과 값을 받습니다.
    result = subprocess.check_output(["python", "main.py", card_info_json])
    
    # 결과 값을 validation_result에 저장합니다.
    validation_result = json.loads(result.decode("utf-8").strip())
    
    print("validation result: ", validation_result)
    
    # 리디렉션 없이 현재 페이지에 머물기 위해 index.html을 다시 렌더링합니다.
    return render_template('result.html', validation_result=validation_result)

@app.route('/card-info', methods=['GET'])
def get_card_info():
    global card_info
    return jsonify(card_info)

@app.route('/result')
def result():
    global validation_result
    return render_template('result.html', validation_result=validation_result)

if __name__ == '__main__':
    app.run(debug=True)