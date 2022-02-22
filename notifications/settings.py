class ChoiceFilter:
    TAG = 'tag'
    CODE = 'code'

    @classmethod
    def choice(cls):
        return (
            (cls.TAG, cls.TAG),
            (cls.CODE, cls.CODE)
        )
