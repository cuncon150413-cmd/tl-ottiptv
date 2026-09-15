import re
import requests

url = "https://hplus.com.vn/iframe?content_id=2669&w=1000&h=541"

headers = {
    "accept-language": "vi",
    "sec-ch-ua": '"Chromium";v="152", "Not?A_Brand";v="24", "Google Chrome";v="152"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36",
    "referer": "https://sdtv.vn/",
}

response = requests.get(url, headers=headers)
html_content = response.text

# Tìm url .m3u8 trong source HTML / JS
m3u8_links = re.findall(r'(https?://[^\s"\']+\.m3u8[^\s"\']*)', html_content)

if m3u8_links:
    print("🎯 Link M3U8 tìm thấy:")
    for link in set(m3u8_links):
        print(link)
else:
    print("❌ Không tìm thấy trực tiếp, luồng có thể được gọi qua API AJAX.")