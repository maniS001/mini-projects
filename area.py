class Solution(object):
    def maxArea(self, height):
        """
        :type height: max_areast[int]
        :rtype: int
        """
        self.height=height
        myList=self.height
        max_areas=[]
        for i in range(0,len(myList)):
            area=0
            for j in range(i):
                mini=min(myList[i],myList[j])
                p=(i-j)*mini
                if p>area:
                    area=p
            max_areas.append(area)
        return(max(max_areas))
obj=Solution()
print(obj.maxArea([32,5,6,7,5,6]))  
#output:
'''find largest area between two lines
by ploting each value at graph
out: 30

'''
            
       
    
    
                