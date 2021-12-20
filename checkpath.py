import os,time
# file_path = 'C:\\selenium\\result\\'+current_day
# if not os.file_path.isdir(file_path):
# 	os.mkdir(file_path)
# fb =open(file_path, "wb")
def checktime():
	current_day = time.strftime("%Y-%m-%d", time.localtime(time.time()))
	current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
	print(current_time)
	print(current_day)
	pic_path = 'C:\\selenium\\result\\'+current_day+'\\'+current_time+'.png'
	file_path = 'C:\\selenium\\result\\'+ current_day
	print(pic_path)
	print(file_path)
	print(current_time)
	print(current_day)
# if ( os.path.isdir(file_path)):
#     print("Directory exists!")
# else:
#     print("Directory not found!")
# 檢查路徑是否存在
# if os.path.exists(file_path):
#   print("路徑存在。")
# else:
#   print("路徑不存在。")
#   os.mkdir(file_path)
#   print("create successfully")
# # 檢查路徑是否為檔案
# if os.path.isfile(file_path):
#   print("路徑是檔案。")
# else:
#   print("路徑不是檔案。")
# # 檢查路徑是否為目錄
# if os.path.isdir(file_path):
#   print("路徑是目錄。")
# else:
#   print("路徑不是目錄。")

if __name__ == "__main__":
	checktime()

