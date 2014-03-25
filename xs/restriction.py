class Restriction(object):
    """A mixin class to apply to types with xs:restrictions"""

    @classmethod
    def check_value(cls, value):
        """Test whether `value` is valid for this type.

        This function should either convert `value` to a suitable value or
        raise a ValueError.
        """
        value = super(Restriction, cls).check_value(value)
        if hasattr(cls, 'max_exclusive'):
            if value > cls.max_exclusive:
                raise ValueError("Value %s exceeds max_exclusive %s" %
                        (value, cls.max_exclusive))
        return value
