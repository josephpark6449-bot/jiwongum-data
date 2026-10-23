#!/usr/bin/env python3
"""deadline.json 에 쓰레드 공지용 notice 블록을 계산해 넣는다.
기준일 = updated. 1일 이상 남은 마감형 항목만, 마감 빠른 순 최대 5건."""
import json, sys, datetime as dt
path = sys.argv[1] if len(sys.argv) > 1 else "deadline.json"
d = json.load(open(path, encoding="utf-8"))
today = dt.date.fromisoformat(d["updated"])
def day(s):
    try: return dt.date.fromisoformat(s)
    except Exception: return None
cands = []
for i in d["items"]:
    end = day(i.get("apply_end", ""))
    if i.get("always") or not end: continue
    left = (end - today).days
    if left < 1: continue
    start = day(i.get("apply_start", ""))
    status = "접수중" if (not start or start <= today) else f"{start.month}/{start.day} 접수 시작"
    cands.append((left, i, status))
cands.sort(key=lambda x: x[0])
pick = cands[:5]
d["notice"] = {
    "date": d["updated"],
    "total": len(cands),
    "items": [{"id": i["id"], "name": i["name"], "audience": i.get("audience", ""),
               "dday": f"D-{left}", "status": status, "apply_end": i["apply_end"],
               "summary": i.get("summary", "")} for left, i, status in pick],
    "rest": max(len(cands) - len(pick), 0),
    "link": "https://blog9.josephpark64.com/?utm_source=threads" + (f"#item-{pick[0][1]['id']}" if pick else "#deadline"),
}
json.dump(d, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"notice: {len(pick)}건 / 전체 {len(cands)}건 / link {d['notice']['link']}")
