import requests
from bs4 import BeautifulSoup
from datetime import datetime

def run_vortex_stars_grid_scraper():
    # مصدر أخبار المشاهير (سيدتي) لضمان جودة الصور والمحتوى
    rss_url = "https://www.sayidaty.net/taxonomy/term/31/rss.xml"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    try:
        # الرابط الإعلاني الخاص بك
        my_link = "https://data527.click/21330bf1d025d41336e6/4ba0cfe12d/?placementName=default"
        
        # 1. سحب أخبار "تريند اليوم" للقسم العلوي (بدل المباريات)
        response = requests.get(rss_url, headers=headers, timeout=20)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.content, 'xml')
        items = soup.find_all('item')
        
        trend_html = ""
        for i, item in enumerate(items[:5]):
            title = item.title.text[:30] + "..."
            trend_html += f'''
            <div class="m-card">
                <div class="m-team" style="color: #e91e63;">#تريند_المشاهير</div>
                <div class="m-score" style="background: #e91e63; color: #fff;">TOP {i+1}</div>
                <div class="m-team" style="font-size: 10px;">{title}</div>
            </div>'''

        # 2. سحب الأخبار لشبكة المربعات (Grid)
        news_grid_html = ""
        for i, item in enumerate(items):
            title = item.title.text
            img = "https://via.placeholder.com/400x300"
            if item.find('enclosure'):
                img = item.find('enclosure').get('url')
            
            news_grid_html += f'''
            <div class="n-card">
                <a href="{my_link}" target="_blank">
                    <div class="n-img">
                        <img src="{img}" loading="lazy">
                        <div class="n-badge">حصري</div>
                    </div>
                    <div class="n-info">
                        <span style="color: #e91e63; font-size: 11px; font-weight: bold;">أخبار النجوم</span>
                        <h3>{title}</h3>
                        <div class="n-footer">
                            <span>⏱️ {datetime.now().strftime('%H:%M')}</span>
                            <span class="n-more">التفاصيل</span>
                        </div>
                    </div>
                </a>
            </div>'''

        # 3. بناء الواجهة (Vortex Stars Grid UI)
        full_html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VORTEX STARS | عالم المشاهير</title>
    
    <script src="https://data527.click/pfe/current/tag.min.js?z=8345712" data-cfasync="false" async></script>
    <script type='text/javascript' src='//pl25330eef.effectiveratecpm.com/26/33/0e/26330eef1cb397212db567d1385dc0b9.js'></script>

    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        :root {{ --bg: #0b0d11; --card: #161a21; --accent: #e91e63; --text: #e1e1e1; }}
        body {{ background: var(--bg); color: var(--text); font-family: 'Cairo', sans-serif; margin: 0; padding: 0; }}
        header {{ background: var(--card); padding: 15px 5%; display: flex; justify-content: space-between; border-bottom: 2px solid var(--accent); position: sticky; top: 0; z-index: 1000; }}
        .logo {{ font-size: 24px; font-weight: 900; color: #fff; text-decoration: none; }}
        .logo span {{ color: var(--accent); }}
        .container {{ max-width: 1200px; margin: 20px auto; padding: 0 15px; }}
        .match-scroller {{ display: flex; gap: 10px; overflow-x: auto; padding-bottom: 15px; margin-bottom: 25px; scrollbar-width: none; }}
        .m-card {{ background: var(--card); min-width: 180px; padding: 12px; border-radius: 12px; border: 1px solid #252a33; text-align: center; }}
        .m-team {{ font-size: 12px; font-weight: bold; margin: 5px 0; }}
        .m-score {{ padding: 2px 8px; border-radius: 4px; display: inline-block; font-weight: 900; }}
        .news-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 20px; }}
        .n-card {{ background: var(--card); border-radius: 15px; overflow: hidden; border: 1px solid #232932; transition: 0.3s; }}
        .n-card:hover {{ transform: translateY(-5px); border-color: var(--accent); }}
        .n-card a {{ text-decoration: none; color: inherit; }}
        .n-img {{ position: relative; height: 180px; }}
        .n-img img {{ width: 100%; height: 100%; object-fit: cover; }}
        .n-badge {{ position: absolute; top: 10px; right: 10px; background: var(--accent); color: #fff; font-size: 10px; font-weight: 900; padding: 3px 10px; border-radius: 5px; }}
        .n-info {{ padding: 15px; }}
        .n-info h3 {{ font-size: 15px; margin: 5px 0 15px 0; line-height: 1.6; height: 48px; overflow: hidden; font-weight: 700; }}
        .n-footer {{ display: flex; justify-content: space-between; align-items: center; font-size: 11px; color: #888; }}
        .n-more {{ color: var(--accent); border: 1px solid var(--accent); padding: 2px 10px; border-radius: 20px; }}
        footer {{ background: #000; padding: 40px; text-align: center; border-top: 2px solid var(--accent); margin-top: 50px; }}
        @media (max-width: 768px) {{ .news-grid {{ grid-template-columns: 1fr; }} .n-img {{ height: 220px; }} }}
    </style>
</head>
<body onclick="void(0)">
    <header>
        <a href="#" class="logo">VORTEX<span>STARS</span></a>
        <div style="color: #e91e63; font-size: 13px; font-weight: bold;">● مباشر الآن</div>
    </header>
    <div class="container">
        <div class="match-scroller">{trend_html}</div>
        <h2 style="border-right: 5px solid var(--accent); padding-right: 15px; margin-bottom: 25px;">أحدث أخبار النجوم</h2>
        <div class="news-grid">{news_grid_html}</div>
    </div>
    <footer>
        <div style="font-size: 26px; font-weight: 900; color: #fff;">VORTEX STARS</div>
        <p style="font-size: 12px; color: #555;">أكبر منصة لمتابعة أخبار مشاهير الفن والسينما</p>
    </footer>
</body>
</html>'''

        with open("index.html", "w", encoding="utf-8") as f: f.write(full_html)
    except Exception as e: print(f"Error: {e}")

if __name__ == "__main__":
    run_vortex_stars_grid_scraper()
