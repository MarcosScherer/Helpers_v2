import pandas as pd
import os
import glob
import shutil


class Helpers():
    def __init__(self):
        pass
    
    def agrupaEx(root_path, final_path):
        #Roth_path é uma pasta contendo os arquivos em excel
        #final_path é o caminho para salva o arquivo excel inclusive com seu nome

        dfs = []
        # Loop through each file in the directory
        for filename in os.listdir(root_path):
            if filename.endswith('.xlsx') or filename.endswith('.xls'):
                # Construct full file path
                file_path = os.path.join(root_path, filename)
                
                # Read the Excel file into a DataFrame
                df = pd.read_excel(file_path, index_col=0)
                
                # Append the DataFrame to the list
                dfs.append(df)

        # Concatenate all DataFrames in the list into a single DataFrame
        combined_df = pd.concat(dfs, ignore_index=True)

        # Display the combined DataF
        combined_df.to_excel(final_path)


    def delete_all_contents(folder_path):
        # Loop through the contents of the directory
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.remove(file_path)  # Remove the file or link
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)  # Remove the directory and its contents
            except Exception as e:
                pass  # Handle errors silently

    """def plan_grades(path_origin,path_destiny):
        
        # Selecione apenas as duas colunas desejadas
        df = pd.read_excel(path_origin)
        df_selected = df[['Corretor', 'Inspetor de producao']]

        # Remova as linhas duplicadas
        df_selected = df_selected.drop_duplicates()
        df_selected = df_selected.reset_index(drop=True)
        df_selected.to_excel(path_destiny)"""










