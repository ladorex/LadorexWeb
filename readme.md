# WEBLADOREX BİLGİ TOPLAMA ARACI

**WEBLADOREX** aracını kullanarak, çeşitli ağ ve web analizlerini kolayca gerçekleştirebilirsiniz. Bu araç, bir dizi bilgi toplama ve güvenlik tarama işlevine sahiptir. Alan adı sorgulama, DNS bilgisi alımı, IP adresi sorgulama, açık port taraması, web teknolojileri tespiti, site durum kontrolü gibi bir dizi özellik içerir.

## Özellikler

- **DNS Bilgisi**: Alan adı üzerinden DNS sunucularını sorgulama.
- **IP Adresi ve Lokasyon**: Alan adı üzerinden IP adresi ve konum bilgilerini sorgulama.
- **Web Teknolojileri**: Web sitesinin kullandığı CMS (örneğin WordPress, Joomla vb.) hakkında bilgi toplama.
- **Robots.txt & Sitemap**: Web sitesinin robots.txt ve sitemap.xml dosyalarını kontrol etme.
- **Güvenlik Tarama**: Belirli bir alan adı üzerindeki açık portları tarayarak güvenlik taraması yapma.
- **IP Sorgulama**: IP adresi sorgulama ve IP'nin bağlı olduğu yer hakkında bilgi edinme.
- **Rastgele IP Üretme**: Rastgele bir IP adresi oluşturma.
- **Rastgele User-Agent Üretme**: Rastgele bir User-Agent başlığı oluşturma.
- **Site Durum Kontrolü**: Belirtilen bir web sitesinin çalışıp çalışmadığını kontrol etme.
- **Site Ekran Görüntüsü Alma**: Web sitesinin ekran görüntüsünü alıp kaydetme.
- **Master Komutu**: Herşeyin Oldugu komut.

## Kullanım

### Gereksinimler
- Python 3.x
- Gerekli Python kütüphaneleri:
  - `requests`
  - `nmap`
  - `beautifulsoup4`
  - `selenium`
  - `whois`
  
Kurulum için terminal veya komut istemcisinde şu komutu çalıştırabilirsiniz:

```bash
pip install requests nmap beautifulsoup4 selenium whois
