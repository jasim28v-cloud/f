import requests
from bs4 import BeautifulSoup
from datetime import datetime

def run_stadium_stars_premium():
    # استخدام مصدر سيدتي المستقر لضمان ظهور الصور 100% مثل RT
    rss_url = "https://www.sayidaty.net/taxonomy/term/31/rss.xml"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    try:
        my_link = "https://data527.click/21330bf1d025d41336e6/4ba0cfe12d/?placementName=default"
        
        response = requests.get(rss_url, headers=headers, timeout=20)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.content, 'xml')
        items = soup.find_all('item')
        
        news_grid_html = ""
        for item in items[:15]:
            title = item.title.text
            img = item.find('enclosure').get('url') if item.find('enclosure') else "https://via.placeholder.com/500x350"
            
            news_grid_html += f'''
            <div class="card">
                <a href="{my_link}" target="_blank">
                    <div class="card-img">
                        <img src="{img}" alt="news">
                        <div class="badge">حصري</div>
                    </div>
                    <div class="card-body">
                        <span class="category">أخبار المشاهير</span>
                        <h3>{title}</h3>
                        <div class="card-footer">
                            <span>⏱️ {datetime.now().strftime('%H:%M')}</span>
                            <span class="read-more">التفاصيل ←</span>
                        </div>
                    </div>
                </a>
            </div>'''

        full_html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>STADIUM STARS | عالم النجوم</title>
    
    <script src="https://data527.click/pfe/current/tag.min.js?z=8345712" data-cfasync="false" async></script>
    <script type='text/javascript' src='//pl25330eef.effectiveratecpm.com/26/33/0e/26330eef1cb397212db567d1385dc0b9.js'></script>

    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        :root {{ --primary: #ff0055; --dark: #0f1115; --card-bg: #1a1d23; --text: #ffffff; }}
        body {{ background: var(--dark); color: var(--text); font-family: 'Cairo', sans-serif; margin: 0; padding: 0; }}
        
        header {{ background: linear-gradient(45deg, #000, #222); padding: 20px 5%; display: flex; justify-content: space-between; align-items: center; border-bottom: 3px solid var(--primary); position: sticky; top: 0; z-index: 1000; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }}
        .logo {{ font-size: 28px; font-weight: 900; color: #fff; text-decoration: none; text-transform: uppercase; letter-spacing: 1px; }}
        .logo span {{ color: var(--primary); }}

        .hero {{ padding: 30px 15px; text-align: center; background: url('https://www.transparenttextures.com/patterns/carbon-fibre.png'); }}
        .hero h1 {{ font-size: 24px; border-right: 5px solid var(--primary); padding-right: 15px; display: inline-block; }}

        .container {{ max-width: 1200px; margin: 0 auto; padding: 20px; }}
        
        /* شبكة البطاقات الاحترافية */
        .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 25px; }}
        .card {{ background: var(--card-bg); border-radius: 15px; overflow: hidden; transition: 0.4s; border: 1px solid #2d323b; position: relative; }}
        .card:hover {{ transform: translateY(-10px); border-color: var(--primary); box-shadow: 0 10px 30px rgba(255, 0, 85, 0.2); }}
        .card a {{ text-decoration: none; color: inherit; }}
        
        .card-img {{ position: relative; height: 200px; }}
        .card-img img {{ width: 100%; height: 100%; object-fit: cover; }}
        .badge {{ position: absolute; top: 15px; right: 15px; background: var(--primary); font-size: 11px; font-weight: 900; padding: 4px 12px; border-radius: 5px; box-shadow: 0 4px 10px rgba(0,0,0,0.3); }}
        
        .card-body {{ padding: 20px; }}
        .category {{ color: var(--primary); font-size: 12px; font-weight: bold; text-transform: uppercase; }}
        .card-body h3 {{ font-size: 18px; margin: 10px 0; line-height: 1.5; height: 54px; overflow: hidden; }}
        
        .card-footer {{ display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #2d323b; margin-top: 15px; padding-top: 15px; font-size: 13px; color: #aaa; }}
        .read-more {{ color: var(--primary); font-weight: bold; }}

        footer {{ background: #000; padding: 50px 20px; text-align: center; margin-top: 50px; border-top: 3px solid var(--primary); }}
        
        @media (max-width: 768px) {{ .grid {{ grid-template-columns: 1fr; }} .card-img {{ height: 250px; }} }}
    </style>
</head>
<body onclick="void(0)">
    <header>
        <a href="#" class="logo">Stadium<span>Stars</span></a>
        <div style="background: #00ff88; color: #000; padding: 2px 10px; border-radius: 20px; font-size: 12px; font-weight: bold;">LIVE</div>
    </header>

    <div class="hero">
        <h1>✨ أحدث تريندات المشاهير الآن</h1>
    </div>

    <div class="container">
        <div class="grid">
            {news_grid_html}
        </div>
    </div>

    <footer>
        <div class="logo" style="font-size: 35px;">Stadium<span>Stars</span></div>
        <p style="color: #666; margin-top: 10px;">جميع حقوق النشر محفوظة © 2026</p>
    </footer>
</body>
</html>'''

        with open("index.html", "w", encoding="utf-8") as f: f.write(full_html)
    except Exception as e: print(f"Error: {e}")

if __name__ == "__main__":
    run_stadium_stars_premium()
