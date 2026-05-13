name: Daily News Bot

on:
  schedule:
    - cron: '0 22 * * *' # 한국 시간 아침 7시
  workflow_dispatch: # 직접 실행 버튼

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: 코드 가져오기
        uses: actions/checkout@v4 # v3가 아니라 v4입니다!

      - name: 파이썬 설치
        uses: actions/setup-python@v5 # v4가 아니라 v5입니다!
        with:
          python-version: '3.10'

      - name: 필요한 도구 설치
        run: pip install requests

      - name: 프로그램 실행
        env:
          NAVER_ID: ${{ secrets.NAVER_ID }}
          NAVER_SECRET: ${{ secrets.NAVER_SECRET }}
          TELEGRAM_TOKEN: ${{ secrets.TELEGRAM_TOKEN }}
          CHAT_ID: ${{ secrets.CHAT_ID }}
          # 2026년 환경에 맞춘 최신 설정
          FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
        run: python main.py
