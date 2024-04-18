import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_Suits_episodes'

tables = pd.read_html(url)
merged_table = pd.DataFrame()

for i, table_df in enumerate(tables):
    filename = f'tables/table_{i+1}.csv'

    # Those tables are of no use
    if i+1 in [11, 12, 15]:
        print(f"Skipping saving Table {i+1}")
        continue

    # Merge tables 2 to 10
    if 0 < i < 11:
        # Remove the header row
        table_df = table_df[0:]
        
        # Add a column for the season number
        table_df.loc[:, 'Season'] = i 
        
        # Concatenate the table with the merged DataFrame
        merged_table = pd.concat([merged_table, table_df], ignore_index=True)
    else:  
        table_df.to_csv(filename, index=False)
        print(f"Table {i+1} saved as {filename}")

merged_table.to_csv('tables/merged_table.csv', index=False)
print("Merged table saved as tables/seasons.csv")

