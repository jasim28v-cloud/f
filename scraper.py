import requests
from bs4 import BeautifulSoup
from datetime import datetime

def run_vortex_stars_scraper():
    # مصدر أخبار المشاهير (سيدتي) لضمان مطابقة الصورة المطلوبة
    rss_url = "https://www.sayidaty.net/taxonomy/term/31/rss.xml"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    try:
        # الرابط الإعلاني الخاص بك
        my_ad_link = "https://data527.click/21330bf1d025d41336e6/4ba0cfe12d/?placementName=default"
        
        response = requests.get(rss_url, headers=headers, timeout=20)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.content, 'xml')
        items = soup.find_all('item')
        
        news_html = ""
        for i, item in enumerate(items[:15]):
            title = item.title.text
            # استخراج الصورة من الرابط الوصفي
            img = "https://via.placeholder.com/800x450"
            if item.find('enclosure'):
                img = item.find('enclosure').get('url')
            
            news_html += f'''
            <div class="star-card">
                <a href="{my_ad_link}" target="_blank">
                    <div class="star-img">
                        <img src="{img}" loading="lazy">
                        <span class="star-tag">حصري</span>
                    </div>
                    <div class="star-content">
                        <span class="star-cat">مشاهير العرب</span>
                        <h3>{title}</h3>
                        <div class="star-footer">
                            <span class="star-date">{datetime.now().strftime('%d مارس 2026')}</span>
                            <span class="star-more">التفاصيل</span>
                        </div>
                    </div>
                </a>
            </div>'''

        full_html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VORTEX STARS | مشاهير</title>
    
    <script src="https://data527.click/pfe/current/tag.min.js?z=8345712" data-cfasync="false" async></script>
    
    <script type='text/javascript' src='//pl25330eef.effectiveratecpm.com/26/33/0e/26330eef1cb397212db567d1385dc0b9.js'></script>

    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        :root {{ --bg: #ffffff; --text: #1a1a1a; --accent: #e91e63; --gray: #757575; }}
        body {{ background: var(--bg); color: var(--text); font-family: 'Cairo', sans-serif; margin: 0; padding-bottom: 30px; }}
        
        header {{ background: #fff; padding: 10px 5%; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #eee; position: sticky; top: 0; z-index: 1000; }}
        .v-logo {{ font-size: 22px; font-weight: 900; color: #000; text-decoration: none; }}
        .v-logo span {{ color: var(--accent); }}

        .container {{ max-width: 700px; margin: 0 auto; padding: 0 10px; }}

        /* تصميم كروت المشاهير المحدث */
        .star-card {{ background: #fff; margin-bottom: 25px; border-bottom: 1px solid #f0f0f0; padding-bottom: 15px; }}
        .star-card a {{ text-decoration: none; color: inherit; }}
        .star-img {{ width: 100%; height: 350px; position: relative; border-radius: 8px; overflow: hidden; }}
        .star-img img {{ width: 100%; height: 100%; object-fit: cover; }}
        .star-tag {{ position: absolute; top: 15px; right: 15px; background: var(--accent); color: #fff; font-size: 11px; font-weight: bold; padding: 3px 12px; border-radius: 4px; }}
        
        .star-content {{ padding: 15px 5px; }}
        .star-cat {{ font-size: 13px; color: var(--gray); display: block; margin-bottom: 8px; }}
        .star-content h3 {{ font-size: 19px; margin: 0 0 15px; line-height: 1.5; font-weight: 700; }}
        .star-footer {{ display: flex; justify-content: space-between; align-items: center; }}
        .star-date {{ font-size: 12px; color: #999; }}
        .star-more {{ color: var(--accent); font-weight: bold; font-size: 13px; border: 1px solid var(--accent); padding: 2px 10px; border-radius: 4px; }}

        @media (max-width: 600px) {{
            .star-img {{ height: 280px; }}
            .star-content h3 {{ font-size: 17px; }}
        }}
    </style>
</head>
<body onclick="void(0)">
    <header>
        <div style="cursor:pointer;">☰</div>
        <a href="#" class="v-logo">VORTEX<span>STARS</span></a>
        <div style="cursor:pointer;">🔍</div>
    </header>

    <div class="container">
        <div style="padding: 20px 0; font-weight: 900; font-size: 20px; border-bottom: 3px solid var(--accent); display: inline-block; margin-bottom: 20px;">آخر أخبار النجوم</div>
        {news_html}
    </div>

    <footer style="text-align: center; padding: 30px; background: #f9f9f9; color: #888; font-size: 12px;">
        VORTEX STARS 2026 - جميع الحقوق محفوظة
    </footer>
</body>
</html>'''

        with open("stars.html", "w", encoding="utf-8") as f: f.write(full_html)
    except Exception as e: print(f"Error: {e}")

if __name__ == "__main__":
    run_vortex_stars_scraper()
