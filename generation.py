import numpy as np

class Generation:
    ancestors = None
    children = np.array([])
    generation_i = 0
    num_clauses = 0
    num_variables = 0

    """docstring for ClassName"""
    def __init__(self, ancestors, children, num_clauses, num_variables):
        super(Generation, self).__init__()
        self.children = children
        self.ancestors = ancestors
        if(type(ancestors) == Generation):
            self.generation_i = self.ancestors.generation_i + 1
        else:
            self.generation_i = 1
        self.num_clauses = num_clauses
        self.num_variables = num_variables


#  Write assignents into children
class Child:
    assignment = None
    score = 0
    parent = None

    """docstring for ClassName"""
    def __init__(self, assignment, score, parent):
        super(Child, self).__init__()
        self.assignment = assignment
        self.score = score
        self.parent = parent
