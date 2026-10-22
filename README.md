# jiwongum-data

정부지원금 포털(blog9) "마감 임박 TOP 10" 위젯이 읽는 데이터 저장소입니다.

- `deadline.json`: 마감 임박 정부지원사업·지원금 목록 (지원금봇: 보조금24·기업마당 기준)
- 공개 주소: https://raw.githubusercontent.com/josephpark6449-bot/jiwongum-data/main/deadline.json
- 갱신: 예약 작업이 매주 월·목 오전 7시(KST)에 자동으로 갱신합니다.

## deadline.json 형식

```json
{
  "updated": "YYYY-MM-DD",
  "headline": "...",
  "disclaimer": "...",
  "items": [
    {"id": "", "name": "", "region": "", "agency": "", "category": "",
     "target": "", "apply_start": "YYYY-MM-DD", "apply_end": "YYYY-MM-DD",
     "summary": "", "url": "https://...", "source": "기업마당|보조금24"}
  ]
}
```

위젯은 방문 시점 기준으로 D-day를 계산하고, `apply_end`가 지난 항목은 숨깁니다.
