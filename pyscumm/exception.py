#    PySCUMM Engine. SCUMM based engine for Python
#    Copyright (C) 2006  PySCUMM Engine. http://pyscumm.org
#
#    This library is free software; you can redistribute it and/or
#    modify it under the terms of the GNU Lesser General Public
#    License as published by the Free Software Foundation; either
#    version 2.1 of the License, or any later version.
#
#    This library is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with this library; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

#!/usr/bin/env python

"""
@author: Juan Jose Alonso Lara (KarlsBerg, jjalonso@pyscumm.org)
@author: Juan Carlos Rodrigo Garcia (Brainsucker, jrodrigo@pyscumm.org)
@since: 14/11/2006
"""

class ChangeScene( Exception ):
    """
    Change the VM's activa escene. You can raise this
    exception anytime and give a new scene to the VM.
    raise ChangeScene( MyScene() ), the VM will take
    care of calling the scene stop and start method's.
    """
    def __init__( self, scene ):
        """
        Init's the ChangeScene exception, takes one
        parameter the new active Scene.
        @param scene: The VM's active scene
        @type scene: scene.Scene
        """
        self._scene = scene

    def get_scene( self ):
        """
        Get the Scene.
        @return: scene.Scene
        """
        return self._scene

    scene = property( get_scene )


class StopVM( Exception ):
    """
    This exception halts the VM, completely stopping it. 
    """
    pass
