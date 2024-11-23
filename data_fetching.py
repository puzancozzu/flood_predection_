import pandas as pd
from scraping_data import read_csv


# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #

# This function is to clean the scrap and adding other columns with mean from train set

def create_df():
    columns = [
    "TopographyDrainage",
    "RiverManagement",
    "Deforestation",
    "Urbanization",
    "ClimateChange",
    "DamsQuality",
    "Siltation",
    "AgriculturalPractices",
    "Encroachments",
    "IneffectiveDisasterPreparedness",
    "DrainageSystems",
    "CoastalVulnerability",
    "Landslides",
    "Watersheds",
    "DeterioratingInfrastructure",
    "PopulationScore",
    "WetlandLoss",
    "InadequatePlanning",
    "PoliticalFactors"]

    df_rainfall = read_csv("data/rainfall_scrap.csv")

    df_rainfall = df_rainfall.drop(columns=[df_rainfall.columns[-1]])


    # droping the columns I dont want
    col_to_drop = ["S.No.", "Station Index", "Station Name"]
    df_rainfall = df_rainfall.drop(columns=col_to_drop, axis=1)
   

    # df_rainfall = df_rainfall.drop(columns=[df_rainfall.columns[], 
    #                                     df_rainfall.columns[2],  
    #                                     df_rainfall.columns[3]])
    

    df_rainfall.columns.values[2:7] = ['1hr', '3hr', '6hr', '12hr', '24hr']

    columns_to_consider = ['1hr', '3hr', '6hr', '12hr', '24hr']

    def calculate_mean(row):
        valid_values = [val for val in row[columns_to_consider] if val != 0]
    
        if valid_values:
            return sum(valid_values) / len(valid_values)
        else:
            return None 

    df_rainfall['MonsoonIntensity'] = df_rainfall.apply(calculate_mean, axis=1)
    

    col_to_drop = ["1hr",  "3hr",  "6hr",  "12hr",   "24hr"]
    df_rainfall = df_rainfall.drop(columns=col_to_drop, axis=1)
    # print(df_rainfall.head())

    df_rainfall['MonsoonIntensity'] = df_rainfall['MonsoonIntensity'].fillna(0)
    df_rainfall["MonsoonIntensity"] = df_rainfall["MonsoonIntensity"].round().astype(int)

    default_value = round(4.927)
    output_path = "data/final_rainfall_data.csv"
    df_rainfall.to_csv(output_path, index=False)

    # Adding the columnns we desired and saving the table
    for column in columns:
        df_rainfall[column] = default_value
    # print(df_rainfall.head())

    return df_rainfall


# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #

def data_to_model(df_rain):
    col_to_drop = ["Basin Name",  "District"]
    df_rain = df_rain.drop(columns=col_to_drop, axis=1)
    # print(df_rain.head())
    return df_rain


#################### TESTING THE MODULES #####################################
# df_rain = create_df()
# data_test = data_to_model(df_rain)
# print(data_test.head())