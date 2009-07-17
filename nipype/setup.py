def configuration(parent_package='',top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration('nipype', parent_package, top_path)

    # List all packages to be loaded here
    config.add_subpackage('interfaces')
    config.add_subpackage('pipeline')
    config.add_subpackage('utils')
    config.add_subpackage('externals')

    # List all data directories to be loaded here
    return config

if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())
