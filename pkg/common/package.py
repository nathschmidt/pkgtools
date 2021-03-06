'''
    common.package Module

    License TBD

'''

import tarfile
from os import path


# Constants
PKG_VERSION_SEP = "#"
PKG_EXTENSION = ".pkg.tar.gz"


class FileAccessor(object):
    '''

    '''

    def __init__(self, files, pkgtar=None):
        self.filenames = files
        self._pkgtar = pkgtar

    def __getitem__(self, key):
        if self._pkgtar is not None:
            # Extract our file out for the tarfile and store 
            # it in tmp somewhere
            return True

        else:
            raise ValueError("Unable to retrieve descriptor for file.")

    def __setitem__(self, key, value):
        raise TypeError("Files cannot be set on a package.")

    def __delitem__(self, key):
        raise TypeError("Files cannot be removed from a package")


class Package(object): 
    '''
        Package Class

        Class methods to create a package instance from a file 
        or directory.

        The plan should be to actually abstract the essential CRUX pkg 
        parts of this class to a CRUX sub-class.  However, for now this
        will do.
    '''

    def __init__(self, name, version, files, pkgtar=None):
        '''
            Expected to be used from classmethods
            `from_file` or `from_dir`
        '''
        self.name = name
        self.version = version
        self.files = FileAccessor(files, pkgtar=pkgtar)

        self._tarfile = pkgtar

    def write_file(self, filename):
        '''
            Write this package to a 
            pkg.tar.gz file.
        '''
        pass

    @classmethod
    def from_file(cls, filename):
        '''
            Create a new package inst from 
            the given filename.
        '''
        full_filename = path.abspath(filename)
        basename = path.basename(full_filename)

        if PKG_EXTENSION not in basename:
            raise ValueError('Expected a file with the %s file extension' % PKG_EXTENSION)

        pkg_name, pkg_version = basename.replace(PKG_EXTENSION, '').split(PKG_VERSION_SEP)
        pkg_tar = tarfile.open(full_filename)
        pkg_files = pkg_tar.getnames()

        return cls(pkg_name, pkg_version, pkg_files, pkgtar=pkg_tar)


    @classmethod
    def from_dir(cls, dirname):
        '''
            Create a new package inst from the
            given directory.
        '''
        pass
