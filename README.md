# Veri Kümeleme (Clustering) Kullanım Kılavuzu

Bu Python script'i, veri kümeleme algoritması olan K-Means'i kullanarak belirli bir veri setini analiz etmek ve görselleştirmek için tasarlanmıştır.

## Kullanım

1. **Gereksinimler**

    - Python 3.x
    - pandas
    - matplotlib
    - scikit-learn

    Gerekli kütüphaneleri yüklemek için terminal veya komut istemcisine şu komutu yazabilirsiniz:

    ```bash
    pip install pandas matplotlib scikit-learn
    ```

2. **Veri Seti**

    - Analiz edilecek veri setini belirtmek için `file_path` değişkenini güncelleyin. Varsayılan olarak "Wednesday-workingHours.pcap_ISCX.csv" kullanılmaktadır.

3. **Kodun Çalıştırılması**

    Terminal veya komut istemcisine şu komutu yazarak script'i çalıştırın:

    ```bash
    python script_adi.py
    ```

    veya

    ```bash
    python3 script_adi.py
    ```

4. **Sonuçlar**

    - Script çalıştığında, K-Means kümeleme algoritması ile oluşturulan grafik ekrana getirilecektir. Bu grafik, veri setindeki benzer özelliklere sahip veri noktalarını belirli kümelere ayırarak görselleştirir.

## Örnek Çıktı

![K-Means Clustering](output.png)

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır - Daha fazla bilgi için [LICENSE.md](LICENSE.md) dosyasına bakın.
# CICIDS2017-veri-seti-K-Means
