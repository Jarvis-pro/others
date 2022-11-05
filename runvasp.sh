#!/bin/sh
### Set intel environment###
source /opt/compilers_and_libraries_2019/linux/bin/compilervars.sh intel64
source /opt/compilers_and_libraries_2019/linux/mkl/bin/mklvars.sh intel64
source /opt/impi/2019.5.281/intel64/bin/mpivars.sh ilp64 

ulimit -s unlimited

#获取任务开始时间和地址
vasp_start_time=`date`
adress=`pwd`

if [ $# -eq 0 ];
then
	    /home/xu/opt/vasp_optcell/vasp.6.1.0/bin/vasp_std
    elif [ $# -eq 1 ];
    then
	    #   mpirun -np $1 vasp
	       mpirun -np $1 /home/xu/opt/vasp_optcell/vasp.6.1.0/bin/vasp_std
       else
   echo "Too less or many parameters, stop."
   echo "Usage: runvasp.sh  processor_number"
fi

#获取结束时间
vasp_end_time=`date`

# 写入文件
log_file_name=`echo "$vasp_start_time""$adresse"|sed 's/ //g'`
cat > ~/log_vasp/$log_file_name<<!!!
任务开始时间：$vasp_start_time
任务结束时间：$vasp_end_time
任务执行所在文件夹：$adress

nohup.out
----------------------------------------


!!!
#cat nohup.out >> ~/log_vasp/$log_file_name

#发送结果到指定邮箱
#echo  "~/log_vasp/$log_file_name $adress/nohup.out"|mail -s "办公室服务器vasp计算结果通知" 1148646360@qq.com
echo  "
任务开始时间：$vasp_start_time
任务结束时间：$vasp_end_time
任务执行所在文件夹：$adress"|mail -s "办公室服务器vasp计算结果通知" -a $adress/nohup.out  1148646360@qq.com
#mail -s "办公室服务器vasp计算结果通知" 1148646360@qq.com< ~/log_vasp/$log_file_name

rm ~/log_vasp/$log_file_name
