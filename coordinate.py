t=int(input())
for _ in range(t):
    n=int(input())
    (x,y)=tuple([0,0])
    
    d=n//4
    (x,y)=(int(x+d/2*(2+(d-1)*4)-d/2*(2*3+(d-1)*4)),int(y+d/2*(2*2+(d-1)*4)-d/2*(2*4+(d-1)*4)))
    
    r=n%4

    if r==1:
        (x,y)=(x+d*4+r,y)
    elif r==2:
        (x,y)=(x+d*4+(r-1),y)
        (x,y)=(x,y+d*4+r)
    elif r==3:
        (x,y)=(x+d*4+(r-2),y)
        (x,y)=(x,y+d*4+(r-1))
        (x,y)=(x-(d*4+r),y)
    
      
       
    print(x,y)
        
