import numpy as np
import pandas as pd

def load_and_clean_data(file_path="laptop_data.csv"):
    # 1. Load Data
    df = pd.read_csv(file_path, encoding='latin-1')
    
    # Unnamed Columns අයින් කිරීම
    unnamed_cols = [col for col in df.columns if 'Unnamed' in col]
    if unnamed_cols:
        df.drop(columns=unnamed_cols, inplace=True)
        
    # Duplicates අයින් කිරීම
    df.drop_duplicates(inplace=True)

    # 2. RAM Column Clean කිරීම (Number එකක් කරගැනීම)
    # Ex: '8 GB' or '8GB' or 8
    df['Ram'] = df['Ram'].astype(str).str.extract(r'(\d+)').astype('int32')

    # 3. Storage (ROM) Capacity Clean කිරීම
    df['ROM'] = df['ROM'].astype(str).str.extract(r'(\d+)').astype('int32')

    # 4. Processor / CPU Brand වෙන් කරගැනීම
    def fetch_processor(text):
        text = str(text)
        if 'i7' in text:
            return 'Intel Core i7'
        elif 'i5' in text:
            return 'Intel Core i5'
        elif 'i3' in text:
            return 'Intel Core i3'
        elif 'Ryzen' in text:
            return 'AMD Ryzen Processor'
        elif 'Intel' in text:
            return 'Other Intel Processor'
        elif 'AMD' in text:
            return 'Other AMD Processor'
        else:
            return 'Other Processor'

    df['Cpu brand'] = df['processor'].apply(fetch_processor)

    # 5. GPU Brand වෙන් කරගැනීම
    def fetch_gpu(text):
        text = str(text)
        if 'Nvidia' in text or 'GeForce' in text or 'RTX' in text or 'GTX' in text:
            return 'Nvidia'
        elif 'AMD' in text or 'Radeon' in text:
            return 'AMD'
        elif 'Intel' in text or 'Iris' in text or 'UHD' in text:
            return 'Intel'
        else:
            return 'Other'

    df['Gpu brand'] = df['GPU'].apply(fetch_gpu)

    # 6. OS Simplified කිරීම
    def cat_os(inp):
        inp = str(inp)
        if 'Windows' in inp:
            return 'Windows'
        elif 'Mac' in inp or 'macOS' in inp:
            return 'Mac'
        elif 'Chrome' in inp:
            return 'Chrome OS'
        else:
            return 'Others/Linux'

    df['os'] = df['OS'].apply(cat_os)

    # 7. අනවශ්‍ය Columns අයින් කිරීම
    cols_to_drop = ['name', 'processor', 'CPU', 'GPU', 'OS']
    df.drop(columns=[col for col in cols_to_drop if col in df.columns], inplace=True)

    # Price එක Target variable එක ලෙස තබාගැනීම
    return df

if __name__ == "__main__":
    cleaned_df = load_and_clean_data()
    print("Data Cleaned Successfully!")
    print(cleaned_df.head())