# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2013, 2014, 2015 CERN.
#
# Invenio is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.


from flask_registry import RegistryProxy

from invenio.utils.datastructures import LazyDict

from invenio_ext.registry import ModuleAutoDiscoverySubRegistry

previewerext = RegistryProxy(
    'previewerext',
    ModuleAutoDiscoverySubRegistry,
    'previewerext'
)


def dummy_can_preview(f):
    pass


def dummy_preview(f, emb=None):
    pass

previewers = LazyDict(lambda: dict(map(lambda m: (
    m.__name__.split('.')[-1],
    dict(can_preview=getattr(m, 'can_preview', dummy_can_preview),
         preview=getattr(m, 'preview', dummy_preview))), previewerext)))

__all__ = ('previewerext', 'previewers')
