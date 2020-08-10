class Label(object):
    def __init__(self,label_num,dict = None):
        self.label_num = label_num
        if not dict:
            self._center = {"x_acc":0,"y_acc":0,"z_acc":0}
            self._nodesnum = 0
            self._avglen = 0
        else:
            self._center = dict["center"]
            self._nodesnum = dict["nodesnum"]
            self._avglen = dict["avglen"]