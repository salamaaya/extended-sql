class Phi:
    def __init__(self):
        self.select = [] # list of selected attributes
        self.n_grouping_vars = 0 # number of group variables
        self.group_by = [] # list of group by attributes
        self.aggregates = [] # list of aggregate functions
        self.such_that = [] # list of such that conditions
        self.grouping_vars = [] # list of grouping variable ids
