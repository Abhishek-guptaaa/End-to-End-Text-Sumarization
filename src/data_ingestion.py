import os
from datasets import load_dataset
import pandas as pd
from config.config import Config

def load_data():
    dataset = load_dataset('abisee/cnn_dailymail', '3.0.0')
    return dataset

def save_data(dataset, split, file_path):
    df = pd.DataFrame(dataset[split])
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    os.makedirs(Config.RAW_DATA_PATH, exist_ok=True)

    dataset = load_data()
    save_data(dataset, 'train', os.path.join(Config.RAW_DATA_PATH, 'train.csv'))
    save_data(dataset, 'validation', os.path.join(Config.RAW_DATA_PATH, 'validation.csv'))
    save_data(dataset, 'test', os.path.join(Config.RAW_DATA_PATH, 'test.csv'))

