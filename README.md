# 🚴 BikeTrain

BikeTrain 是一個自行車訓練管理平台，提供騎乘紀錄管理、FTP 分析、訓練統計與個人成就追蹤功能。

---

## 📌 專案介紹

BikeTrain 旨在幫助自行車騎士：

- 記錄每日騎乘資料
- 追蹤訓練成果
- 分析 FTP 與 W/kg
- 設定月里程目標
- 查看騎乘統計圖表
- 解鎖騎乘成就
- 上傳個人頭像

---

## ✨ 功能特色

### 👤 使用者系統

- 註冊帳號
- 登入 / 登出
- 個人資料管理
- 頭像上傳

### 🚴 騎乘紀錄

- 新增紀錄
- 編輯紀錄
- 刪除紀錄
- 搜尋紀錄

紀錄內容：

- 日期
- 距離
- 時間
- 平均速度
- 訓練類型

---

### 📊 Dashboard

顯示：

- FTP
- 體重
- W/kg
- 騎士等級
- 連續騎乘天數

訓練統計：

- 平均速度
- 最長距離
- 總騎乘次數
- 總騎乘距離
- 總騎乘時間

---

### 🎯 月里程目標

使用者可自行設定：

- 每月目標距離

系統自動計算：

- 完成距離
- 完成百分比

---

### 🏅 成就系統

目前成就：

- 100km 騎士
- 500km 騎士
- 1000km 騎士

---

### 📈 圖表分析

使用 Chart.js

包含：

- 騎乘距離趨勢圖
- 訓練類型分布圖

---

## 🛠 技術架構

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- Chart.js

### Backend

- Python
- Flask
- Flask-Login
- Flask-WTF

### Database

- SQLite
- SQLAlchemy

---

## 📂 專案結構

```text
BikeTrain
│
├── app
│   ├── routes.py
│   ├── models.py
│   ├── forms.py
│   ├── templates
│   └── static
│
├── migrations
├── run.py
├── config.py
└── requirements.txt
```

## 🚀 安裝方式

### 1. 下載專案

```bash
git clone <repository-url>
```

### 2. 安裝套件

```bash
pip install -r requirements.txt
```

### 3. 啟動專案

```bash
python run.py
```

### 4. 開啟瀏覽器

```text
http://127.0.0.1:5000
```

---

## 👨‍💻 開發者

Jerry

靜宜大學資訊管理學系

BikeTrain 作品