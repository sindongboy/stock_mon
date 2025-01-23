import os
import requests
import datetime

api_key = os.environ.get('OPENAI_API_KEY')

def get_api_usage():
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    date = datetime.date(2025, 1, 21)  # 현재 날짜 사용
    url = f'https://api.openai.com/v1/usage?date={date.strftime("%Y-%m-%d")}'

    response = requests.get(url, headers=headers)
    usage_data = response.json()['data']

    # 사용량 데이터 처리
    for data in usage_data:
        print(f"Model: {data['model']}")
        print(f"Tokens used: {data['n_generated_tokens_total']}")


def main():
    get_api_usage()


if __name__ == '__main':
    main()

