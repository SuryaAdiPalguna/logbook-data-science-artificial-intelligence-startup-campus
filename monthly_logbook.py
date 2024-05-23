import pandas as pd, numpy as np

def main():
  month = int(input("Masukkan Bulan: "))

  df_activity = pd.read_excel("logbook.xlsx", sheet_name="Activity")
  df_month_activity = df_activity.loc[df_activity["Month"] == month]
  df_type = pd.read_excel("logbook.xlsx", sheet_name="Type")

  df_question_1_type = df_type.loc[df_type["Question 1"] == True]
  df_question_2_type = df_type.loc[df_type["Question 2"] == True]
  df_question_3_type = df_type.loc[df_type["Question 3"] == True]
  df_question_4_type = df_type.loc[df_type["Question 4"] == True]

  df_attend_type = df_type.loc[df_type["Notes"] == "Attend"]
  df_do_type = df_type.loc[df_type["Notes"] == "Do"]

  question_1_type = list(row["Type"] for _, row in df_question_1_type.iterrows())
  question_2_type = list(row["Type"] for _, row in df_question_2_type.iterrows())
  question_3_type = list(row["Type"] for _, row in df_question_3_type.iterrows())
  question_4_type = list(row["Type"] for _, row in df_question_4_type.iterrows())

  attend_type = list(row["Type"] for _, row in df_attend_type.iterrows())
  do_type = list(row["Type"] for _, row in df_do_type.iterrows())

  print()
  print("=" * 50)
  print()

  if month != 5:
    print("1. Bagaimana aktivitas mentoring dan koordinasi dengan Mentor & DPP?")
    print("Saya mengikuti:")
    print("\n".join(list(("- {} pada {}".format(" &&& ".join(list(dict.fromkeys(list(filter(lambda value: value is not np.nan, list(df_month_activity[i])))))), i)) for i in question_1_type)))
    print()
    print("2. Apa yang telah kamu kerjakan dan bagaimana perkembangannya?")
    print("Saya mengerjakan:")
    print("\n".join(list(("- {} pada {}".format(" &&& ".join(list(dict.fromkeys(list(filter(lambda value: value is not np.nan, list(df_month_activity[i])))))), i)) for i in question_2_type)))
    print()
    print("3. Tantangan apa yang dihadapi dan berikan alternatif solusi untuk menghadapinya?")
    print("Saya menghadapi:")
    print("\n".join(list(("- {} pada {}".format(" &&& ".join(list(dict.fromkeys(list(filter(lambda value: value is not np.nan, list(df_month_activity[i])))))), i)) for i in question_3_type)))
    print()
    print("4. Apa saja dan jelaskan pengembangan kompetensi yang telah didapat?")
    print("Saya mengembangkan:")
    print("\n".join(list(("- {} pada {}".format(" &&& ".join(list(dict.fromkeys(list(filter(lambda value: value is not np.nan, list(df_month_activity[i])))))), i)) for i in question_4_type)))
  else:
    print("1. Bagaimana aktivitas mentoring dan koordinasi dengan Mentor & DPP?")
    print("Bulan ini selama program ini saya mengikuti beberapa aktivitas mulai:")
    print("\n".join(list(filter(lambda value: value != "", list(dict.fromkeys(list("- {} yang dimana dilakukan secara online pada bagian {}".format(row[i], i) if row[i] is not np.nan else "" for _, row in df_month_activity.iterrows() for i in question_1_type)))))))
    print()
    print("2. Apa yang telah kamu kerjakan dan bagaimana perkembangannya?")
    print("Bulan ini selama program ini saya mengerjakan beberapa perkembangan mulai:")
    print("\n".join(list(filter(lambda value: value != "", list(dict.fromkeys(list("- {} yang dimana dilakukan secara online pada bagian {}".format(row[i], i) if row[i] is not np.nan else "" for _, row in df_month_activity.iterrows() for i in question_2_type)))))))
    print()
    print("3. Tantangan apa yang dihadapi dan berikan alternatif solusi untuk menghadapinya?")
    print("Bulan ini selama program ini saya menghadapi beberapa tantangan mulai:")
    print("\n".join(list(filter(lambda value: value != "", list(dict.fromkeys(list("- {} yang dimana dilakukan secara online pada bagian {}".format(row[i], i) if row[i] is not np.nan else "" for _, row in df_month_activity.iterrows() for i in question_3_type)))))))
    print()
    print("4. Apa saja dan jelaskan pengembangan kompetensi yang telah didapat?")
    print("Bulan ini selama program ini saya mengembangkan beberapa kompetensi mulai:")
    print("\n".join(list(filter(lambda value: value != "", list(dict.fromkeys(list("- {} yang dimana dilakukan secara online pada bagian {}".format(row[i], i) if row[i] is not np.nan else "" for _, row in df_month_activity.iterrows() for i in question_4_type)))))))

  print()
  print("=" * 50)
  print()
  
  print("Bulan ini selama program ini saya mengikuti beberapa attendance mulai:")
  print("\n".join(list(filter(lambda value: value != "", list(dict.fromkeys(list("- {} yang dimana dilakukan secara online pada bagian {}".format(row[i], i) if row[i] is not np.nan else "" for _, row in df_month_activity.iterrows() for i in attend_type)))))))
  print()
  print("Bulan ini selama program ini saya mengerjakan beberapa assignment mulai:")
  print("\n".join(list(filter(lambda value: value != "", list(dict.fromkeys(list("- {} yang dimana dilakukan secara online pada bagian {}".format(row[i], i) if row[i] is not np.nan else "" for _, row in df_month_activity.iterrows() for i in do_type)))))))
  
  print()
  print("=" * 50)
  print()