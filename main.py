from scraper import ViennaScraper

MY_API_KEY = "AIzaSyBHc4PCRfBadjIhcCMV-vstDlCN-bPZ9pA"

def start_project():
    print("--- 🚀 جاري بدء مشروع فيينا الرقمي ---")
    try:
        scraper = ViennaScraper(MY_API_KEY)
        print("🔍 جاري البحث عن عيادات في فيينا...")
        results = scraper.get_vienna_clinics()
        
        print(f"\n✅ تم العثور على {len(results)} عيادات:")
        for clinic in results:
            print(f"📍 {clinic['Name']} - التقييم: {clinic['Rating']}")
            
    except Exception as e:
        print(f"❌ حدث خطأ: {e}")

if __name__ == "__main__":
    start_project()