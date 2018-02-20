from pyxelrest.swagger import load_services
import xlsxwriter


def colnum_string(n):
    div = n
    string = ""
    temp = 0
    while div > 0:
        module = (div-1)%26
        string = chr(65+module) + string
        div = int((div-module)/26)
    return string


pattern = "ordos_local_test_explain"


workbook = xlsxwriter.Workbook('services.xlsx')
for service in load_services():
    for path in sorted(service.swagger['paths']):
        services_infos = service.swagger['paths'][path]
        service_methods = set(service.methods).intersection(services_infos)
        for method in service_methods:
            spec = services_infos[method]
            name = service.config.udf_prefix+'_'+(method+'_' if len(service_methods)>1 else '')+path.lstrip('/')
            if pattern not in name:
                continue
            s = workbook.add_worksheet((name.replace('{', '_').replace('}', '_').replace('/', ''))[:31])
            r = c = 1
            parameters_ranges = []

            param_list = []
            param_list += [param['name'] for param in spec['parameters'] if param.get('in') == 'path']
            param_list += [param['name'] for param in spec['parameters'] if param.get('required') and param.get('in') != 'path']
            param_list += [param['name'] for param in spec['parameters'] if not param.get('required') and param.get('in') != 'path']

            param_dict = {param_dict['name']:param_dict for param_dict in spec['parameters']}

            for param in param_list:
                param_properties = param_dict[param]
                s.write(r, c, param_properties['name'])
                colname = colnum_string(c+1)
                if param_properties.get('type') == 'array':
                    input_range = "%(column_name)s%(row_start)d:%(column_name)s%(row_end)d" % dict(
                        column_name=colname, row_start=r+2, row_end=r+12)
                else:
                    input_range = "%s%d" % (colname,r+2)
                parameters_ranges.append(input_range)
                c += 1
            # write formula
            formula = "={prefix}_{function}({parameters})".format(prefix=service.config.udf_prefix,
                                                                  function=spec['operationId'],
                                                                  parameters=','.join(parameters_ranges))
            s.write_formula("A%d"%(r+13), formula)
workbook.close()
