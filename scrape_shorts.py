import os
import csv
import sys
from yt_dlp import YoutubeDL

def scrape_youtube_shorts(channel_url, max_videos=0):
    print(f"Memulai Divisi Riset untuk kanal: {channel_url}")
    if max_videos > 0:
        print(f"Mode Uji Coba: Membatasi hanya {max_videos} video teratas.")
    else:
        print("Mode Penuh: Menarik seluruh video dari kanal.")
    
    ydl_opts = {
        'extract_flat': True,
        'skip_download': True,
        'ignoreerrors': True,
    }

    video_data = []

    with YoutubeDL(ydl_opts) as ydl:
        try:
            result = ydl.extract_info(channel_url, download=False)
            if 'entries' in result:
                for entry in result['entries']:
                    if entry:
                        video_id = entry.get('id')
                        title = entry.get('title', 'Tanpa Caption')
                        if video_id:
                            url = f"https://www.youtube.com/shorts/{video_id}"
                            video_data.append([url, title])
                            
                            # Batasi jika max_videos diisi dan sudah tercapai
                            if max_videos > 0 and len(video_data) >= max_videos:
                                break
        except Exception as e:
            print(f"Terjadi kendala saat scraping: {e}")

    # Simpan hasil ke file CSV
    csv_filename = 'data_youtube_shorts.csv'
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Link_Video', 'Caption'])
        writer.writerows(video_data)
        
    print(f"Berhasil! {len(video_data)} data Shorts berhasil disimpan ke {csv_filename}")

if __name__ == "__main__":
    target_url = sys.argv[1] if len(sys.argv) > 1 else "https://www.youtube.com/@Nostalgiback/shorts"
    
    # Menangkap parameter jumlah dari input Actions
    limit = 0
    if len(sys.argv) > 2 and sys.argv[2].strip():
        try:
            limit = int(sys.argv[2])
        except ValueError:
            limit = 0
            
    scrape_youtube_shorts(target_url, limit)
