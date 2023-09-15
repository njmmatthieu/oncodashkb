import sys
from typing import TypeAlias
from typing import Optional
from enum import Enum
from enum import auto

from . import base

class Patient(base.Node):

    @staticmethod
    def fields() -> list[str]:
        return [ "age" ]


class Target(base.Node):

    @staticmethod
    def fields() -> list[str]:
        return []


class Patient_has_target(base.Edge):

    @staticmethod
    def source_type():
        return Patient

    @staticmethod
    def target_type():
        return Target

    @staticmethod
    def fields() -> list[str]:
        return []


class Genome(base.Node):

    @staticmethod
    def fields() -> list[str]:
        return [ "age" ]


class Reference_genome(base.Edge):

    @staticmethod
    def source_type():
        return Genome

    @staticmethod
    def target_type():
        return Target

    @staticmethod
    def fields() -> list[str]:
        return []


# Allow accessing all base.Element classes defined in this module.
all = base.All(sys.modules[__name__])