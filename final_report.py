import pandas as pd, numpy as np

def main():
  df_activity = pd.read_excel("logbook.xlsx", sheet_name="Activity")
  
  df_type = pd.read_excel("logbook.xlsx", sheet_name="Type")
  df_attend_type = df_type.loc[df_type["Notes"] == "Attend"]
  df_do_type = df_type.loc[df_type["Notes"] == "Do"]

  attend_type = list(row["Type"] for _, row in df_attend_type.iterrows())
  do_type = list(row["Type"] for _, row in df_do_type.iterrows())
  
  print("Selama mengikuti program Startup Campus 2024 H1 ini saya mengikuti beberapa attendance mulai:")
  print("\n".join(list(filter(lambda value: value != "", list(dict.fromkeys(list("- {} yang dimana dilakukan secara online pada bagian {}".format(row[i], i) if row[i] is not np.nan else "" for _, row in df_activity.iterrows() for i in attend_type)))))))
  print()
  print("Selama mengikuti program Startup Campus 2024 H1 ini saya mengerjakan beberapa assignment mulai:")
  print("\n".join(list(filter(lambda value: value != "", list(dict.fromkeys(list("- {} yang dimana dilakukan secara online pada bagian {}".format(row[i], i) if row[i] is not np.nan else "" for _, row in df_activity.iterrows() for i in do_type)))))))
  
  print()
  print("=" * 50)
  print()