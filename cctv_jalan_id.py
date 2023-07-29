
import random
import emoji

cctv_jalan = ['https://atcs.banjarkota.go.id:5443/LiveApp/streams/lapangbakti1.m3u8', 'https://atcs.banjarkota.go.id:5443/LiveApp/streams/cijolang2.m3u8', 'https://atcs.banjarkota.go.id:5443/LiveApp/streams/langensari1.m3u8', 'https://cctvjss.jogjakota.go.id/malioboro/Malioboro_6_Mall_Utara.stream/chunklist_w736238618.m3u8', 'https://cctvjss.jogjakota.go.id/atcs/ATCS_Lampu_Merah_Pingit3.stream/chunklist_w1901748655.m3u8', 'https://cctvjss.jogjakota.go.id/atcs/ATCS_tamansari.stream/chunklist_w168903250.m3u8', 'https://atcs.tasikmalayakota.go.id/camera/tamankota.m3u8', 'https://atcs.tasikmalayakota.go.id/camera/dewisartikaarahmasjidagung.m3u8', 'https://atcs.tasikmalayakota.go.id/camera/mhatta.m3u8', 'http://atcsdishub.pemkomedan.go.id/camera/MULTATULI.m3u8', 'http://atcsdishub.pemkomedan.go.id/camera/IMMANUEL.m3u8', 'http://atcsdishub.pemkomedan.go.id/camera/KRAKATAUPASAR3.m3u8', 'http://103.110.11.24:5080//LiveApp/streams/539172222535992724034741.m3u8', 'http://123.108.103.101/camera/SIMP_PDAM.m3u8', 'http://123.108.103.101/camera/SIMP_JAMBO_TAPE.m3u8', 'http://123.108.103.101/camera/SIMP_JAMBO_TAPE_IV.m3u8', 'http://stream.cctv.malangkota.go.id/WebRTCApp/streams/027277786580967639165024.m3u8']

print(emoji.emojize("code_By n00bX8 :red_heart:", variant="emoji_type"))
print("\033[1;32;40mBeberapa daftar CCTV jalan di Indonesia, : \n")
for i in range(3):
    print(random.choice(cctv_jalan))
     