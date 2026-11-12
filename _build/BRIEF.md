# Mavzularni yozish bo'yicha yo'riqnoma (majburiy)

Ish papkasi: `/projects/sandbox/work` (barcha buyruqlarni shu papkada bajaring).

## Vazifa
Sizga berilgan mavzu raqamlari (NNN) uchun `specs/NNN.json` yozing va `python3 check.py NNN ...` bilan tekshirib quring.
Natija `out/NNN.docx`. Rol: parazitologiya bo'yicha oliy toifali shifokor. Til: o'zbek, LOTIN yozuvi, apostrof faqat `'`.

## Namuna
Tayyor namunalar: `specs/004.json`–`specs/020.json`. Uslub, tuzilma va havola formatini AYNAN shulardek qiling (avval 2–3 tasini o'qing).

## Matn talablari
- Ilmiy maqola uslubi: izchil abzatslar, tushuntiruvchi bayon. Repetitorlik/imtihon materiali EMAS.
- "esse" so'zi umuman ishlatilmaydi. Taqiqlangan bo'lim/jumlalar: "Laboratoriya xodimi uchun amaliy xulosa", "Savolga javob berish tartibi", "Savolga ... javob", matn ichida "imtihonda...", "Laborant uchun", "Imtihon uchun qisqa javob", "Eslatma", "Laborant vazifalari", "Misol", "Klinik misol", "Tashxis misoli", "Amaliy misol", "Takrorlash uchun savollar". Kuchsiz qisqa umumiy bo'limlar ham yo'q.
- Sarlavha: `"N. <mavzu nomi>"` — nom `src_txt/NNN.txt` ning birinchi qatoridan (raqam nolsiz). Faqat yaqqol yopishgan so'zlarni ajrating (masalan KLINIKASIVATASHXISI → KLINIKASI VA TASHXISI), boshqa imloni o'zgartirmang.
- Tuzilma: "Kirish" → 6–9 ta mavzuga mos nomlangan bo'lim → "Xulosa". Har bo'limda 2–3 abzats, har abzats 50–90 so'z.
- Hajm: asosiy matn kamida 800 so'z (builder sanaydi; sarlavha va adabiyotlar kirmaydi). Kam bo'lsa, MAZMUNLI abzats qo'shing (suv qo'shmang).
- HAR BIR abzats havola bilan tugaydi: `... matn [1].` yoki `... [1], [3].` Havolalar faqat abzats oxirida.
- Matnda kirill so'zlar bo'lmasin (ruscha manbadagi faktni o'zbekchaga tarjima qilib yozing). Kirill faqat references ichida bo'lishi mumkin.
- Ro'yxat kerak bo'lsa `{"ul": [...]}` (kamdan-kam, oxiri ham havola bilan tugashi shart emas, lekin keyingi abzats havolali bo'lsin).

## Manbalar (ustuvorlik tartibida)
1. Kutubxona matnlari: `lib_txt/<id>.txt` (OCR qilingan, kirill). Ro'yxat: `LIB_INDEX.tsv`. Qidirish: `python3 ctx.py lib_txt/1525.txt "регекс" 5 400` (topilgan joy atrofidagi matn).
   Eng muhimlari:
   - 432 — SSV 121-buyruq (25.03.2015) asosiy matni
   - 1523 Ilova 1 Bezgak; 1524 Ilova 2 Leyshmanioz; 1519 Ilova 3 KQT; 1525 Ilova 4 Gelmintozlar; 1520 Ilova 5 Ichak protozoozlari; 1521 Ilova 6 Laborator diagnostika; 1522 Ilova 7 Epidemiologik nazorat
   - 398 — 166-buyruq (05.04.2016) tashxis/davolash standartlari; 1559 davolash bayonnomalari; 1560, 1600 standartlar
   - 486 — 630-buyruq; 1607 — Exinokokkoz uslubiy qo'llanma; 1547 — TTA bezgak uslubiy qo'llanmasi (2009); 1546 — Bezgakni davolash protokoli
   - 2357 — Jahongirov va boshq. Tibbiy entomologiya (2016); 1604 — Kuliyeva Medicinskaya entomologiya; 2737 — Медицинская паразитология (darslik); 2736 — Pavlovich; 1598 — Romanenko Sanitarnaya parazitologiya; 1543, 2738, 1541 atlaslar
   - 1605, 2104–2115, 2103 bezgak mikroskopiyasi SOPlari; 1535 Fasciolosis (o'zbekcha); prezentatsiyalar (1358 KQT, 1581 gijja, 1592/1591/1580 trixotsefalyoz, 1583 deratizatsiya, 1585 larvitsid, 1597 leyshmanioz epidnazorat, 1593 moskitlar, 1601 ZTL epidkarta va b.)
2. Qonunlar (lex.uz, matni `lex_-2732587.txt` — O'RQ-393; `lex_-26013.txt` — 265-I). Kerak bo'lsa boshqasini: `python3 lex.py "qidiruv"` (lex.uz qidiruvi), hujjat: `https://lex.uz/uz/docs/<id>`.
3. Xalqaro manbalar: `src_txt/NNN.txt` (eski matn) dagi adabiyotlar oldingi sessiyada tekshirilgan — ulardan foydalanish mumkin. Yangi DOI/JSST hujjatini qo'shsangiz, web_search bilan tekshiring; tekshirib bo'lmasa `[tasdiqlanmagan]` deb belgilang.
- Mahalliy hujjat (buyruq ilovasi) mavzuga tegishli bo'lsa, ALBATTA ishlatilsin va undagi aniq raqam/muddat/me'yorlar keltirilsin.
- Hech qachon raqam, muallif, DOI, sana to'qib chiqarmang. Manbada yo'q narsani "buyruqqa ko'ra" demang.

## Adabiyot yozuvlari formati (aynan shunday yozing)
- `O'zbekiston Respublikasi Sog'liqni saqlash vazirligining 2015-yil 25-martdagi 121-son buyrug'iga 4-ilova. Aholi o'rtasida gelmintoz kasalliklarining oldini olish va epidemiyaga qarshi chora-tadbirlar to'g'risidagi yo'riqnoma. – URL: https://xayrullokomilov.uz/api/materiallar/1525/fayl`
- Ilova nomlari: 1 — "Aholi o'rtasida bezgak kasalligining profilaktikasi va chetdan kirib kelishini oldini olish chora-tadbirlari to'g'risidagi yo'riqnoma" (1523); 2 — "Aholi o'rtasida teri va visseral leyshmanioz kasalligini oldini olish va epidemiyaga qarshi chora-tadbirlar to'g'risidagi yo'riqnoma" (1524); 3 — "Kanali qaytalama terlama bo'yicha uslubiy qo'llanma" (1519); 5 — "Aholi o'rtasida ichak protozooz kasalliklarining oldini olish va epidemiyaga qarshi chora-tadbirlar to'g'risidagi yo'riqnoma" (1520); 6 — "Parazitar kasalliklarning laborator diagnostikasi to'g'risidagi yo'riqnoma" (1521); 7 — "Parazitar kasalliklarning epidemiologik nazorati to'g'risidagi yo'riqnoma" (1522).
- Boshqa kutubxona hujjatlari: `Muallif/tashkilot. Nomi. – Joy: Nashriyot, yil. – URL: https://xayrullokomilov.uz/api/materiallar/<id>/fayl` (muallif/yil faylning o'zidan aniqlansin; noma'lum bo'lsa yozilmaydi).
- 1547: `Umirov S.E., Magzumov H.B., Mirzaboyev D.S. va boshq. Bezgakning etiologiyasi, klinikasi, tashxisoti, epidemiologiyasi, epidemiologik nazorati va profilaktikasi: uslubiy qo'llanma. – Toshkent: TTA, 2009. – URL: https://xayrullokomilov.uz/api/materiallar/1547/fayl`
- 2357: `Jahongirov Sh.M., Nurmamatov Sh., Hamzayev R.A. Tibbiy entomologiya: o'quv qo'llanma. – Samarqand: L.M. Isayev nomidagi tibbiy parazitologiya ilmiy-tekshirish instituti, 2016. – 292 b. – URL: https://xayrullokomilov.uz/api/materiallar/2357/fayl`
- 398: `O'zbekiston Respublikasi Sog'liqni saqlash vazirligining 2016-yil 5-apreldagi «Parazitar kasalliklar tashxis va davolash standartlari hamda davolash bayonnomalarini tasdiqlash to'g'risida»gi 166-son buyrug'i. – URL: https://xayrullokomilov.uz/api/materiallar/398/fayl`
- Qonun: `O'zbekiston Respublikasining 2015-yil 26-avgustdagi «Aholining sanitariya-epidemiologik osoyishtaligi to'g'risida»gi O'RQ-393-son Qonuni (amaldagi tahrir). – URL: https://lex.uz/uz/docs/-2732587`
- Har bir manba matnda kamida bir marta ishlatilsin; ishlatilmaganini ro'yxatdan olib tashlang.

## Bir xil savollar
Agar ikki mavzu nomi bir xil bo'lsa (faqat raqami farq qilsa), ikkinchisining matni birinchisiniki bilan bir xil bo'ladi (faqat number va title raqami o'zgaradi). O'xshash, lekin boshqacha savolga kontekstiga mos alohida matn yoziladi.

## Tekshiruv va yakun
- Har bir fayl uchun `python3 check.py NNN` — natija `OK NNN.docx: XXX so'z` bo'lishi shart. `XATO`/`QISQA` bo'lsa, tuzatib qayta ishga tushiring.
- Boshqa agentlarning fayllariga TEGMANG (faqat o'z raqamlaringiz). git ishlatmang.
- Yakunda qisqa hisobot qaytaring: har bir fayl — so'z soni, asosiy mahalliy manbalar; tasdiqlanmagan faktlar; sarlavhadagi tuzatishlar; manbalar o'rtasidagi farqlar.
