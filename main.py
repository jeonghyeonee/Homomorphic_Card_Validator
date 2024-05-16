from heaan_utils import Heaan

# Heaan 클래스의 인스턴스 생성
heaan_instance = Heaan()

# Heaan 클래스의 메서드 호출
heaan_instance.initialize()

def preprocess_card_number(card_info):
    card_number = [int(num) for i in range(1, 5) for num in card_info[f'card_number_{i}']]
    card_num_ctxt = heaan_instance.preprocess_card_number(card_number)
    return card_num_ctxt

def preprocess_expiry_date(card_info):
    expiry_month = int(card_info['expiry_month'])
    expiry_year = int(card_info['expiry_year'])
    valid_thru = expiry_year * 100 + expiry_month
    return valid_thru