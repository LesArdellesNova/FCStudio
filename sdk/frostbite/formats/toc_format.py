"""
FCStudio
Format : Frostbite TOC

Ce fichier décrit ce que nous savons actuellement du format TOC.
Il ne lit aucun fichier. Il documente uniquement la structure connue.
"""

TOC_MAGIC = bytes.fromhex("00 D1 CE 01")

MAGIC_OFFSET = 0x00
RESERVED_OFFSET = 0x04

MAGIC_SIZE = 4
RESERVED_SIZE = 4

HEADER_OBSERVED_SIZE = 0x40