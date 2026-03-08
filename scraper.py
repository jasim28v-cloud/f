import requests
from bs4 import BeautifulSoup
from datetime import datetime

def run_vortex_rt_stable():
    # المصدر المضمون (RT) الذي لا يفشل أبداً في السحب
    rss_url = "https://arabic.rt.com/rss/sport/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    try:
        # الرابط الربحي الخاص بك
        my_link = "https://data527.click/21330bf1d025d41336e6/4ba0cfe12d/?placementName=default"
        
        response = requests.get(rss_url, headers=headers, timeout=20)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.content, 'xml')
        items = soup.find_all('item')
        
        news_grid_html = ""
        for item in items[:16]:
            title = item.title.text
            # سحب الصور بنفس طريقة RT التي تنجح معك دائماً
            img = item.find('enclosure').get('url') if item.find('enclosure') else "https://via.placeholder.com/500x350"
            
            news_grid_html += f'''
            <div class="v-card">
                <a href="{my_link}" target="_blank">
                    <div class="v-img-container">
                        <img src="{img}" alt="News Image" loading="lazy">
                        <div class="v-badge">عاجل</div>
                    </div>
                    <div class="v-body">
                        <h3>{title}</h3>
                        <div class="v-footer">
                            <span>🕒 {datetime.now().strftime('%H:%M')}</span>
                            <span class="v-btn">التفاصيل</span>
                        </div>
                    </div>
                </a>
            </div>'''

        full_html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VORTEX PRO | أخبار الساعة</title>
    
    <script src="https://data527.click/pfe/current/tag.min.js?z=8345712" data-cfasync="false" async></script>
    <script type='text/javascript' src='//pl25330eef.effectiveratecpm.com/26/33/0e/26330eef1cb397212db567d1385dc0b9.js'></script>

    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        :root {{ --main: #007bff; --dark: #0a0a0a; --card: #141414; }}
        body {{ background: var(--dark); color: #fff; font-family: 'Cairo', sans-serif; margin: 0; padding: 0; }}
        header {{ background: #000; padding: 15px 5%; display: flex; justify-content: space-between; border-bottom: 2px solid var(--main); position: sticky; top: 0; z-index: 1000; }}
        .logo {{ font-size: 24px; font-weight: 900; color: #fff; text-decoration: none; }}
        .logo span {{ color: var(--main); }}
        
        .container {{ max-width: 1200px; margin: 20px auto; padding: 0 15px; }}
        
        /* تصميم الشبكة الاحترافي */
        .v-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 20px; }}
        .v-card {{ background: var(--card); border-radius: 12px; overflow: hidden; border: 1px solid #222; transition: 0.3s; }}
        .v-card:hover {{ transform: translateY(-5px); border-color: var(--main); }}
        .v-card a {{ text-decoration: none; color: inherit; }}
        
        .v-img-container {{ position: relative; height: 180px; }}
        .v-img-container img {{ width: 100%; height: 100%; object-fit: cover; }}
        .v-badge {{ position: absolute; top: 10px; right: 10px; background: var(--main); color: #fff; font-size: 10px; padding: 3px 10px; border-radius: 5px; font-weight: bold; }}
        
        .v-body {{ padding: 15px; }}
        .v-body h3 {{ font-size: 15px; margin: 0 0 15px 0; line-height: 1.6; height: 48px; overflow: hidden; }}
        
        .v-footer {{ display: flex; justify-content: space-between; align-items: center; font-size: 11px; color: #888; }}
        .v-btn {{ color: var(--main); border: 1px solid var(--main); padding: 2px 10px; border-radius: 20px; }}
        
        @media (max-width: 768px) {{ .v-grid {{ grid-template-columns: 1fr; }} }}
    </style>
</head>
<body onclick="void(0)">
    <header>
        <a href="#" class="logo">VORTEX<span>24</span></a>
        <div style="color: #00ff88; font-size: 13px; font-weight: bold;">● مباشر</div>
    </header>

    <div class="container">
        <h2 style="border-right: 5px solid var(--main); padding-right: 15px; margin-bottom: 25px;">أبرز الأخبار الآن</h2>
        <div class="v-grid">{news_grid_html}</div>
    </div>
</body>
</html>'''

        with open("index.html", "w", encoding="utf-8") as f: f.write(full_html)
    except Exception as e: print(f"Error: {e}")

if __name__ == "__main__":
    run_vortex_rt_stable()
