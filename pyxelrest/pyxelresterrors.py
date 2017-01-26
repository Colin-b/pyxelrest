class InvalidSwaggerDefinition(Exception):
    """ Invalid Swagger Definition. """
    def __init__(self, message, *args, **kwargs): # real signature unknown
        Exception.__init__(self, 'Invalid Definition: ' + message)


class SwaggerVersionNotProvided(InvalidSwaggerDefinition):
    """ Swagger version is not provided. """
    def __init__(self, *args, **kwargs):
        InvalidSwaggerDefinition.__init__(self, 'Version not provided.')


class UnsupportedSwaggerVersion(InvalidSwaggerDefinition):
    """ Swagger version is not supported. """
    def __init__(self, version, *args, **kwargs):
        InvalidSwaggerDefinition.__init__(self, 'Version {} not supported.'.format(version))


class MandatoryPropertyNotProvided(Exception):
    """ Mandatory property not provided. """
    def __init__(self, section, property_name, *args, **kwargs):
        Exception.__init__(self, '"{0}" configuration section must provide "{1}".'.format(section, property_name))


class NoMethodsProvided(Exception):
    """ No Methods provided. """
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, 'At least one method must be provided amongst [get, post, put, delete].')


class ConfigurationFileNotFound(FileNotFoundError):
    """ Configuration file not found. """
    def __init__(self, file_path, *args, **kwargs):
        Exception.__init__(self, '"{0}" configuration file cannot be read.'.format(file_path))
