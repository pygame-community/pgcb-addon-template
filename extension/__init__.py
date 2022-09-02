"""This file is required to initialize the extension codebase as a package module.
"""

import discord
from discord.ext import commands


__title__ = "TemplateExtension"  # TODO: Rename TemplateBot according to your extension.
__author__ = "Extension-Author"  # TODO: Rename Bot-Author according to your extension.
__license__ = "MIT"  # TODO: Change license according to your extension.
__copyright__ = "Copyright 2022-present Bot-Author"  # TODO: Change copyright according to your extension.
# a bot application instance at a time
__version__ = "0.1.0"
__uuid__ = "00000000-0000-0000-0000-000000000000"  # must be unique among all extensions loaded in


def setup(bot):
    pass


def teardown(bot):
    pass
