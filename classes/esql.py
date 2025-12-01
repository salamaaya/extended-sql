class ESQL:
    def __init__(self):
        self.select = [] # list of selected attributes
        self.from_tables = [] # list of tables
        self.where = "" # OPTIONAL: string of the WHERE condition
        self.group_by = [] # OPTIONAL: list of group by attributes
        self.having = "" # OPTIONAL: string of having condition
        self.such_that = [] # OPTIONAL: list of such that conditions

    def add_select(self, attributes):
        if isinstance(attributes, list):
            self.select.extend(attributes)
        else:
            self.select.append(attributes)

    def add_where(self, conditions):
        self.where += conditions # string addition

    def add_having(self, conditions):
        self.having += conditions # string addition

    def add_group_by(self, attributes):
        if isinstance(attributes, list):
            self.group_by.extend(attributes)
        else:
            self.group_by.append(attributes)
    
    def add_such_that(self, conditions):
        if isinstance(conditions, list):
            self.such_that.extend(conditions)
        else:
            self.such_that.append(conditions)

    def __str__(self):
        return f"""
            Select Clause: {self.select}
            Tables:{self.from_tables}
            Where Clause:{self.where}
            Group By Clause: {self.group_by}
            Having Clause:{self.having}
            Such That Clause:{self.such_that}
            """