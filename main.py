from datetime import date
from pathlib import Path

topics = [
    ("हिमालय के अद्भुत रहस्य", "Amazing Secrets of the Himalayas"),
    ("झरने कैसे बनते हैं?", "How Are Waterfalls Formed?"),
    ("जंगल हमारे लिए क्यों जरूरी हैं?", "Why Are Forests Important?"),
    ("नदियों का पानी कहाँ से आता है?", "Where Does River Water Come From?"),
    ("प्रकृति के 5 अद्भुत तथ्य", "5 Amazing Facts About Nature"),
]

output = ["MOUNTORA - DAILY SHORTS PLAN", str(date.today()), ""]

for i, (hindi, english) in enumerate(topics, 1):
    output.extend([
        f"SHORT {i}",
        f"Hindi Topic: {hindi}",
        f"English Topic: {english}",
        "Hindi Hook: क्या आप प्रकृति का यह अद्भुत रहस्य जानते हैं?",
        "English Hook: Did you know this amazing fact about nature?",
        "Visual: Use relevant nature footage.",
        "-" * 35
    ])

Path("output").mkdir(exist_ok=True)
Path("output/shorts_plan.txt").write_text(
    "\n".join(output), encoding="utf-8"
)

print("MOUNTORA: 5 Shorts plans created successfully!")
