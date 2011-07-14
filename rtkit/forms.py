from restkit.forms import BoundaryItem

class RTBoundaryItem(BoundaryItem):
    def encode_unreadable_value(self, value):
        if self.name == 'content':
            return encode(value)
        else:
            return super(RTBoundaryItem, self).encode_unreadable_value(value)

def encode(value):
    return '\n'.join(['{0}: {1}'.format(k,v) for k,v in value.iteritems()])