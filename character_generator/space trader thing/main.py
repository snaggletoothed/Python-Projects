import pandas as pd
new_haven = ('NEW_HAVEN.ods')
dfinventory = pd.read_excel(new_haven,sheet_name='Inventory')
dfdrug_pricing = pd.read_excel(new_haven,sheet_name='Drug Pricing')
dfcityStateDistances = pd.read_excel(new_haven,sheet_name='City State Distances')#.to_string(index=False)
dfcity_States = pd.read_excel(new_haven,sheet_name='City States')


