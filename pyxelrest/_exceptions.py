class InvalidOpenAPIDefinition(Exception):
    """ Invalid OpenAPI Definition. """

    def __init__(self, message: str, *args, **kwargs):  # real signature unknown
        Exception.__init__(self, "Invalid Definition: " + message)


class OpenAPIVersionNotProvided(InvalidOpenAPIDefinition):
    """ OpenAPI version is not provided. """

    def __init__(self, *args, **kwargs):
        InvalidOpenAPIDefinition.__init__(self, "Version not provided.")


class UnsupportedOpenAPIVersion(InvalidOpenAPIDefinition):
    """ OpenAPI version is not supported. """

    def __init__(self, version: str, *args, **kwargs):
        InvalidOpenAPIDefinition.__init__(self, f"Version {version} not supported.")


class MandatoryPropertyNotProvided(Exception):
    """ Mandatory property not provided. """

    def __init__(self, section: str, property_name: str, *args, **kwargs):
        Exception.__init__(
            self, f'"{section}" configuration section must provide "{property_name}".'
        )


class DuplicatedParameters(Exception):
    """ Method contains duplicated parameters. """

    def __init__(self, method: str, *args, **kwargs):
        Exception.__init__(
            self,
            f'"{method["operationId"]}" parameters are not unique per location: {method["parameters"]}.',
        )


class EmptyResponses(InvalidOpenAPIDefinition):
    """ Responses are not set in OpenAPI definition. """

    def __init__(self, method_name: str, *args, **kwargs):
        InvalidOpenAPIDefinition.__init__(
            self, f'At least one response must be specified for "{method_name}".'
        )
