import sys
import sendemail

addlines="";
for line in sys.stdin:
    addlines = addlines + line;

if (len(addlines) > 0) :
    sm = sendemail.sendemail();        
    sm.sendatt(addlines, "\n\n");
	
