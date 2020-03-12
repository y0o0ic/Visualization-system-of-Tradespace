#!/usr/bin/env python

import pandas as pd
import yaml
# pip install azure-storage-file
from azure.storage.file import FileService

def data_download():
    with open('config.yaml', 'r') as yml:
        config = yaml.load(yml)

    account_name = config['account_name']
    key = config['key']
    file_service = FileService(account_name=account_name, account_key=key)

    # ファイルのダウンロード(カレントにそのままダウンロード)
    share_name = 'data'
    dir_name = None
    file_name = 'TradeSpace.csv'
    download_path = 'TradeSpace.csv'
    file_service.get_file_to_path(share_name, dir_name, file_name, download_path)

def TradeSpace():

    data_download()
    df = pd.read_csv("TradeSpace.csv")

    return df    

if __name__ == "__main__":
    data_download()