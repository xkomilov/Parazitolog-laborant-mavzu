#!/usr/bin/env python3
"""Spec tekshiruvi + qurish.  Ishlatish:  python3 check.py 021 022 ...
Har bir NNN uchun: specs/NNN.json ni tekshiradi, keyin builder bilan out/NNN.docx quradi."""
import json, re, sys, subprocess, os
BAN = r"\besse|imtihon|laborant uchun|laboratoriya xodimi uchun|savolga|takrorlash uchun|klinik misol|tashxis misoli|amaliy misol|laborant vazifalari|qisqa javob"
BAN_HEAD = r"^(misol|eslatma|laborant|amaliy xulosa|amaliy ahamiyati$|laboratoriya uchun)"
ok_all = True
for n in sys.argv[1:]:
    f = f"specs/{n}.json"
    errs = []
    try:
        s = json.load(open(f))
    except Exception as e:
        print(f"XATO {n}: JSON o'qilmadi: {e}"); ok_all = False; continue
    if s.get("number") != int(n): errs.append("number mos emas")
    if not re.match(rf"^{int(n)}\. \S", s.get("title", "")): errs.append("sarlavha 'N. ...' formatida emas")
    t = json.dumps(s, ensure_ascii=False)
    if re.search(BAN, t, re.I): errs.append("taqiqlangan so'z: " + ", ".join(set(re.findall(BAN, t, re.I))))
    heads = [x["heading"] for x in s["sections"]]
    if heads[0] != "Kirish" or heads[-1] != "Xulosa": errs.append("Kirish/Xulosa yo'q")
    for h in heads:
        if re.search(BAN_HEAD, h, re.I): errs.append("taqiqlangan bo'lim: " + h)
    nref = len(s["references"])
    for x in s["sections"]:
        for c in x["content"]:
            if isinstance(c, str):
                if not re.search(r"\[\d+\](, \[\d+\])*\.?$", c): errs.append("abzats havolasiz tugaydi: " + c[:50])
                if re.search(r"[А-Яа-яЁё]{3,}", c): errs.append("matnda kirill so'z: " + c[:50])
            for m in re.findall(r"\[(\d+)\]", json.dumps(c, ensure_ascii=False)):
                if int(m) > nref or int(m) < 1: errs.append(f"[{m}] adabiyotda yo'q")
    if errs:
        ok_all = False
        print(f"XATO {n}: " + " | ".join(dict.fromkeys(errs)))
        continue
    r = subprocess.run(["node", "topic-docx-packager/scripts/build_docx.js", f, "out", "--min", "800"],
                       capture_output=True, text=True, env=dict(os.environ, NODE_PATH="_deps/node_modules"))
    print(r.stdout.strip())
    if not r.stdout.startswith("OK"): ok_all = False
sys.exit(0 if ok_all else 1)
