# 定義一個包含學生資料的字典
student = {}

# 讀取用戶輸入
student["sid"] = input("請輸入您的學號：")
student["sname"] = input("請輸入您的姓名：")
student["fchina"] = float(input("請輸入您的國文成績："))
student["fmath"] = float(input("請輸入您的數學成績："))
student["finfo"] = float(input("請輸入您的電腦成績："))

# 計算總分和平均分
total_score = student["fchina"] + student["fmath"] + student["finfo"]
# 四捨五入
total_score_round = round(total_score)
average_score = round(total_score / 3, 2)

# 判斷成績是否及格
if average_score < 60:
    result = "不及格"
else:
    result = "合格"

# 印出結果
print("-" * 30)
print(f'{student["sname"]}({student["sid"]})同學您好：')
print("以下是您的各科成績與分數評定\n")
print(f'國文：{student["fchina"]} / 數學：{student["fmath"]} / 電腦：{student["finfo"]}')
print(f'總分：{total_score_round} / 平均：{average_score}')
print("-" * 30)
print(f'成績判定：{result}')
