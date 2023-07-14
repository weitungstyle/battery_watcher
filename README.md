# # Battery_Watcher


### 功能描述

- 電池電量通知

  - 電量高於設定值（預設80%）提醒拔除充電器
  - 電量低於設定值（預設40%）提醒開始充電

- 是否背景執行

  - 選擇關閉設定頁面視窗後，是否背景執行（目前仍須 terminal 以執行 python ）

- 電量使用圖表
  - 可以選擇日期範圍
  - 繪製電量使用圖表


### Launch

1. Make shure that you have installed python 3.11 and tkinter 3.8

2. Open terminal enter following order to copy the repository to local

```
git clone https://github.com/weitungstyle/battery_watcher.git
```

3. Move to target folder

```
cd battery_watcher
```

4. You can create an virtual environment by following order, or skip to step 6.

```
python3 -m venv venv
```

5. Activate the virtual environment

```
source venv/bin/activate
```

6. Install the requrie library

```
pip install --trusted-host pypi.python.org -r requirements.txt
```

7. Launch the app and keep the terminal window running

```
python main.py
```


8. Stop running:

press 'ctrl' + 'c'
