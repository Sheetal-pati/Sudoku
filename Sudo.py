import random
Sudo=[9][9]
def Check_input():
	flag1=0
	sub_x=0
	sub_y=0
	while (i<9):
		if(Sudo[i][y]==value):
		flag1=1
		break
	if(flag1==0):
		while (j<9):
			if(Sudo[x][j]==value):
				flag1=1
				break
	if (flag1==0):
		if(x==0||x==1||x==2):
			if(y==0||y==1||y==2):
				print("case 1")

            if(y==3||y==4||y==5):
            	print("case 2")
            if(y==6||y==7||y==8):
                print("case 3")	

		if(x==3||x==4||x==5):
			if(y==0||y==1||y==2):
				print("case 4")
            if(y==3||y==4||y==5):
            	print("case 5")
            if(y==6||y==7||y==8):
            	print("case 6")


		if(x==6||x==7||x==8):
			if(y==0||y==1||y==2):
				print("case 7")
            if(y==3||y==4||y==5):
            	print("case 8")
            if(y==6||y==7||y==8):
            	print("case 9")

def Ease():
	num=random.randint(30,35)
	i=0
	j=0
	count=0
	while(count<num):
		value=random.randint(0,10)
		flag=0
		while(flag==0):
			x=random.randint(-1,9)
		    y=random.randint(-1,9)
            flag=Check_input()


	
