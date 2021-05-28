tail -n 1000 /home/pi/raspproj/tvroomtemp.txt | sed s/^...........// | sort | sed s/:...../:00:00/ | sort -nr | uniq -w 5 | sort > /home/pi/raspproj/max.txt
tail -n 1000 /home/pi/raspproj/tvroomtemp.txt | sed s/^...........// | sort | sed s/:...../:00:00/ | sort | uniq -w 5 | sort > /home/pi/raspproj/min.txt
tail -n 288 /home/pi/raspproj/tvroomtemp.txt | head -n 144 | sed s/^...........// | sort >  /home/pi/raspproj/prevday.txt
tail -n 144 /home/pi/raspproj/tvroomtemp.txt | sed s/^...........// | sort >  /home/pi/raspproj/lastday.txt
gnuplot -e "set term jpeg; set xdata time; set timefmt \"%H:%M:%S\"; set format x \"%H\"; unset key; set datafile separator \",\"; plot '/home/pi/raspproj/lastday.txt' using 1:2 lc rgb 'purple','/home/pi/raspproj/lastday.txt' using 1:3 lc rgb 'green', '/home/pi/raspproj/max.txt' using 1:2 lc rgb 'red', '/home/pi/raspproj/min.txt' using 1:2 lc rgb 'blue';"
