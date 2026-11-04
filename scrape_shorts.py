import os
import csv
from yt_dlp import YoutubeDL

def scrape_youtube_shorts(channel_url):
    print(f"Memulai Divisi Riset untuk kanal: {channel_url}")
    
    # Pengaturan yt-dlp khusus untuk mengambil metadata Shorts tanpa mendownload video fisik
    ydl_opts = {
        'extract_flat': True,  # Hanya mengambil data/link daftar video
        'skip_download': True,
    }

    video_data = []

    with YoutubeDL(ydl_opts) as ydl:
        try:
            result = ydl.extract_info(channel_url, download=False)
            if 'entries' in result:
                for entry in result['entries']:
                    video_id = entry.get('id')
                    title = entry.get('title', 'Tanpa Caption')
                    # Format URL YouTube Shorts standar
                    url = f"https://www.youtube.com/shorts/{video_id}"
                    
                    video_data.append([url, title])
        except Exception as e:
            print(f"Terjadi kendala saat scraping: {e}")

    # Simpan hasil ke file CSV agar bisa ditarik oleh divisi berikutnya
    csv_filename = 'data_youtube_shorts.csv'
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Link_Video', 'Caption'])  # Header kolom
        writer.writerows(video_data)
        
    print(f"Berhasil! {len(video_data)} data Shorts berhasil disimpan ke {csv_filename}")

if __name__ == "__main__":
    # Target kanal YouTube Shorts perusahaan
    target_url = "https://www.youtube.com/@fifa/shorts"
    scrape_youtube_shorts(target_url)
