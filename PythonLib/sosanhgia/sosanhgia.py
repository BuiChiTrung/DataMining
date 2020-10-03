import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import json

def create_dataframe():
    with open ('/home/straw/Data_mining/Technical_Tutorial/Pandas_Matplotlib/sosanhgia/sosanhgia.csv', 'r') as file:
        data_file = file.readlines()
    
    row_list = []
    for line in data_file:
        # convert str to dict
        product = json.loads(line)

        # bỏ các list đi ko 1 product sẽ ra nhiều dòng 
        if 'category' in product:
            product['category'] = product['category'][0]
        
        # tạo list các dict để nhét vào DF cùng lúc cho nhanh (gấp 10 concat từng df một)
        row_list.append(product)

    return pd.DataFrame(row_list)


def category_statistic(products):
    group_by_category = products.groupby('category')

    category = group_by_category.sum().index
    num = group_by_category.sum()['num_of_product']

    print(category, num)

def main():
    products = create_dataframe()
    category_statistic(products)
    #print(products)

if __name__ == "__main__":
    main()