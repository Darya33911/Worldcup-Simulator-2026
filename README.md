# Worldcup-Simulator-2026
World cup 2026 Simulator - Advanced Programming Project
# 🏆 World Cup 2026 Simulator

یک شبیه‌ساز جام جهانی فوتبال با رویکرد ۳۲ تیمی با استفاده از برنامه‌نویسی شی‌گرا در زبان پایتون.


ویژگی‌ها

- بارگذاری تیم‌ها از فایل CSV
- قرعه‌کشی گروه‌ها بر اساس سیدبندی فیفا
- شبیه‌سازی مرحله گروهی با توزیع پواسون
- شبیه‌سازی مراحل حذفی (یک‌هشتم، یک‌چهارم، نیمه‌نهایی، فینال)
- پیاده‌سازی قوانین کامل فیفا (امتیازدهی، تفاضل گل، قانون بازی مستقیم، پنالتی)
- شبیه‌سازی ۱۰۰۰ باره و محاسبه درصد قهرمانی
- نمایش براکت حذفی


ابزارها

- Python 3.14
- کتابخانه‌های: `csv`, `os`, `random`, `math`

  ساختار فایل‌ها
Worldcup-Simulator-2026/│

├── main.py # نقطه ورود برنامه

├── utils.py # توزیع پواسون

├── team.py # کلاس Team

├── match.py # کلاس Match

├── group.py # کلاس Group

├── knockout_stage.py # کلاس KnockoutStage

├── world_cup_simulator.py # کلاس اصلی

└── worldcup_2026_teams.csv # داده‌های تیم‌ها




نحوه اجرا


python main.py




خروجی نمونه

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

شبیه‌سازی ۱۰۰۰ باره


Simulation completed 1000 times.
Championship percentages:
----------------------------------------
Brazil              :  28.4%
France              :  18.2%
Argentina           :  15.1%
Germany             :   8.3%
...
----------------------------------------
15 teams had 0% championship probability.

توسعه‌دهنده
نام: دریا بهروز

شماره دانشجویی: ۴۰۴۱۳۰۴۷۳

دانشگاه: دانشگاه صنعتی همدان

درس: برنامه‌سازی پیشرفته

استاد: مرتضی بهرامی
