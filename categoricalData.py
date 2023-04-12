import pandas as pd

def funCategoricalData(df,df_trial):

    #Columns Website, Comment & Salesforce Status
    # Columns with ID numbers or identifiers do not contain useful information are dropped.
    df.drop('Website', axis=1, inplace=True)
    df.drop('Comment', axis=1, inplace=True)
    df.drop('Salesforce Status', axis=1, inplace=True)
    df.tail()
    df_trial.drop('Website', axis=1, inplace=True)
    df_trial.drop('Comment', axis=1, inplace=True)
    df_trial.drop('Salesforce Status', axis=1, inplace=True)

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    # pd.set_option('display.max_colwidth', -1)

    # cat_cols = df.select_dtypes(include=object).columns.tolist()
    # (pd.DataFrame(
    #     df[cat_cols]
    #     .melt(var_name='column', value_name='value')
    #     .value_counts())
    #  .rename(columns={0: 'counts'})
    #  .sort_values(by=['column', 'counts']))

    # Encode Ordinal Categorical Attributes

    # Create a mapper
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

    df['Buyer Interest'] = df['Buyer Interest'].replace(scale_mapper)
    df['Company Size'] = df['Company Size'].replace(scale_mapper_company_size)
    df['Aviation'] = df['Aviation'].replace(yesno_mapper)
    df['Automotive'] = df['Automotive'].replace(yesno_mapper)
    df['Agriculture'] = df['Agriculture'].replace(yesno_mapper)
    df['Banking/Finance/Insurance'] = df['Banking/Finance/Insurance'].replace(yesno_mapper)
    df['Construction'] = df['Construction'].replace(yesno_mapper)
    df['Chemicals/Life Sciences'] = df['Chemicals/Life Sciences'].replace(yesno_mapper)
    df['Education'] = df['Education'].replace(yesno_mapper)
    df['Energy/Utilities'] = df['Energy/Utilities'].replace(yesno_mapper)
    df['Defense/Security'] = df['Defense/Security'].replace(yesno_mapper)
    df['Government'] = df['Government'].replace(yesno_mapper)
    df['Health'] = df['Health'].replace(yesno_mapper)
    df['Hospitality'] = df['Hospitality'].replace(yesno_mapper)
    df['Logistics'] = df['Logistics'].replace(yesno_mapper)
    df['Manufacturing'] = df['Manufacturing'].replace(yesno_mapper)
    df['Media/Entertainment'] = df['Media/Entertainment'].replace(yesno_mapper)
    df['Public Sector'] = df['Public Sector'].replace(yesno_mapper)
    df['Retail and eCommerce'] = df['Retail and eCommerce'].replace(yesno_mapper)
    df['Transport'] = df['Transport'].replace(yesno_mapper)
    df['Travel'] = df['Travel'].replace(yesno_mapper)
    df['Telecommunications'] = df['Telecommunications'].replace(yesno_mapper)
    df['Personal Contact'] = df['Personal Contact'].replace(yesnomaybe_mapper)
    df['Conference'] = df['Conference'].replace(yesnomaybe_mapper)
    df['Company Size'] = df['Company Size'].replace(yesno_mapper)
    df['North America'] = df['North America'].replace(yesno_mapper)
    df['LATAM'] = df['LATAM'].replace(yesno_mapper)
    df['UK'] = df['UK'].replace(yesno_mapper)
    df['Europe'] = df['Europe'].replace(yesno_mapper)
    df['MEA'] = df['MEA'].replace(yesno_mapper)
    df['APAC'] = df['APAC'].replace(yesno_mapper)
    df['Lead became Opportunity'] = df['Lead became Opportunity'].replace(yesno_mapper)

    #for 2nd dataframe
    df_trial['Buyer Interest'] = df_trial['Buyer Interest'].replace(scale_mapper)
    df_trial['Company Size'] = df_trial['Company Size'].replace(scale_mapper_company_size)
    df_trial['Aviation'] = df_trial['Aviation'].replace(yesno_mapper)
    df_trial['Automotive'] = df_trial['Automotive'].replace(yesno_mapper)
    df_trial['Agriculture'] = df_trial['Agriculture'].replace(yesno_mapper)
    df_trial['Banking/Finance/Insurance'] = df_trial['Banking/Finance/Insurance'].replace(yesno_mapper)
    df_trial['Construction'] = df_trial['Construction'].replace(yesno_mapper)
    df_trial['Chemicals/Life Sciences'] = df_trial['Chemicals/Life Sciences'].replace(yesno_mapper)
    df_trial['Education'] = df_trial['Education'].replace(yesno_mapper)
    df_trial['Energy/Utilities'] = df_trial['Energy/Utilities'].replace(yesno_mapper)
    df_trial['Defense/Security'] = df_trial['Defense/Security'].replace(yesno_mapper)
    df_trial['Government'] = df_trial['Government'].replace(yesno_mapper)
    df_trial['Health'] = df_trial['Health'].replace(yesno_mapper)
    df_trial['Hospitality'] = df_trial['Hospitality'].replace(yesno_mapper)
    df_trial['Logistics'] = df_trial['Logistics'].replace(yesno_mapper)
    df_trial['Manufacturing'] = df_trial['Manufacturing'].replace(yesno_mapper)
    df_trial['Media/Entertainment'] = df_trial['Media/Entertainment'].replace(yesno_mapper)
    df_trial['Public Sector'] = df_trial['Public Sector'].replace(yesno_mapper)
    df_trial['Retail and eCommerce'] = df_trial['Retail and eCommerce'].replace(yesno_mapper)
    df_trial['Transport'] = df_trial['Transport'].replace(yesno_mapper)
    df_trial['Travel'] = df_trial['Travel'].replace(yesno_mapper)
    df_trial['Telecommunications'] = df_trial['Telecommunications'].replace(yesno_mapper)
    df_trial['Personal Contact'] = df_trial['Personal Contact'].replace(yesnomaybe_mapper)
    df_trial['Conference'] = df_trial['Conference'].replace(yesnomaybe_mapper)
    df_trial['Company Size'] = df_trial['Company Size'].replace(yesno_mapper)
    df_trial['North America'] = df_trial['North America'].replace(yesno_mapper)
    df_trial['LATAM'] = df_trial['LATAM'].replace(yesno_mapper)
    df_trial['UK'] = df_trial['UK'].replace(yesno_mapper)
    df_trial['Europe'] = df_trial['Europe'].replace(yesno_mapper)
    df_trial['MEA'] = df_trial['MEA'].replace(yesno_mapper)
    df_trial['APAC'] = df_trial['APAC'].replace(yesno_mapper)
    df_trial['Lead became Opportunity'] = df_trial['Lead became Opportunity'].replace(yesno_mapper)

    ########
    pd.set_option('display.max_columns', 100)
    pd.set_option('display.max_rows', 100)
    # first one-hot encode the categorical columns with NaNs

    df = pd.get_dummies(df, columns=['Industry Vertical', 'BICS Product Area'],
                        dummy_na=False,
                        drop_first=False)

    df_trial = pd.get_dummies(df_trial, columns=['Industry Vertical', 'BICS Product Area'],
                              dummy_na=False,
                              drop_first=False)

    ##########
    new_cols = [col for col in df.columns if col != 'Lead became Opportunity'] + ['Lead became Opportunity']
    df = df[new_cols]


    new_cols = [col for col in df_trial.columns if col != 'Lead became Opportunity'] + ['Lead became Opportunity']
    df_trial = df_trial[new_cols]
    return df,df_trial