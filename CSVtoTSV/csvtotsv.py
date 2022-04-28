import pandas as pd
import csv

def main():
  file_path = "./"
  # Add the header do we need 
  header_list = ['S.No', 'IP_Addr']
  with_open( file_path + 'data.tsv', 'w') as file:
    # Along with the function DictonaryWriter use a space in the header_list component
    dw = csv.DictWriter(file, delimeter=' ', fieldnames=header_list)
    # It will write the header in the file
    dw.writeheader()
    df = pd.read_csv(file_path + r'Filename.csv')
    df.to_csv(file_path + 'data.tsv', sep='\t', index=False, escapechar='\n')

if __name__ == "__main__":
  main()
