import pandas as pd
import numpy as np
import itertools

top_50_coin_names = pd.read_csv('top_50_coin_names.csv')
market_data = pd.read_csv('market_data.csv')
top_50_coin_names = pd.DataFrame(top_50_coin_names)
market_data = pd.DataFrame(market_data)

# print(market_data.index[market_data['coin'] == 'RPG'].to_list()[0])
# print(market_data['exchange'][1])

# print('BTC' in market_data['coin'].unique())

exchanges = []
for each in top_50_coin_names['coins']:
    if (each in market_data['coin'].unique()):
        index = market_data.index[market_data['coin'] == each].to_list()[0]
        exchanges.append(market_data['exchange'][index])

print(np.shape(exchanges))
exchanges = np.asarray(exchanges)

# print(np.shape(exchanges))


###########这部分把2D Arrary变成1D (array of each coin name (str))#############
######因为正常python iteration这个array得到的是each character，所以这里用了很蠢的方法#############
######理论上这里是所有包含top50%币种(by volume)的exchange了#############
exchange_df = pd.DataFrame({'exchanges': exchanges})

exchange_list = []
for each in exchange_df['exchanges']:
    cur = each.split(',')
    for i in cur:
        j = i.split('\'')
        for k in j:
            if k != "\'":
                exchange_list.append(k)
                # print(k)
    # print(type(cur))
# print(np.shape(exchange_list))
exchange_list = np.delete(exchange_list, np.argwhere(exchange_list == "\'"), axis=0)
exchange_list = np.delete(exchange_list, np.argwhere(exchange_list == "["), axis=0)
exchange_list = np.delete(exchange_list, np.argwhere(exchange_list == "]"), axis=0)
exchange_list = np.delete(exchange_list, np.argwhere(exchange_list == " "), axis=0)
exchange_list = np.delete(exchange_list, np.argwhere(exchange_list == " "), axis=0)

result = []
for each in exchange_list:
    if each not in result:
        result.append(each)
result.pop(1)
pd.DataFrame({'exchanges': result}).to_csv('exchanges.csv')
# exchange_df.to_csv('exchanges.csv')
# pd.DataFrame({'exchanges': new}).to_csv('unique_exchanges.csv')