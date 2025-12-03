# 🌤️ 氣溫預報 Web App

📌 Demo 網址：  
👉 [[https://your-streamlit-url.streamlit.app](https://hw4-weather-app-ggshcsvszh2w5rnwxbcfrn.streamlit.app/)]([https://your-streamlit-url.streamlit.app](https://hw4-weather-app-ggshcsvszh2w5rnwxbcfrn.streamlit.app/))

---

## 📚 專案功能說明

🔹 使用 `requests` 套件調用中央氣象局 F-A0010-001 API，獲取 JSON 格式氣象資料  
🔹 解析 JSON 結構，提取每日最高/最低溫資料（MaxT / MinT）  
🔹 將氣溫資料寫入 SQLite `data.db` 資料庫，並可查詢地區名稱與中部地區氣溫  
🔹 以 Streamlit 實作氣溫預報 Web App，支援地區下拉選單、氣溫表格與折線圖顯示

---

## 🖼️ App 頁面特色

- 📌 下拉選單選擇地區
- 🧾 表格顯示該地區未來一週氣溫
- 📈 折線圖呈現最高/最低溫趨勢
- 🖼️ 自訂主題與背景美化（含中央氣象局圖示）

---

## 🛠️ 使用套件（Python 3.x）

```txt
streamlit
pandas
matplotlib
requests
sqlite3（內建）
