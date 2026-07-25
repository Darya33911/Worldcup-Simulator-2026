# 🏆 World Cup 2026 Simulator

یک شبیه‌ساز جام جهانی فوتبال با رویکرد ۳۲ تیمی با استفاده از برنامه‌نویسی شی‌گرا در زبان پایتون.

---

## ویژگی‌ها

- بارگذاری تیم‌ها از فایل CSV
- قرعه‌کشی گروه‌ها بر اساس سیدبندی فیفا
- شبیه‌سازی مرحله گروهی با توزیع پواسون
- شبیه‌سازی مراحل حذفی (یک‌هشتم، یک‌چهارم، نیمه‌نهایی، فینال)
- پیاده‌سازی قوانین کامل فیفا (امتیازدهی، تفاضل گل، قانون بازی مستقیم، پنالتی)
- شبیه‌سازی ۱۰۰۰ باره و محاسبه درصد قهرمانی
- نمایش براکت حذفی

---

## ابزارها

- Python 3.14
- کتابخانه‌های: `csv`, `os`, `random`, `math`

---

##ساختار فایل‌ها
Worldcup-Simulator-2026/
│
├── main.py # نقطه ورود برنامه
├── utils.py # توزیع پواسون
├── team.py # کلاس Team
├── match.py # کلاس Match
├── group.py # کلاس Group
├── knockout_stage.py # کلاس KnockoutStage
├── world_cup_simulator.py # کلاس اصلی
└── worldcup_2026_teams.csv # داده‌های تیم‌ها


---

## نحوه اجرا


python main.py


##خروجی نمونه
مرحله گروهی
===== Group A =====
1. Brazil: 9 pts, GD +5, GF 8
2. France: 6 pts, GD +2, GF 5
3. Argentina: 3 pts, GD -1, GF 3
4. Japan: 0 pts, GD -6, GF 1
 فینال
===== Final =====
Brazil 2 - 1 Germany
Champion: Brazil

شبیه سازی 1000 باره
Simulation completed 1000 times.
Championship percentages:
----------------------------------------
Brazil              :  28.4%
France              :  18.2%
Argentina           :  15.1%
Germany             :   8.3%
England             :   7.2%
Spain               :   5.8%
Netherlands         :   4.1%
Portugal            :   3.5%
Belgium             :   2.8%
Croatia             :   2.1%
Uruguay             :   1.5%
Mexico              :   1.2%
Switzerland         :   0.8%
...
----------------------------------------
15 teams had 0% championship probability.

براکت حذفی
===== Knockout Bracket =====

===== Round of 16 =====
Brazil 3-0 Portugal -> Winner: Brazil
France 2-1 England -> Winner: France
Germany 1-0 Spain -> Winner: Germany
Argentina 2-0 Netherlands -> Winner: Argentina
Belgium 3-2 Croatia -> Winner: Belgium
Uruguay 1-0 Mexico -> Winner: Uruguay
Switzerland 1-1 (4-3) Italy -> Winner: Switzerland
Denmark 2-1 Sweden -> Winner: Denmark

===== Quarterfinals =====
Brazil 1-0 France -> Winner: Brazil
Germany 2-1 Argentina -> Winner: Germany
Belgium 3-1 Uruguay -> Winner: Belgium
Switzerland 0-0 (5-4) Denmark -> Winner: Switzerland

===== Semifinals =====
Brazil 2-1 Germany -> Winner: Brazil
Belgium 1-1 (3-2) Switzerland -> Winner: Belgium

===== Final =====
Brazil 2-1 Belgium -> Winner: Brazil
Champion: Brazil 🏆

##توسعه دهنده

نام: دریا بهروز

شماره دانشجویی: ۴۰۴۱۳۰۴۷۳

دانشگاه: دانشگاه صنعتی همدان

دانشکده: مهندسی کامپیوتر

درس: برنامه‌سازی پیشرفته

استاد: مرتضی بهرامی


   ## 📄 فایل کامل `README.md` برای کپی و جایگزینی

```markdown
# 🏆 World Cup 2026 Simulator

یک شبیه‌ساز جام جهانی فوتبال با رویکرد ۳۲ تیمی با استفاده از برنامه‌نویسی شی‌گرا در زبان پایتون.

---

## 📋 ویژگی‌ها

- بارگذاری تیم‌ها از فایل CSV
- قرعه‌کشی گروه‌ها بر اساس سیدبندی فیفا
- شبیه‌سازی مرحله گروهی با توزیع پواسون
- شبیه‌سازی مراحل حذفی (یک‌هشتم، یک‌چهارم، نیمه‌نهایی، فینال)
- پیاده‌سازی قوانین کامل فیفا (امتیازدهی، تفاضل گل، قانون بازی مستقیم، پنالتی)
- شبیه‌سازی ۱۰۰۰ باره و محاسبه درصد قهرمانی
- نمایش براکت حذفی

---

## 🛠️ ابزارها

- Python 3.14
- کتابخانه‌های: `csv`, `os`, `random`, `math`

---

## 📁 ساختار فایل‌ها

```
Worldcup-Simulator-2026/
│
├── main.py                 # نقطه ورود برنامه
├── utils.py                # توزیع پواسون
├── team.py                 # کلاس Team
├── match.py                # کلاس Match
├── group.py                # کلاس Group
├── knockout_stage.py       # کلاس KnockoutStage
├── world_cup_simulator.py  # کلاس اصلی
└── worldcup_2026_teams.csv # داده‌های تیم‌ها
```

---

## 🚀 نحوه اجرا

```bash
python main.py
```

---

## 📊 خروجی نمونه

### مرحله گروهی

```
===== Group A =====
1. Brazil: 9 pts, GD +5, GF 8
2. France: 6 pts, GD +2, GF 5
3. Argentina: 3 pts, GD -1, GF 3
4. Japan: 0 pts, GD -6, GF 1
```

### فینال

```
===== Final =====
Brazil 2 - 1 Germany
Champion: Brazil
```

### شبیه‌سازی ۱۰۰۰ باره

```
Simulation completed 1000 times.
Championship percentages:
----------------------------------------
Brazil              :  28.4%
France              :  18.2%
Argentina           :  15.1%
Germany             :   8.3%
England             :   7.2%
Spain               :   5.8%
Netherlands         :   4.1%
Portugal            :   3.5%
Belgium             :   2.8%
Croatia             :   2.1%
Uruguay             :   1.5%
Mexico              :   1.2%
Switzerland         :   0.8%
...
----------------------------------------
15 teams had 0% championship probability.
```

### براکت حذفی

```
===== Knockout Bracket =====

===== Round of 16 =====
Brazil 3-0 Portugal -> Winner: Brazil
France 2-1 England -> Winner: France
Germany 1-0 Spain -> Winner: Germany
Argentina 2-0 Netherlands -> Winner: Argentina
Belgium 3-2 Croatia -> Winner: Belgium
Uruguay 1-0 Mexico -> Winner: Uruguay
Switzerland 1-1 (4-3) Italy -> Winner: Switzerland
Denmark 2-1 Sweden -> Winner: Denmark

===== Quarterfinals =====
Brazil 1-0 France -> Winner: Brazil
Germany 2-1 Argentina -> Winner: Germany
Belgium 3-1 Uruguay -> Winner: Belgium
Switzerland 0-0 (5-4) Denmark -> Winner: Switzerland

===== Semifinals =====
Brazil 2-1 Germany -> Winner: Brazil
Belgium 1-1 (3-2) Switzerland -> Winner: Belgium

===== Final =====
Brazil 2-1 Belgium -> Winner: Brazil
Champion: Brazil 🏆
```

---

## 👩‍💻 توسعه‌دهنده

- **نام:** دریا بهروز
- **شماره دانشجویی:** ۴۰۴۱۳۰۴۷۳
- **دانشگاه:** دانشگاه صنعتی همدان
- **دانشکده:** مهندسی کامپیوتر
- **درس:** برنامه‌سازی پیشرفته
- **استاد:** مرتضی بهرامی
- **تاریخ تحویل:** ۰۱/۰۵/۱۴۰۵

---

## 📄 مجوز

این پروژه برای پروژه درس برنامه‌سازی پیشرفته تهیه شده است.

---

**موفق باشید!** 🏆⚽
```

---

## ✅ چطور جایگزین کنم؟

1. توی گیت‌هاب، روی فایل `README.md` کلیک کنید
2. دکمه مداد (`✏️`) رو بزنید
3. کل متن قبلی رو پاک کنید
4. متن بالا رو کپی کنید و بچسبونید
5. برید پایین و **`Commit changes`** رو بزنید

---

**تموم شد!** 🚀
