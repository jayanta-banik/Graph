class Graph:
    from numpy import shape
    
    def __init__(self, nodes=None, edges=None, data=None, mat=None, direct= False, gtype=None, war=True):
        self.G = None
        self._node = {'data':[], 'to':[], 'from':[]}
        self.list_edges = []
        self.adj_mat = mat
        self.isDirected = direct
        self.gtype = gtype
        
#          checking for input errors
        if (type(mat) is not list or type(mat) is not type(np.array([0])) and mat is not None):
            raise TypeError("mat is not list, expected 2D or 3D list or numpy array")
        if (type(nodes) is not list or type(nodes) is not type(np.array([0])) or type(nodes) is not int) and nodes is not None:
            raise TypeError('''nodes should be mentioned as list of names of nodes['A','B',...] 
            or as int as in number of nodes\nExpected int, list or numpy.ndarray but recieved{}'''.format(type(nodes)))     
        if (type(edges) is not list or type(edges) is not type(np.array([0])or type(edges) is bool) and edges is not None):
            raise TypeError('''edges is not list or bool, expected 2D list or numpy array
            or boolean value for connected or disconnected graph''')        
        if (type(data) is not list or type(data) is not type(np.array([0])) and data is not None):
            raise TypeError("data is not list, expected list or numpy array")        
        if type(direct) is not bool:
            raise TypeError("direct is not bool")        
        if type(war) is not bool:
            raise TypeError("war is not bool")        
        if type(gtype) is not str and type(gtype) is not NoneType:
            raise TypeError("gtype is not str, expected string")        
        if gtype not in [None,'tree','cyclic','eulerian'] and war:
            gtype = None   
            print("Warning: No gtype {} found, default 'None' used \nTo disable warnings make 'war'=False".format(gtype))            
        self.gtype = gtype
        
        if mat is not None:
            if len(shape(mat)) is not 2 or len(shape(mat)) is not 3:
                raise ValueError('shape expected = ({0},{0})\t got {1}'.format(len(mat), shape(mat)))
            if nodes is None or len(nodes) is len(mat):
                nodes = [i for i in range(len(mat))]
                
            for i,n in enumerate(nodes):
                
                _temp = self._node.copy()
                
                if data is not none:
                    _temp['data'] = data[i]
                
                _to_temp = []
                _from_temp = []
                for j in range(len(mat)):
                    if i is not j:
                        _from_temp.append(mat[j][i])
                        _to_temp.append(mat[i][j])
                _temp['to'] = _to_temp
                _temp['from'] = _from_temp
                G[n] = _temp.copy()
                                
                for j, f in enumerate(e):
                    if type(f) is list or type(f) is tuple:
                        pass
                    elif type(f) is int or type(f) is float:
                        _to_temp.append([nodes[j]])
                    else:
                        raise TypeError("mat contains type {}".format(type(j)))
                    
        
        elif nodes is not None:
            if len(data) != len(nodes) and data is not None:
                raise ValueError("nodes {} but data recieved for {}".format(len(nodes), len(data)))
            
            if type(nodes) is int:
                nodes = [i for i in range(nodes)]
            
            if edges is True or edges[0] is True:
                    for j in nodes:
                        if j is not i:
                            self.list_edges.append([[j,name] if edge is True else [j,name,edge[i if len(edge) is 2 else -1]]])
                            self.list_edges.append([[name,j] if edge is True else [name,j,edge[i if len(edge) is 2 else -1]]])
            else:
                self.list_edges = edges
                
            for i,name in enumerate(nodes):
                _temp = self._node.copy()
                
                if data is not none:
                    _temp['data'] = data[i]
                
                _to_temp = []
                _from_temp = []
                if edges is True:
                    _to_temp.append([(j,0) for j in nodes if j is not name])
                elif edges[0] is True:
                    if len(edge) is not 2:
                        raise ValueError("edges of length 2 expected")
                    for j in nodes:
                        if j is not name:
                            _to_temp.append((j,edge[1]))
                else: 
                    for j in edges:
                        if j[0] is name:
                            _to_temp.append(j)
                        if j[1] is name:
                            _from_temp.append(j)
                _temp['to'] = _to_temp
                _temp['from'] = _from_temp
                
                G[name] = _temp
                    
        else:
            if edge is not None:
                raise ValueError("Edges innitialized without Nodes")
            if data is not None:
                raise ValueError("Data provided without Nodes")

         
        if gtype not in [None,'tree','cyclic','eulerian'] and war:
            gtype = None
            
            print("Warning: No gtype {} found, default 'None' used \nTo disable warnings make 'war'=False".format(gtype))            
        self.gtype = gtype
        
        if nodes is None and mat is None and war:
            print("Warning: No Graph innitialized\nTo disable warnings make 'war'=False")
            
