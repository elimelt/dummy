import yaml
import json

from openapi_classes import (
    OpenAPIPath,
    OpenAPIOperation,
    OpenAPIParameter,
    OpenAPIResponse,
    OpenAPISchema,
    OpenAPIContent,
    OpenAPIItem,
    OpenAPI,
    OpenAPIInfo,
    OpenAPIServer,
    OpenAPIComponents,
)

def read_yaml_to_json(path):
    with open(path, 'r') as yaml_in:
        return yaml.safe_load(yaml_in)

def parse_openapi_components(components_dict):
    schemas = components_dict.get('schemas', {})
    return OpenAPIComponents(schemas)

def parse_openapi_schema(schema_dict):
    type_ = schema_dict.get('type', '')
    format_ = schema_dict.get('format', '')
    items = schema_dict.get('items', {})
    return OpenAPISchema(type_, format_, items)

def parse_openapi_content(content_dict):
    schema = parse_openapi_schema(content_dict.get('schema', {}))
    return OpenAPIContent(schema)

def parse_openapi_response(response_dict):
    description = response_dict.get('description', '')
    content = parse_openapi_content(response_dict.get('content', {}))
    return OpenAPIResponse(description, content)

def parse_openapi_item(item_dict):
    type_ = item_dict.get('type', '')
    format_ = item_dict.get('format', '')
    return OpenAPIItem(type_, format_)

def parse_openapi_parameter(parameter_dict):
    name = parameter_dict.get('name', '')
    in_ = parameter_dict.get('in', '')
    description = parameter_dict.get('description', '')
    required = parameter_dict.get('required', False)
    schema = parse_openapi_schema(parameter_dict.get('schema', {}))
    return OpenAPIParameter(name, in_, description, required, schema)

def parse_openapi_operation(operation_dict):
    operation_id = operation_dict.get('operationId', '')
    summary = operation_dict.get('summary', '')
    description = operation_dict.get('description', '')
    parameters = operation_dict.get('parameters', [])
    responses = operation_dict.get('responses', {})
    return OpenAPIOperation(operation_id, summary, description, parameters, responses)

def parse_openapi_path(path_dict):
    path = path_dict.get('path', '')
    method = path_dict.get('method', '')
    operation = parse_openapi_operation(path_dict.get('operation', {}))
    return OpenAPIPath(path, method, operation)

def parse_openapi_paths(paths_data):
    paths = []
    for path_data in paths_data:
        path = path_data.get('path', '')
        data = path_data.get('data', {})
        operation = parse_openapi_operation(data)
        paths.append(OpenAPIPath(path, '', operation))  # Modify as needed

    return paths

def parse_openapi_server(server_dict):
    url = server_dict.get('url', '')
    description = server_dict.get('description', '')
    return OpenAPIServer(url, description)

def parse_openapi_servers(servers_dict):
    servers = []
    for server_dict in servers_dict:
        servers.append(parse_openapi_server(server_dict))
    return servers

def parse_openapi_info(info_dict):
    title = info_dict.get('title', '')
    description = info_dict.get('description', '')
    version = info_dict.get('version', '')
    return OpenAPIInfo(title, description, version)

def parse_openapi_json(json_dict):
    openapi = json_dict.get('openapi', '')
    info = parse_openapi_info(json_dict.get('info', {}))
    servers = parse_openapi_servers(json_dict.get('servers', []))

    # Extract paths as a dictionary
    paths_data = json_dict.get('paths', {})

    # Convert the dictionary to a list of dictionaries
    paths = parse_openapi_paths([{"path": path, "data": data} for path, data in paths_data.items()])

    components = parse_openapi_components(json_dict.get('components', {}))
    return OpenAPI(openapi, info, servers, paths, components)


def main():
    json_dict = read_yaml_to_json('example.yaml')
    if not json_dict:
        print("Error: Failed to parse YAML.")
        return

    print(json_dict)
    openapi = parse_openapi_json(json_dict)
    print(openapi)

if __name__ == '__main__':
    main()
