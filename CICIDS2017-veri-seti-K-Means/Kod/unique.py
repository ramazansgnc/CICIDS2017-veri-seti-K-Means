import pandas as pd

# Veri seti dosyalarının isimleri ve dosya yolları
data_files = {
    "Friday-WorkingHours-Afternoon-DDos.pcap_ISCX": "Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv",
    "Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX": "Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv",
    "Friday-WorkingHours-Morning.pcap_ISCX": "Friday-WorkingHours-Morning.pcap_ISCX.csv",
    "Monday-WorkingHours.pcap_ISCX": "Monday-WorkingHours.pcap_ISCX.csv",
    "Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX": "Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv",
    "Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX": "Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv",
    "Tuesday-WorkingHours.pcap_ISCX": "Tuesday-WorkingHours.pcap_ISCX.csv",
    "Wednesday-workingHours.pcap_ISCX": "Wednesday-workingHours.pcap_ISCX.csv"
}

# Her bir veri seti için unique değerleri ve sayılarını gösterir
for data_file, file_path in data_files.items():
    try:
        df = pd.read_csv(file_path, encoding='latin1', dtype=str)
        
        # NaN içeren sütunları sayar
        nan_columns = df.columns[df.isna().any()].tolist()
        for col in nan_columns:
            nan_count = df[col].isna().sum()
            
        
        # NaN etiketini sayar
        nan_label_count = df['Label'].isna().sum()
        
        
        # NaN etiketi hariç unique label değerleri ve sayılarını gösterir
        df = df.dropna(subset=['Label'])
        unique_labels = df['Label'].unique()
        num_unique_labels = len(unique_labels)
        
        print(f"{data_file} veri setindeki unique label değerleri ve sayıları:")
        for label in unique_labels:
            count = df[df['Label'] == label].shape[0]
            print(f"{label}: {count} adet")
        
        print(f"Toplam unique label sayısı: {num_unique_labels}\n")
    
    except FileNotFoundError:
        print(f"{data_file} veri seti okunurken bir hata oluştu: {file_path} bulunamadı.\n")
    except UnicodeDecodeError:
        print(f"{data_file} veri seti okunurken bir hata oluştu: {file_path} dosyası UTF-8 formatında değil.\n")
    except Exception as e:
        print(f"{data_file} veri seti okunurken bir hata oluştu: {str(e)}\n")
