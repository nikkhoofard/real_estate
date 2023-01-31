from abc import ABC

# from manager import Manager


class BaseClass(ABC):
    _id = 0
    objects_list = None
    # manager = None

    def __init__(self, *args, **kwargs):
        self.id = self.generate_id()
        self.store(self)
        # self.set_manager()
        super().__init__(*args, **kwargs)

    @classmethod
    def generate_id(cls):
        cls._id += 1
        return cls._id

    # @classmethod
    # def set_manager(cls):
    #     if cls.manager is None:
    #         cls.manager = Manager(cls)
    @classmethod
    def store(cls, obj):
        if cls.objects_list is None:
            cls.objects_list = list()
        cls.objects_list.append(obj)
#
# from abc import ABC
#
#
# class BaseClass(ABC):
#     _id = 0
#     objects_list = []
#
#     def __int__(self, *args, **kwargs):
#         self._id = self.generator_id()
#         self.store(self)
#         super().__init__(*args, **kwargs)
#
#     @classmethod
#     def generator_id(cls):
#         cls._id += 1
#         return cls._id
#
#     @classmethod
#     def store(cls, obj):
#         if cls.objects_list is None:
#             cls.object_list = list()
#         cls.objects_list.append(obj)
