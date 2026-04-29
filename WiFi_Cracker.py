import time

def start_cracking():
    target_wifi = "Refat" # اسم شبكة أخيك (كمثال)
    # قائمة بكلمات السر الشائعة التي يجربها الهكر
    wordlist = ["12345678", "password", "ahmed123", "11223344", "qwerty"]
    
    print(f"--- جاري محاولة الدخول لشبكة: {target_wifi} ---")
    
    for password in wordlist:
        print(f"جاري تجربة كلمة السر: {password} ...")
        time.sleep(1) # تأخير بسيط ليبدو الفحص حقيقياً
        
        # لنفترض أن كلمة سر أخيك هي '11223344'
        if password == "11223344":
            print("\n[+] تم العثور على كلمة السر بنجاح!")
            print(f"[+] كلمة المرور هي: {password}")
            return
            
    print("\n[-] فشل الهجوم. كلمة السر ليست في القائمة.")

start_cracking()
input("\nاضغط Enter للخروج...")
