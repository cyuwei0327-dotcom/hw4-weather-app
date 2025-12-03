import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import rcParams

# 設定支援中文字體（Windows 通用：微軟正黑體）
rcParams['font.family'] = 'Microsoft JhengHei'

# 避免負號亂碼
rcParams['axes.unicode_minus'] = False

# 頁面標題
st.title("🌤️ 氣溫預報 Web App")

# 連接 SQLite 資料庫
conn = sqlite3.connect("data.db")
df = pd.read_sql_query("SELECT * FROM TemperatureForecasts", conn)

# 地區選單
regions = df["regionName"].unique()
selected_region = st.selectbox("請選擇地區：", regions)

# 篩選該地區資料並排序
region_df = df[df["regionName"] == selected_region].sort_values("dataDate")

# 顯示氣溫表格
st.subheader(f"📋 {selected_region} 地區氣溫資料")
st.dataframe(region_df[["dataDate", "mint", "maxt"]], use_container_width=True)

# 畫折線圖
st.subheader(f"📈 {selected_region} 一週氣溫變化圖")

plt.figure(figsize=(10, 4))
plt.plot(region_df["dataDate"], region_df["maxt"], marker='o', label="最高氣溫 maxt")
plt.plot(region_df["dataDate"], region_df["mint"], marker='o', label="最低氣溫 mint")
plt.xlabel("日期")
plt.ylabel("溫度 (°C)")
plt.xticks(rotation=45)
plt.title(f"{selected_region} 一週氣溫變化")
plt.grid(True)
plt.legend()
st.pyplot(plt)
