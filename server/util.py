import json
import pickle
import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings("ignore")

__locations = None
__model = None
__data_columns = 10


def get_price(company, memory, ram, os, size_in_inches):
    # no of inputs = 8
    # c_col = {
    #     'company_'+str(company): 1,
    #     'processor_company_'+str(processor_company): 1,
    #     'processor_cores_'+str(processor_core): 1,
    #     'processor_gen': processor_gen,
    #     'memory': memory,
    #     'ram_in_gb': ram,
    #     'os': os,
    #     'size_in_inches': size_in_inches
    # }
    # x = pd.DataFrame(columns=__data_columns)
    # columns = __data_columns
    # # giving value if col present in the dict and is a mem of columns
    # for col in columns:
    #     if col in c_col:
    #         x.loc[0, col] = c_col[col]
    #     else:
    #         x.loc[0, col] = 0

    # return round(__model.predict(x)[0], 2)
    nums = ['company_'+str(company), 'Memory',
            'Ram_in_GB', 'OS', 'size_in_inches']
    values = ['1', memory, ram, os, size_in_inches]
    for i in range(len(nums)):
        nums[i] = nums[i].lower()

    x = np.zeros(len(__data_columns))

    for col in __data_columns:
        loc_index = __data_columns.index(col.lower())
        if col in nums:
            x[loc_index] = values[nums.index(col)]
        else:
            x[loc_index] = 0

    return round(__model.predict([x])[0], 2)


def load_saved_artifacts():
    global __data_columns
    global __locations
    global __model

    with open("server/artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns
    with open("server/artifacts/laptop_price_model.pickle", 'rb') as f:
        __model = pickle.load(f)


def get_location_names():
    return __locations


if __name__ == "__main__":
    load_saved_artifacts()
    # print(get_location_names())
    # print("\n")
    #print(get_estimated_price('MSI', 2, 32, 11, 14))
    # print(get_estimated_price('HP', 2, 32, 11, 14))
    # print(get_estimated_price('Dell', 2, 32, 11, 14))
