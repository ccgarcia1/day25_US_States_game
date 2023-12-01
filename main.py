import pandas as pd

data = pd.read_csv("squirrel_count_nyc.csv")
fur_color_cnt = data["Primary Fur Color"].value_counts()

print(fur_color_cnt)
print(type(fur_color_cnt))

result_df = pd.DataFrame({'Fur Color': fur_color_cnt.index, 'Quantity': fur_color_cnt.values})

result_df.to_csv("fur_color_cnt_v2.csv")

#data_dict = data.to_dict()

#print(fur_color_cnt)
