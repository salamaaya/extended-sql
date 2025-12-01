class Phi:
    def __init__(self):
        self.select = [] # list of selected attributes
        self.n_grouping_vars = 0 # number of group variables
        self.group_by = [] # list of group by attributes
        self.aggregates = [] # list of aggregate functions
        self.such_that = [] # list of such that conditions
        self.grouping_vars = [] # list of grouping variable ids

    def add_select(self, attributes):
        if isinstance(attributes, list):
            self.select.extend(attributes)
        else:
            self.select.append(attributes)

    def increment_grouping_vars(self):
        self.n_grouping_vars += 1

    def add_group_by(self, attributes):
        if isinstance(attributes, list):
            self.group_by.extend(attributes)
        else:
            self.group_by.append(attributes)
    
    def add_aggregate(self, aggregates):
        if isinstance(aggregates, list):
            self.aggregates.extend(aggregates)
        else:
            self.aggregates.append(aggregates)
    
    def add_such_that(self, conditions):
        if isinstance(conditions, list):
            self.such_that.extend(conditions)
        else:
            self.such_that.append(conditions)
    
    def add_grouping_var(self, var_id):
        if var_id not in self.grouping_vars:
            self.grouping_vars.append(var_id)