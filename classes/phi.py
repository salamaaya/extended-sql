import re

class Phi:
    def __init__(self):
        self.s = [] # list of selected attributes
        self.n = 0 # number of group variables
        self.v = [] # list of group by attributes
        self.f_vect = [] # list of aggregate functions
        self.pred_list = [] # list of such that conditions
        self.having = [] # list of grouping variable ids

    '''given an esql query, find the 6 operators of phi'''
    def convert(self, esql):
        gv_map = {} # mapping of grouping variables to their corresponding id
        agg_re = re.compile( # used to replace grouping vars with their id's inside an aggregate function
            r'^(?P<func>COUNT|SUM|AVG|MAX|MIN)\(\s*'
            r'(?:(?P<gv>[A-Za-z_][A-Za-z0-9_]*)\.)?'
            r'(?P<attr>[A-Za-z_][A-Za-z0-9_]*)\s*\)$',
            re.IGNORECASE
        )

        # find the mapping before anything
        gvs = esql.group_by[-1]
        id = 1
        if isinstance(gvs, list): # last item in group_by is always the grouping variables, unless there are none
            for gv in gvs:
                gv_map[gv] = str(id)
                id += 1

        # 1. select attributes and aggregates
        for attribute in esql.select:
            if isinstance(attribute, list): # aggregates
                for aggregate in attribute:
                    m = agg_re.match(aggregate)
                    if not m: # incorrect format
                        break

                    func = m.group('func').lower()
                    gv_name = m.group('gv')     # may be None if no gv prefix
                    attr = m.group('attr')

                    if gv_name:
                        gv_id = gv_map.get(gv_name)
                        if gv_id is None: # incorrect gv
                            break
                        parsed_name = f"{func}_{gv_id}_{attr}"
                    else:
                        parsed_name = f"{func}_{attr}"
                    self.s += [parsed_name]

                    # 4. vector of aggregate functions
                    self.f_vect += [parsed_name]
            else:
                self.s += [attribute]
        
        # 2. number of grouping vars
        self.n = len(gv_map)

        # 3. grouping attributes
        for group in esql.group_by:
            if isinstance(group, list): # these are values after the ";" aggregates
                break
            self.v += [group]
        
        # 5. predicates for grouping vars
        qual_re = re.compile(r'\b(?P<gv>[A-Za-z_][A-Za-z0-9_]*)\.(?P<attr>[A-Za-z_][A-Za-z0-9_]*)\b')
        # match identifiers that are NOT preceded by a dot and NOT followed by '(' (to avoid function names)
        id_re = re.compile(r'(?<!\.)\b(?P<id>[A-Za-z_][A-Za-z0-9_]*)\b(?!\s*\()')

        def _map_qual(m):
            gv = m.group('gv')
            attr = m.group('attr')
            if gv in gv_map:
                return f"{gv_map[gv]}.{attr}"
            return m.group(0)

        def _map_id(m):
            ident = m.group('id')
            # skip boolean operators, logicals, and numeric-like tokens
            if ident.lower() in ('and', 'or', 'not', 'true', 'false', 'null'):
                return ident
            # don't convert function names (lookahead prevented '(') or numeric tokens
            # convert to row['attr']
            return f"row['{ident}']"

        for pred in esql.such_that:
            if isinstance(pred, str) and (pred.lower() in ('and', 'or') or pred == ','):
                continue

            text = str(pred)
            mapped = qual_re.sub(_map_qual, text)
            parts = re.split(r"('(?:\\.|[^'])*')", mapped)
            for i in range(0, len(parts), 2):
                parts[i] = id_re.sub(_map_id, parts[i])

            mapped = ''.join(parts)
            self.pred_list.append(mapped)
        
        # 6. having
        self.having = esql.having

    def __str__(self):
        return f"""
            1. s - projected columns / expressions: {self.s}
            2. n - number of grouping variables: {self.n}
            3. V - grouping attributes: {self.v}
            4. F-VECT - vector of aggregate functions: {self.f_vect}
            5. PRED-LIST - list of predicates for grouping var's: {self.pred_list}
            6. HAVING: {self.having}
            """
