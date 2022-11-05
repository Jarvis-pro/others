#! /bin/bash

addre=`pwd`
echo $addre >> /home/xuliang-stu/work/tsh/mlcur/sac/$1/herpotentials.txt

for i in {0..10}
do
cd $i/relax
slab=`energy |  awk '{print $7}'  | head -2 | tail -1`
slab="$slab"
cd ../her/relax
sacH=`energy |  awk '{print $7}'  | head -2 | tail -1`
sacH="$sacH"
cd ../freq
freq=`echo -e "501 \n 298.15" | vaspkit | tail -16 | head -1 | awk '{print $7}'`
freq="$freq"
FreeEnergy=$(printf "%.4f" `echo "$sacH + $freq - $slab + 3.4"|bc`)
cd $addre
echo $i $slab $sacH $freq $FreeEnergy >> /home/xuliang-stu/work/tsh/mlcur/sac/$1/herpotentials.txt
echo $i
done

