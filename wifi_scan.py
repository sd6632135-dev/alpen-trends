import subprocess

# هذا الأمر يقوم باستدعاء أداة النظام لرؤية الشبكات
print("--- جاري البحث عن شبكات الوايفاي المحيطة ---")
try:
    # تشغيل أمر النظام لعرض الشبكات
    devices = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])
    devices = devices.decode('ascii', errors='ignore')
    print(devices)
except:
    print("تأكد من تفعيل الوايفاي في جهازك.")

input("\nاضغط Enter للخروج...")
