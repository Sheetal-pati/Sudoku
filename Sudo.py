import random
def Check_input(x,y,Sudo):
	flag1=0
	sub_x=0
	sub_y=0
	while (i<9):
		if(Sudo[i][y]==value):
		   flag1=1
		   break
		else:
		   i+=1
	if(flag1==0):
		while (j<9):
			if(Sudo[x][j]==value):
			   flag1=1
			   break
			else:
		       j+=1
	if (flag1==0):
		if(x==0||x==1||x==2):
			if(y==0||y==1||y==2):
				print("case 1")
				while ((sub_x<3) && (flag1==0)):
					while (sub_y<3):
						if(Sudo[sub_x][sub_y]==value):
						   flag1=1;
						   break
						else:
							sub_y+=1
                    sub_x+=1
                if(flag1==0):
                	return 1
                else:
                    return 0	
            if(y==3||y==4||y==5):
            	print("case 2")
            	while ((sub_x<3) && (flag1==0)):
					while ((sub_y<6)&&(sub_y>2)):
						if(Sudo[sub_x][sub_y]==value):
						   flag1=1;
						   break
						else:
							sub_y+=1
                    sub_x+=1
                if(flag1==0):
                	return 1
                else:
                    return 0		
            if(y==6||y==7||y==8):
                print("case 3")	
                while ((sub_x<3) && (flag1==0)):
					while ((sub_y<9)&&(sub_y>5)):
						if(Sudo[sub_x][sub_y]==value):
						   flag1=1;
						   break
						else:
							sub_y+=1
                    sub_x+=1
                if(flag1==0):
                	return 1
                else:
                    return 0		

		if(x==3||x==4||x==5):
			if(y==0||y==1||y==2):
				print("case 4")
				while ((sub_x>2) && (sub_x<6)&&(flag1==0)):
					while (sub_y<3):
						if(Sudo[sub_x][sub_y]==value):
						   flag1=1;
						   break
						else:
							sub_y+=1
                    sub_x+=1
                if(flag1==0):
                	return 1
                else:
                    return 0		
            if(y==3||y==4||y==5):
            	print("case 5")
            	while ((sub_x>2) && (sub_x<6)&& (flag1==0)):
					while ((sub_y<6)&&(sub_y>2)):
						if(Sudo[sub_x][sub_y]==value):
						   flag1=1;
						   break
						else:
							sub_y+=1
                    sub_x+=1
                if(flag1==0):
                	return 1
                else:
                    return 0		
            if(y==6||y==7||y==8):
            	print("case 6")
                while ((sub_x>2) && (sub_x<6)&& (flag1==0)):
					while ((sub_y<9)&&(sub_y>5)):
						if(Sudo[sub_x][sub_y]==value):
						   flag1=1;
						   break
						else:
							sub_y+=1
                    sub_x+=1
                if(flag1==0):
                	return 1
                else:
                    return 0		

		if(x==6||x==7||x==8):
			if(y==0||y==1||y==2):
				print("case 7")
				while ((sub_x<9) && (sub_x>5)&& (flag1==0)):
					while (sub_y<3):
						if(Sudo[sub_x][sub_y]==value):
						   flag1=1;
						   break
						else:
							sub_y+=1
                    sub_x+=1
                if(flag1==0):
                	return 1
                else:
                    return 0		
            if(y==3||y==4||y==5):
            	print("case 8")
            	while ((sub_x<9) && (sub_x>5)&& (flag1==0)):
					while ((sub_y<6)&&(sub_y>2)):
						if(Sudo[sub_x][sub_y]==value):
						   flag1=1;
						   break
						else:
							sub_y+=1
                    sub_x+=1
                if(flag1==0):
                	return 1
                else:
                    return 0	    
            if(y==6||y==7||y==8):
            	print("case 9")
            	while ((sub_x<9) && (sub_x>5)&& (flag1==0)):
					while ((sub_y<9)&&(sub_y>5)):
						if(Sudo[sub_x][sub_y]==value):
						   flag1=1;
						   break
						else:
							sub_y+=1
                    sub_x+=1
                if(flag1==0):
                	return 1
                else:
                    return 0	

def Easy():
	Sudo=[9][9]
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
            flag=Check_input(x,y,Sudo)
def Medium():
	Sudo=[9][9]
	num=random.randint(25,30)
	i=0
	j=0
	count=0
	while(count<num):
		value=random.randint(0,10)
		flag=0
		while(flag==0):
			x=random.randint(-1,9)
		    y=random.randint(-1,9)
            flag=Check_input(x,y,Sudo)

def Hard():
	Sudo=[9][9]
	num=random.randint(20,25)
	i=0
	j=0
	count=0
	while(count<num):
		value=random.randint(0,10)
		flag=0
		while(flag==0):
			x=random.randint(-1,9)
		    y=random.randint(-1,9)
            flag=Check_input(x,y,Sudo)

def Expert():
	Sudo=[9][9]
	num=random.randint(15,20)
	i=0
	j=0
	count=0
	while(count<num):
		value=random.randint(0,10)
		flag=0
		while(flag==0):
			x=random.randint(-1,9)
		    y=random.randint(-1,9)
            flag=Check_input(x,y,Sudo)
            if (flag==1):
            	Sudo[x][y]=value
            	break
            else:
            	continue
def Check_Solution(Sudo):
	i=0
	j=0
	count=0
	while(i<9):
		while(j<9):
			unique = set(Sudo[i])  
            for each in unique: 
                count = Sudo.count(each)  
                if count > 0:  
                    print("Oops! You lost the game")
                    return False
                    break
                j+=1    
            i+=1
            //within sub grids for each case
    if(count>0):
    	print("Congratulations! You won the game")  
        return True






	
