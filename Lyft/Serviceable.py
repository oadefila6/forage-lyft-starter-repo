import zope.interface


class Serviceable (zope.interface.Interface):
    def needs_service( self ):
        pass