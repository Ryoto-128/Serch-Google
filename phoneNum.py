import time
import multiprocessing
from multiprocessing import Pool

from modules.fileIO import Csv
from modules.serchGoogle import PhoneNumber

# 定数
input_path = './phoneNum_inputFile/main.csv'
read_row = [0, 1 ,2]
target_row = 1
other_write_row = [0,1,2]
output_path = './address_inputFile/main.csv'


if __name__ == '__main__':
    # csvの読み込み
    csv = Csv()
    contents = csv.readCsv(input_path, read_row)
    
    # 検索
    phoneNumber = PhoneNumber()
    resolt_contents = phoneNumber.serchPhoneNum(contents, target_row, other_write_row)
    
    # 出力
    csv.addContents(output_path, resolt_contents)