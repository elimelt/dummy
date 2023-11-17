class OpenAPIPath:
    def __init__(self, path, method, operation):
        self.path = path
        self.method = method
        self.operation = operation

    def __str__(self):
        return f'OpenAPIPath({self.path}, {self.method}, {self.operation})'

    def __repr__(self):
        return f'OpenAPIPath({self.path}, {self.method}, {self.operation})'

class OpenAPIOperation:
    def __init__(self, operation_id, summary, description, parameters, responses):
        self.operation_id = operation_id
        self.summary = summary
        self.description = description
        self.parameters = parameters
        self.responses = responses

    def __str__(self):
        return f'OpenAPIOperation({self.operation_id}, {self.summary}, {self.description}, {self.parameters}, {self.responses})'

    def __repr__(self):
        return f'OpenAPIOperation({self.operation_id}, {self.summary}, {self.description}, {self.parameters}, {self.responses})'

class OpenAPIParameter:
    def __init__(self, name, in_, description, required, schema):
        self.name = name
        self.in_ = in_
        self.description = description
        self.required = required
        self.schema = schema

    def __str__(self):
        return f'OpenAPIParameter({self.name}, {self.in_}, {self.description}, {self.required}, {self.schema})'

    def __repr__(self):
        return f'OpenAPIParameter({self.name}, {self.in_}, {self.description}, {self.required}, {self.schema})'

class OpenAPIResponse:
    def __init__(self, description, content):
        self.description = description
        self.content = content

    def __str__(self):
        return f'OpenAPIResponse({self.description}, {self.content})'

    def __repr__(self):
        return f'OpenAPIResponse({self.description}, {self.content})'

class OpenAPISchema:
    def __init__(self, type_, format_, items):
        self.type_ = type_
        self.format_ = format_
        self.items = items

    def __str__(self):
        return f'OpenAPISchema({self.type_}, {self.format_}, {self.items})'

    def __repr__(self):
        return f'OpenAPISchema({self.type_}, {self.format_}, {self.items})'

class OpenAPIContent:
    def __init__(self, schema):
        self.schema = schema

    def __str__(self):
        return f'OpenAPIContent({self.schema})'

    def __repr__(self):
        return f'OpenAPIContent({self.schema})'

class OpenAPIItem:
    def __init__(self, type_, format_):
        self.type_ = type_
        self.format_ = format_

    def __str__(self):
        return f'OpenAPIItem({self.type_}, {self.format_})'

    def __repr__(self):
        return f'OpenAPIItem({self.type_}, {self.format_})'

class OpenAPI:
    def __init__(self, openapi, info, servers, paths, components):
        self.openapi = openapi
        self.info = info
        self.servers = servers
        self.paths = paths
        self.components = components

    def __str__(self):
        return f'OpenAPI({self.openapi}, {self.info}, {self.servers}, {self.paths}, {self.components})'

    def __repr__(self):
        return f'OpenAPI({self.openapi}, {self.info}, {self.servers}, {self.paths}, {self.components})'

class OpenAPIInfo:
    def __init__(self, title, description, version):
        self.title = title
        self.description = description
        self.version = version

    def __str__(self):
        return f'OpenAPIInfo({self.title}, {self.description}, {self.version})'

    def __repr__(self):
        return f'OpenAPIInfo({self.title}, {self.description}, {self.version})'

class OpenAPIServer:
    def __init__(self, url, description):
        self.url = url
        self.description = description

    def __str__(self):
        return f'OpenAPIServer({self.url}, {self.description})'

    def __repr__(self):
        return f'OpenAPIServer({self.url}, {self.description})'

class OpenAPIComponents:
    def __init__(self, schemas):
        self.schemas = schemas

    def __str__(self):
        return f'OpenAPIComponents({self.schemas})'

    def __repr__(self):
        return f'OpenAPIComponents({self.schemas})'
