import requests
from bs4 import BeautifulSoup
from datetime import datetime

def run_vogue_stable_scraper():
    # نستخدم رابط سيدتي المستقر لضمان ظهور الأخبار مثل RT
    rss_url = "https://www.sayidaty.net/taxonomy/term/31/rss.xml"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    try:
        my_link = "https://data527.click/21330bf1d025d41336e6/4ba0cfe12d/?placementName=default"
        
        response = requests.get(rss_url, headers=headers, timeout=20)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.content, 'xml')
        items = soup.find_all('item')
        
        news_html = ""
        for item in items[:10]:
            title = item.title.text
            img = item.find('enclosure').get('url') if item.find('enclosure') else "https://via.placeholder.com/800x1000"
            
            news_html += f'''
            <article class="vogue-item">
                <a href="{my_link}" target="_blank">
                    <div class="vogue-img-container">
                        <img src="{img}" loading="lazy">
                    </div>
                    <div class="vogue-meta">
                        <span class="vogue-cat">VOGUE CELEBRITY</span>
                        <h2 class="vogue-title">{title}</h2>
                        <p class="vogue-author">بواسطة فورتكس ستايل</p>
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
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&family=Playfair+Display:wght@900&display=swap" rel="stylesheet">
    <style>
        body {{ background: #fff; color: #000; font-family: 'Cairo', sans-serif; margin: 0; }}
        header {{ border-bottom: 2px solid #000; padding: 20px 0; text-align: center; position: sticky; top: 0; background: #fff; z-index: 1000; }}
        .vogue-logo {{ font-family: 'Playfair Display', serif; font-size: 60px; color: #000; text-decoration: none; letter-spacing: -3px; }}
        .container {{ max-width: 900px; margin: 0 auto; padding: 20px; }}
        .vogue-item {{ margin-bottom: 60px; border-bottom: 1px solid #eee; padding-bottom: 40px; }}
        .vogue-item a {{ text-decoration: none; color: inherit; }}
        .vogue-img-container {{ width: 100%; margin-bottom: 25px; }}
        .vogue-img-container img {{ width: 100%; height: auto; display: block; }}
        .vogue-title {{ font-size: 32px; font-weight: 700; line-height: 1.2; margin: 15px 0; }}
        .vogue-cat {{ font-weight: 900; border-right: 4px solid #000; padding-right: 10px; font-size: 14px; }}
    </style>
</head>
<body onclick="void(0)">
    <header><a href="#" class="vogue-logo">VOGUE</a></header>
    <div class="container">
        {news_html}
    </div>
</body>
</html>'''

        with open("index.html", "w", encoding="utf-8") as f: f.write(full_html)
    except Exception as e: print(f"Error: {e}")

if __name__ == "__main__":
    run_vogue_stable_scraper()
