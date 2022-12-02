# 介绍
本仓库用于保存一些研究工作中写的小脚本，减少简单重复操作，提高工作效率。

## Li-frequence.py
用于处理华辰电化学工作站CHI660测试锂电池阻抗谱的数据。

## heroverpotentials.sh
用于批量读取HER自由能垒数据，做手头筛选单原子HER的工作写的。

## runvasp_mail.sh/vasp_mail.pbs
两个都是服务器提交任务脚本，任务结束可将日志文件发送到邮箱。前者用于小型服务器，后者用于没有开通邮件服务的超算，需配合sendcloud的api使用。

## vasp_submit.sh
实现全自动化批量计算HER，只需提交slab的POSCAR。slab优化→活性位点吸附氢原子→优化→自由能矫正→邮件提醒。
