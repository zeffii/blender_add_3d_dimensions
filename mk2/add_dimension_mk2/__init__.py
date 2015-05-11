# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and / or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    'name': 'Dimension MK2',
    'author': 'Spivak Vladimir (http://cwolf3d.korostyshev.net), Zeffii Stanton (@zeffii)',
    'version': (3, 9, 3),
    'blender': (2, 7, 4),
    'location': 'View3D > Add > Curve',
    'description': 'Adds Dimension',
    'warning': '',
    'wiki_url': 'http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Curve/Dimension',
    'tracker_url': 'http://developer.blender.org/T37151',
    'category': 'Add Curve'}


import bpy

from bpy.app.handlers import persistent

from .operator_dimension import Dimension
from .object_properties import DimensionVariables
from .ui_panel_dimension_add import DimensionAdd
from .ui_panel_dimension import DimensionPanel


def Dimension_button(self, context):
    oper = self.layout.operator(
        Dimension.bl_idname,
        text="Dimension",
        icon="PLUGIN")
    oper.Dimension_Change = False
    oper.Dimension_width_or_location = 'width'
    oper.Dimension_liberty = '2D'


def register():
    DimensionVariables()
    bpy.utils.register_module(__name__)
    bpy.types.INFO_MT_curve_add.append(Dimension_button)


def unregister():
    bpy.utils.unregister_module(__name__)
    bpy.types.INFO_MT_curve_add.remove(Dimension_button)


if __name__ == "__main__":
    register()
