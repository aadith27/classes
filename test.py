class list_compare():

    def __init__(self,l1,l2):
        self.l1=l1
        self.l2=l2
        self.all=set(l1).union(set(l2))
        self.inter=set(l1).intersection(set(l2))

    def list_uncommon(self,l1,l2):
        print("Displaying uncommon elements")
        return(self.all-self.inter)

    def list_common(self,l1,l2):
        print("Displaying common elements")
        return(self.inter)


la=[1,2,3,45,23,34,212,3,2,3,4,2,67]
lb=[1,3,2,4,65,76,78]
compare=list_compare(la,lb)
print(compare.list_uncommon(la,lb))
print(compare.list_common(la,lb))