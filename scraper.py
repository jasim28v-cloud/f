import requests
from bs4 import BeautifulSoup
from datetime import datetime

def run_vogue_premium_scraper():
    # سحب المحتوى من Vogue مباشرة لضمان مطابقة التصميم
    target_url = "https://www.vogue.com/celebrity-style"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    try:
        # الرابط الربحي الخاص بك
        my_link = "https://data527.click/21330bf1d025d41336e6/4ba0cfe12d/?placementName=default"
        
        response = requests.get(target_url, headers=headers, timeout=20)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # استخراج المقالات بناءً على هيكلية Vogue
        articles = soup.find_all('div', class_='summary-item')
        
        news_html = ""
        for item in articles[:10]:
            title = item.find('h2').text if item.find('h2') else ""
            img_tag = item.find('img')
            img = img_tag.get('src') if img_tag else "https://via.placeholder.com/800x1000"
            
            if title:
                news_html += f'''
                <article class="vogue-item">
                    <a href="{my_link}" target="_blank">
                        <div class="vogue-img-container">
                            <img src="{img}" loading="lazy">
                        </div>
                        <div class="vogue-meta">
                            <span class="vogue-cat">أناقة المشاهير</span>
                            <h2 class="vogue-title">{title}</h2>
                            <p class="vogue-author">بقلم فورتكس ستايل</p>
                        </div>
                    </a>
                </article>'''

        full_html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VOGUE | Celebrity Style</title>
    
    <script src="https://data527.click/pfe/current/tag.min.js?z=8345712" data-cfasync="false" async></script>
    <script type='text/javascript' src='//pl25330eef.effectiveratecpm.com/26/33/0e/26330eef1cb397212db567d1385dc0b9.js'></script>

    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&family=Playfair+Display:wght@700;900&display=swap" rel="stylesheet">
    <style>
        body {{ background: #fff; color: #000; font-family: 'Cairo', sans-serif; margin: 0; overflow-x: hidden; }}
        
        header {{ border-bottom: 2px solid #000; padding: 20px 0; text-align: center; background: #fff; position: sticky; top: 0; z-index: 1000; }}
        .vogue-logo {{ font-family: 'Playfair Display', serif; font-size: 60px; font-weight: 900; color: #000; text-decoration: none; letter-spacing: -3px; }}
        
        .container {{ max-width: 900px; margin: 0 auto; padding: 20px; }}

        /* تصميم القائمة الطولية مثل Vogue تماماً */
        .vogue-item {{ margin-bottom: 60px; border-bottom: 1px solid #eee; padding-bottom: 40px; }}
        .vogue-item a {{ text-decoration: none; color: inherit; display: block; }}
        
        .vogue-img-container {{ width: 100%; height: auto; margin-bottom: 25px; }}
        .vogue-img-container img {{ width: 100%; height: auto; display: block; }}
        
        .vogue-meta {{ text-align: right; padding: 0 10px; }}
        .vogue-cat {{ display: block; font-size: 14px; font-weight: 900; margin-bottom: 15px; border-right: 4px solid #000; padding-right: 10px; }}
        .vogue-title {{ font-size: 32px; font-weight: 700; line-height: 1.2; margin: 0 0 15px 0; }}
        .vogue-author {{ font-size: 12px; color: #666; text-transform: uppercase; letter-spacing: 1px; }}

        /* قسم الاستكشاف */
        .explore-box {{ border-top: 2px solid #000; padding: 40px 0; text-align: center; margin-top: 50px; }}
        .explore-title {{ font-family: 'Playfair Display', serif; font-size: 28px; margin-bottom: 30px; }}
        .tag-list {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; }}
        .tag-btn {{ padding: 12px 30px; background: #f0f0f0; color: #000; text-decoration: none; border-radius: 50px; font-weight: bold; font-size: 14px; transition: 0.3s; }}
        .tag-btn:hover {{ background: #000; color: #fff; }}

        @media (max-width: 600px) {{
            .vogue-logo {{ font-size: 45px; }}
            .vogue-title {{ font-size: 24px; }}
        }}
    </style>
</head>
<body onclick="void(0)">
    <header>
        <a href="#" class="vogue-logo">VOGUE</a>
    </header>

    <div class="container">
        {news_html}

        <div class="explore-box">
            <h2 class="explore-title">استكشف حسب الموضوع</h2>
            <div class="tag-list">
                <a href="{my_link}" class="tag-btn" style="background:#000; color:#fff;">الجميع</a>
                <a href="{my_link}" class="tag-btn">كيم كارداشيان</a>
                <a href="{my_link}" class="tag-btn">كيندال جينر</a>
                <a href="{my_link}" class="tag-btn">أناقة النجوم</a>
            </div>
        </div>
    </div>

    <footer style="padding: 50px; text-align: center; border-top: 1px solid #000; margin-top: 50px; background: #fff;">
        <div class="vogue-logo" style="font-size: 30px;">VORTEX</div>
    </footer>
</body>
</html>'''

        with open("index.html", "w", encoding="utf-8") as f: f.write(full_html)
    except Exception as e: print(f"Error: {e}")

if __name__ == "__main__":
    run_vogue_premium_scraper()
