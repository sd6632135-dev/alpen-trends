import requests
from bs4 import BeautifulSoup

def amazon_bestsellers():
    # الرابط الخاص بالمنتجات الأكثر مبيعاً في أمازون ألمانيا
    url = "https://www.amazon.de/gp/bestsellers/?ref_=nav_cs_bestsellers"
    
    # تعريف المتصفح لأمازون (عشان ما يحظرك)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "de-DE,de;q=0.9"
    }

    print("جاري البحث عن المنتجات الترند في ألمانيا والنمسا... انتظر لحظة.")
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        
        # استخراج أسماء المنتجات (هذا الكود يبحث عن العناوين تحديداً)
        titles = soup.find_all("div", {"class": "_cDEzb_p13n-sc-css-line-clamp-3_g30p1"})
        
        if not titles:
            print("لم أتمكن من سحب الأسماء، قد يكون أمازون غير واجهة الصفحة. جرب يدوياً.")
            return

        print("\n🔥 أهم 10 منتجات ترند الآن 🔥")
        print("-" * 30)
        for i, title in enumerate(titles[:10], 1):
            print(f"{i}. {title.get_text()}")
            
    except Exception as e:
        print(f"حدث خطأ: {e}")

if __name__ == "__main__":
    amazon_bestsellers()