# netPhishing

Açık kaynak kodlu phishing aracı. Bu araç, eğitim ve test amaçlı geliştirilmiştir. Kötüye kullanımından doğacak yasal sorumluluk kullanıcıya aittir.

## ⚠️ Uyarı

Bu araç yalnızca eğitim ve test amaçlı kullanılmalıdır. Kötüye kullanımı yasal sonuçlar doğurabilir. Geliştirici, bu aracın kötüye kullanımından sorumlu değildir.

## 🔧 Kurulum

Termux üzerinde kurulumu için aşağıdaki adımları izleyin:

```bash
# Termux'u güncelleyin
pkg update && pkg upgrade -y

# Gerekli paketleri yükleyin
pkg install git python -y

# Projeyi klonlayın
git clone https://github.com/yuniss60/netPhishing.git

# Tool dizinine geçin
cd netPhishing

# Gerekli Python bağımlılıklarını yükleyin
pip install colorama pyfiglet

# Toolu çalıştırın
python netPhishing.py
