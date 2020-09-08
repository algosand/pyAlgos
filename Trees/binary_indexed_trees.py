"""
Implementation of binary indexed trees:  To be continued, trying to learn what this code is doing exactly
in more details.  To be finished and explained. 

"""
class BIT:
	def __init__(self,n,idx):
		self.bit1=[0]*(n+2)
		self.bit2=[0]*(n+2)
		self.mode=idx
	def bit_add(self,a,w,bit):
		x=a
		while x<=(len(bit)-1):
			bit[x]+=w
			x+=x & (-1*x)
	def bit_sum(self,a,bit):
		ret=0
		x=a
		while x>0:
			ret+=bit[x]
			x-=x&(-1*x)
		return ret
	def add(self,l,r,w):
		l=l+(1-self.mode)
		r=r+(1-self.mode)
		self.bit_add(l,-1*w*l,self.bit1)
		self.bit_add(r,w*r,self.bit1)
		self.bit_add(l,w,self.bit2)
		self.bit_add(r,-1*w,self.bit2)
	def sum(self,l,r):
		l=l+(1-selfmode)
		r=r+(1-self.mode)
		ret=self.bit_sum(r,self.bit1)+r*self.bit_sum(r,self.bit2)
		ret-=self.bit_sum(l,self.bit1)+l*self.bit_sum(l,self.bit2)
		return ret