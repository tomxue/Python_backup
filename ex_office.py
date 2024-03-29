# Filename: backup_ver4.py  
import os  
import time  
  
# 1.需要备份的文件目录  
source1 = 'C:\\Users\\tomxue\\Desktop'
source2 = r'"C:\Program Files\Vim"'
cwd = 'C:\\Program Files\\WinRAR'
  
# 2. 备份文件到目标路径  
target_dir = 'D:\\Dropbox\\lenovo\\Backup\\'
  
# 3. The files are backed up into a zip file.  
# 4. The current day is the name of the subdirectory in the main directory  
PathOfToday = target_dir + time.strftime('%Y-%m-%d')
# The current time is the name of the zip archive  
now = time.strftime('%H-%M-%S')  
  
# Take a comment from the user to create the name of the zip file  
comment = raw_input('Enter a comment -->')  
if len(comment)==0:   
    target = PathOfToday+os.sep+now+'.zip'  
else:  
    target = PathOfToday+os.sep+now+'_'+\
             comment.replace(' ','_')+'.zip'
    # Notice the backslash!  
  
# Create the subdirectory if it isn't already there  
if not os.path.exists(PathOfToday):  
    os.mkdir(PathOfToday)  # make directory  
    print('Successfully created directory', PathOfToday)  
  
# 5. 用winrar的rar命令压缩文件，但首先要安装有winrar且设置winrar到环境变量的路径path中  
zip_command = "rar a %s %s %s & pause" %(target, source2, source1)
  
# Run the backup  
# 设置winrar到path环境中，这里已经手动添加，如图  
# os.system('set Path=%Path%;C:\\Program Files\\WinRAR')
os.chdir(cwd)
ret = os.system(zip_command)
print 'Successful backup to', target, '.', 'And return value =', ret