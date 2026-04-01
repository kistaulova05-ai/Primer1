# #делала с Николаевым
# import os
# my_secret1=os.environ['S1_Nikolaev']
# print(my_secret1)

# import os
# my_secret2=os.environ['S2_Nikolaev']
# print(my_secret2)

# import os
# my_secret3=os.environ['S3_Nikolaev']
# print(my_secret3)

# #Задание 2 (делала одна, вариант 1)
# from sympy import *

# k, T, C, L = symbols('k C T L')

# C_ost_4 = 15000
# Am_lst_4 = []
# C_ost_lst_4 = []
# for i in range(8):
#     Am = (C - L) / T
#     C_ost_4 -= Am.subs({C: 15000, T: 8, L: 0})
#     Am_lst_4.append(round(Am.subs({C: 15000, T: 8, L: 0}), 2))
#     C_ost_lst_4.append(round(C_ost_4, 2))
# print('Am_lst_4:', Am_lst_4)
# print('C_ost_lst_4:', C_ost_lst_4)

# #2-ой способ 
# Aj = 0
# C_ost_4 = 15000
# Am_lst_2_4 = []
# C_ost_lst_2_4 = []
# for i in range(8):
#     Am = k * 1 / T * (C - Aj)
#     C_ost_4 -= Am.subs({C: 15000, T: 8, k: 2})
#     Am_lst_2_4.append(round(Am.subs({C: 15000, T: 8, k: 2}), 2))
#     Aj += Am
#     C_ost_lst_2_4.append(round(C_ost_4, 2))
# print('Am_lst_2_4:', Am_lst_2_4)
# print('C_ost_lst_2_4:', C_ost_lst_2_4)

# #Таблица 
# import pandas as pd

# Y = range(1, 9)
# table1 = list(zip(Y, C_ost_lst_4, Am_lst_4))
# table2 = list(zip(Y, C_ost_lst_2_4, Am_lst_2_4))
# tframe = pd.DataFrame(table1, columns=['Y', 'C_ost_lst_4', 'Am_lst_4'])
# tframe2 = pd.DataFrame(table2, columns=['Y', 'C_ost_lst_2_4', 'Am_lst_2_4'])
# print(tframe)
# print(tframe2)

# #Визуализация 
# import numpy as np
# import matplotlib.pyplot as plt

# plt.figure() #что значит? Создает фигуру - ответила Журавлева
# plt.plot(tframe['Y'], tframe['C_ost_lst_4'], label='Am')
# plt.savefig('chart7.png')
# plt.figure()
# plt.plot(tframe2['Y'], tframe2['C_ost_lst_2_4'], label='Am_2')
# plt.savefig('chart8.png')

# #Круговая диаграмма 
# vals = Am_lst_4
# labels = [str(x) for x in range(1, 9)]
# explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,0.1)
# fig, ax = plt.subplots()
# ax.pie(vals,
#        labels=labels,
#        autopct='%1.1f%%',
#        shadow=True,
#        explode=explode,
#        wedgeprops={
#            'lw': 1,
#            'ls': '--',
#            'edgecolor': "k"
#        },
#        rotatelabels=True)
# ax.axis("equal")
# plt.savefig('chart9.png') #Что значит? Сохраняет график в файл - ответила Журавлева

# #Круговая диаграмма (данные от 2-го способа)
# vals = Am_lst_2_4
# labels = [str(x) for x in range(1, 9)]
# explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,0.1)
# fig, ax = plt.subplots()
# ax.pie(vals,
#        labels=labels,
#        autopct='%1.1f%%',
#        shadow=True,
#        explode=explode,
#        wedgeprops={
#            'lw': 1,
#            'ls': '--',
#            'edgecolor': "k"
#        },
#        rotatelabels=True)
# ax.axis("equal")
# plt.savefig('chart10.png')

# #Гистограмма (индивидуальное задание)
# table1 = list(zip(Y, Am_lst_4))
# table2 = list(zip(Y, Am_lst_2_4))
# tframe = pd.DataFrame(table1, columns=['Y', 'Am_lst_4'])
# tframe2 = pd.DataFrame(table2, columns=['Y', 'Am_lst_2_4'])

# plt.figure()
# plt.bar(tframe['Y'], tframe['Am_lst_4'])#что значит? Строит график- ответила Журавлева 
# plt.savefig('chart11.png')

# plt.figure()
# plt.bar(tframe2['Y'], tframe2['Am_lst_2_4'])
# plt.savefig('chart12.png')

# #Все корректно, ставлю оценку 5, проверила Журавлева 
# #Ответы на вопросы верны, у Журавлевой оценка 5

# #Первое задание
# import os
# S1_kistaulova = os.environ ['S1_kistaulova']
# print(S1_kistaulova)

#по ТЗ
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import json
import sys
import os

BLOCK_THRESHOLD = int(os.environ['BLOCK_THRESHOLD'])
LOG_FILE        = "1.json"
FAILED_LOG_FILE = "2.json"
CHART_FILE      = "report.png"


def load_attempts():
    try:
        with open(LOG_FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        sys.exit(f" Файл '{LOG_FILE}' не найден.")
    except json.JSONDecodeError:
        sys.exit(f"Файл '{LOG_FILE}' повреждён или имеет неверный формат JSON.")


def _resettable_fails(success_series):
    counts, count = [], 0
    for s in success_series:
        if s:
            count = 0
        else:
            count += 1
        counts.append(count)
    return counts


def analyze(attempts):
    df = pd.DataFrame(attempts)
    df["Статус"] = df["success"].map({True: "УСПЕШНО", False: "НЕУДАЧА"})

    df = df.sort_values("timestamp").reset_index(drop=True)

    df["fail_so_far"] = df.groupby("mac", group_keys=False).apply(
        lambda g: pd.Series(_resettable_fails(g["success"]), index=g.index)
    )

    df["Блок"] = df["fail_so_far"].apply(
        lambda x: "ЗАБЛОКИРОВАН" if x >= BLOCK_THRESHOLD else "-"
    )

    fails = (
        df[df["success"] == False]
        .groupby("mac")
        .size()
        .rename("fail_count")
    )

    blocked = set(
        df.groupby("mac")["fail_so_far"]
        .max()
        .pipe(lambda s: s[s >= BLOCK_THRESHOLD])
        .index
    )

    return df, fails, blocked


def save_failed_attempts(df):
    failed = df[df["success"] == False][["mac", "ssid", "pin_tried", "timestamp"]].copy()
    records = failed.to_dict(orient="records")
    with open(FAILED_LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)


def print_table(df):
    display = df[["mac", "ssid", "pin_tried", "timestamp", "Статус", "Блок"]].copy()
    display.columns = ["MAC-адрес", "SSID", "PIN", "Время", "Статус", "Блок"]

    print("         ОТЧЁТ: Обнаружение WPS атак".center(85))
    print(display.to_string(index=False))


def print_summary(df, fails, blocked):
    total = df.groupby("mac").size().rename("Попыток")

    summary = pd.concat([total, fails], axis=1).fillna(0)
    summary["fail_count"] = summary["fail_count"].astype(int)
    summary["Статус"] = summary.index.map(lambda m: "Заблокирован" if m in blocked else "Активен")
    summary.index.name = "MAC-адрес"
    summary.columns = ["Попыток", "Неудач", "Статус"]

    print("\n" + "=" * 55)
    print("         Сводка по подключениям".center(55))
    print(summary.to_string())

    fail_values = fails.values

    print(f"\n  Всего попыток ввода PIN: {len(df)}")
    print(f"  Уникальных MAC-адресов: {df['mac'].nunique()}")
    print(f"  Заблокировано устройств: {len(blocked)}")
    print(f"  Среднее неудачных попыток ввода PIN: {np.mean(fail_values):.1f}")
    print(f"  Максимально неудачных попыток ввода PIN: {np.max(fail_values)}")

    if blocked:
        print(" Заблокированные устройства:")
        for mac in blocked:
            print(f"      -> {mac} ({fails[mac]} неудачных попыток)")
        print()


def plot_summary(df, fails, blocked):
    macs = df["mac"].unique().tolist()

    fail_vals = np.array([fails.get(m, 0) for m in macs])
    mean_fail = np.mean(fail_vals)
    std_fail  = np.std(fail_vals)

    block_count  = len(blocked)
    active_count = len(macs) - block_count

    fig, ax = plt.subplots(figsize=(6, 6))
    fig.suptitle("Статус устройств", fontsize=14, fontweight="bold")

    wedge_colors = ["#e74c3c", "#2ecc71"]
    wedge_labels = [f"Заблокировано\n({block_count})", f"Активен\n({active_count})"]
    explode = [0.05, 0]

    wedges, texts, autotexts = ax.pie(  
        [block_count, active_count],
        labels=wedge_labels,
        colors=wedge_colors,
        autopct="%1.0f%%",
        startangle=90,
        explode=explode,
        textprops={"fontsize": 11},
        wedgeprops={"edgecolor": "white", "linewidth": 1.5}
    )
    for at in autotexts:
        at.set_fontweight("bold")

    stats_text = (
        f"Среднее неудачных попыток : {mean_fail:.1f}\n"
    )
    ax.text(0, -1.45, stats_text, ha="center", va="center", fontsize=9,
            bbox=dict(boxstyle="round,pad=0.5", facecolor="#f8f9fa", edgecolor="#bdc3c7"))

    blocked_patch = mpatches.Patch(color="#e74c3c", label="Заблокирован")
    active_patch  = mpatches.Patch(color="#2ecc71", label="Активен")
    ax.legend(handles=[blocked_patch, active_patch], fontsize=9, loc="upper right")

    plt.tight_layout()
    plt.savefig(CHART_FILE, dpi=130, bbox_inches="tight")
    plt.close()

def main():
    attempts = load_attempts()
    df, fails, blocked = analyze(attempts)

    print_table(df)
    print_summary(df, fails, blocked)
    save_failed_attempts(df)
    plot_summary(df, fails, blocked)


main()