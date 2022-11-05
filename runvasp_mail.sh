#!/bin/sh
### Set intel environment###
source /opt/intel/composer_xe_2015/bin/compilervars.sh intel64
source /opt/intel/mkl/bin/intel64/mklvars_intel64.sh
source /opt/intel/impi/5.0.2.044/bin64/mpivars.sh

ulimit -s unlimited
vasp_start_time=`date`
adress=`pwd`

#运行vasp
if [ $# -eq 0 ];
then
    /home/xuliang-stu/opt/vasp.5.4.4/bin/vasp_std
elif [ $# -eq 1 ];
then
#   mpirun -np $1 vasp_std
   mpirun -np $1 /home/xuliang-stu/opt/vasp.5.4.4/bin/vasp_std
else
   echo "Too less or many parameters, stop."
   echo "Usage: runvasp.sh  processor_number"
fi

#获取结束时间
vasp_end_time=`date`

cp /home/xuliang-stu/bin/python_mail.py .

# 将时间和目录写入文件
T="任务开始时间：$vasp_start_time;任务结束时间：$vasp_end_time ;任务执行所在文件夹：$adress "
sed -i "18i \"html\": \"NanChang:$T\"" python_mail.py

#任务执行所在文件夹：$adress
#执行发送邮件脚本
python python_mail.py

#初始化脚本
rm python_mail.py
