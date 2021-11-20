class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        self.height=height
        a=self.height
        lis=[]
        for i in range(0,len(a)):
            c=0
            for j in range(i):
                mini=min(a[i],a[j])
                p=(i-j)*mini
                if p>c:
                    c=p
            lis.append(c)
        return(max(lis))
                    
       
    
    
                