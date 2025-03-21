class Shopping_cart:
    it=""
    cost=""
    r1=""
    dic={}
    def adding(self,i,c):
        self.it=i
        self.cost=c
        self.dic.update({self.it:self.cost})
    def remove(self,r):
        self.r1=r
        if self.r1 in self.dic:
            self.dic.pop(self.r1)
        else:
            print("OOPS..SORRY ")
    def total(self):
        self.t=0
        for i in self.dic.values():
            self.t+=int(i)
        print("total cost:",self.t)
    def disp(self):
        print(self.dic)

c=Shopping_cart()
is_run=True
while(is_run):
    print("1.Adding Elements into cart\n2.Remove the item\n3.Total Amount\n4.Display Items and Costs\n5.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        n=int(input("Enter no.of items you want:"))
        for i in range(n):
            x=input("Enter Item:")
            y=input("Enter price:")
            c.adding(x,y)
    elif ch==2:
        rm=input("Enter intem to be removed:")
        c.remove(rm)
    elif ch==3:
        c.total()
    elif ch==4:
        c.disp()
    else:
        is_run=False


print("Bye...SEE YOU NEXT")