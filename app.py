from flask import Flask, jsonify, request
import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt

class MyApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.add_url_rule('/', view_func=self.index)
        self.df = None

    def run(self):
        self.app.run(debug=True)

    def index(self):
        return jsonify({'message': 'Hello, World!'})

    def importDataset(self):
        try:
           filename = 'C:/Users/Linuxbean/Music/leadgen/leadgendata.csv'
           f2 = 'C:/Users/Linuxbean/Music/leadgen/Latest samples for checking.csv'
           # f2 = 'C:/Users/Nigel Portley/Desktop/Masters/ACode/BICS LG/Positives - Machine Learning.csv'
           for files in glob.glob(filename):
               with open(files) as filename:
                   df = pd.read_csv(files)
                   self.df = df
                   print(self.df.columns)
           for files in glob.glob(f2):
               with open(files) as f2:
                   df_trial = pd.read_csv(files)
           return "imported Dataset successfully"

        except Exception as e:
            return f"{e}"

    def processEncodeCategoricalData(self):
        if self.df is None:
            return "no data to process"
        try:
            #save original dataset
            df_original = self.df

            self.df.drop('Website', axis=1, inplace=True)
            self.df.drop('Comment', axis=1, inplace=True)
            self.df.drop('Salesforce Status', axis=1, inplace=True)
            self.df.tail()
            self.df_trial.drop('Website', axis=1, inplace=True)
            self.df_trial.drop('Comment', axis=1, inplace=True)
            self.df_trial.drop('Salesforce Status', axis=1, inplace=True)

            pd.set_option('display.max_rows', None)
            pd.set_option('display.max_columns', None)
            pd.set_option('display.width', None)
            # pd.set_option('display.max_colwidth', -1)
            cat_cols = self.df.select_dtypes(include=object).columns.tolist()
            (pd.DataFrame(
                self.df[cat_cols]
                .melt(var_name='column', value_name='value')
                .value_counts())
             .rename(columns={0: 'counts'})
             .sort_values(by=['column', 'counts']))

            # Encode Ordinal Categorical Atrributes
            # Create a mapper
            print("scaler mapper")
            scale_mapper = {
                "Negative": 0,
                "Neutral": 0.33,
                "Moderate": 0.67,
                "High": 1
            }

            scale_mapper_company_size = {
                "0-50": 0,
                "51-200": 0.17,
                "201-500": 0.33,
                "501-1000": 0.5,
                "1001-5000": 0.67,
                "5001-10000": 0.84,
                "10001+": 1
            }

            yesno_mapper = {
                "Yes": 1,
                "No": 0
            }

            yesnomaybe_mapper = {
                "Yes": 1,
                "Maybe": 0.5,
                "No": 0
            }

            print("enhance first dataset")
            #first dataset
            self.df['Buyer Interest'] = self.df['Buyer Interest'].replace(scale_mapper)
            self.df['Company Size'] = self.df['Company Size'].replace(scale_mapper_company_size)

            self.df['Aviation'] = self.df['Aviation'].replace(yesno_mapper)
            self.df['Automotive'] = self.df['Automotive'].replace(yesno_mapper)
            self.df['Agriculture'] = self.df['Agriculture'].replace(yesno_mapper)
            self.df['Banking/Finance/Insurance'] = self.df['Banking/Finance/Insurance'].replace(yesno_mapper)
            self.df['Construction'] = self.df['Construction'].replace(yesno_mapper)
            self.df['Chemicals/Life Sciences'] = self.df['Chemicals/Life Sciences'].replace(yesno_mapper)
            self.df['Education'] = self.df['Education'].replace(yesno_mapper)
            self.df['Energy/Utilities'] = self.df['Energy/Utilities'].replace(yesno_mapper)
            self.df['Defense/Security'] = self.df['Defense/Security'].replace(yesno_mapper)
            self.df['Government'] = self.df['Government'].replace(yesno_mapper)
            self.df['Health'] = self.df['Health'].replace(yesno_mapper)
            self.df['Hospitality'] = self.df['Hospitality'].replace(yesno_mapper)
            self.df['Logistics'] = self.df['Logistics'].replace(yesno_mapper)
            self.df['Manufacturing'] = self.df['Manufacturing'].replace(yesno_mapper)
            self.df['Media/Entertainment'] = self.df['Media/Entertainment'].replace(yesno_mapper)
            self.df['Public Sector'] = self.df['Public Sector'].replace(yesno_mapper)
            self.df['Retail and eCommerce'] = self.df['Retail and eCommerce'].replace(yesno_mapper)
            self.df['Transport'] = self.df['Transport'].replace(yesno_mapper)
            self.df['Travel'] = self.df['Travel'].replace(yesno_mapper)
            self.df['Telecommunications'] = self.df['Telecommunications'].replace(yesno_mapper)
            self.df['Personal Contact'] = self.df['Personal Contact'].replace(yesnomaybe_mapper)
            self.df['Conference'] = self.df['Conference'].replace(yesnomaybe_mapper)
            self.df['Company Size'] = self.df['Company Size'].replace(yesno_mapper)
            self.df['North America'] = self.df['North America'].replace(yesno_mapper)
            self.df['LATAM'] = self.df['LATAM'].replace(yesno_mapper)
            self.df['UK'] = self.df['UK'].replace(yesno_mapper)
            self.df['Europe'] = self.df['Europe'].replace(yesno_mapper)
            self.df['MEA'] = self.df['MEA'].replace(yesno_mapper)
            self.df['APAC'] = self.df['APAC'].replace(yesno_mapper)
            self.df['Lead became Opportunity'] = self.df['Lead became Opportunity'].replace(yesno_mapper)
            self.df.tail()

            print("enhance 2nd dataset")
            #2nd dataset
            self.df_trial['Buyer Interest'] = self.df_trial['Buyer Interest'].replace(scale_mapper)
            self.df_trial['Company Size'] = self.df_trial['Company Size'].replace(scale_mapper_company_size)
            self.df_trial['Aviation'] = self.df_trial['Aviation'].replace(yesno_mapper)
            self.df_trial['Automotive'] = self.df_trial['Automotive'].replace(yesno_mapper)
            self.df_trial['Agriculture'] = self.df_trial['Agriculture'].replace(yesno_mapper)
            self.df_trial['Banking/Finance/Insurance'] = self.df_trial['Banking/Finance/Insurance'].replace(yesno_mapper)
            self.df_trial['Construction'] = self.df_trial['Construction'].replace(yesno_mapper)
            self.df_trial['Chemicals/Life Sciences'] = self.df_trial['Chemicals/Life Sciences'].replace(yesno_mapper)
            self.df_trial['Education'] = self.df_trial['Education'].replace(yesno_mapper)
            self.df_trial['Energy/Utilities'] = self.df_trial['Energy/Utilities'].replace(yesno_mapper)
            self.df_trial['Defense/Security'] = self.df_trial['Defense/Security'].replace(yesno_mapper)
            self.df_trial['Government'] = self.df_trial['Government'].replace(yesno_mapper)
            self.df_trial['Health'] = self.df_trial['Health'].replace(yesno_mapper)
            self.df_trial['Hospitality'] = self.df_trial['Hospitality'].replace(yesno_mapper)
            self.df_trial['Logistics'] = self.df_trial['Logistics'].replace(yesno_mapper)
            self.df_trial['Manufacturing'] = self.df_trial['Manufacturing'].replace(yesno_mapper)
            self.df_trial['Media/Entertainment'] = self.df_trial['Media/Entertainment'].replace(yesno_mapper)
            self.df_trial['Public Sector'] = self.df_trial['Public Sector'].replace(yesno_mapper)
            self.df_trial['Retail and eCommerce'] = self.df_trial['Retail and eCommerce'].replace(yesno_mapper)
            self.df_trial['Transport'] = self.df_trial['Transport'].replace(yesno_mapper)
            self.df_trial['Travel'] = self.df_trial['Travel'].replace(yesno_mapper)
            self.df_trial['Telecommunications'] = self.df_trial['Telecommunications'].replace(yesno_mapper)
            self.df_trial['Personal Contact'] = self.df_trial['Personal Contact'].replace(yesnomaybe_mapper)
            self.df_trial['Conference'] = self.df_trial['Conference'].replace(yesnomaybe_mapper)
            self.df_trial['Company Size'] = self.df_trial['Company Size'].replace(yesno_mapper)
            self.df_trial['North America'] = self.df_trial['North America'].replace(yesno_mapper)
            self.df_trial['LATAM'] = self.df_trial['LATAM'].replace(yesno_mapper)
            self.df_trial['UK'] = self.df_trial['UK'].replace(yesno_mapper)
            self.df_trial['Europe'] = self.df_trial['Europe'].replace(yesno_mapper)
            self.df_trial['MEA'] = self.df_trial['MEA'].replace(yesno_mapper)
            self.df_trial['APAC'] = self.df_trial['APAC'].replace(yesno_mapper)
            self.df_trial['Lead became Opportunity'] = self.df_trial['Lead became Opportunity'].replace(yesno_mapper)

            return "ProcessedandEncodedCategoricalData"

        except Exception as e:
            return f"{e}"



# app = MyApp()
# app.app.add_url_rule('/square', view_func=app.square)
# app.app.add_url_rule('/cube',view_func=app.cube)
app.app.add_url_rule('/importDataset',view_func=app.importDataset)
app.app.add_url_rule('/proceesEncodedCategoricalData',view_func=app.processEncodeCategoricalData)

# if __name__ == '__main__':
#     app.run()



