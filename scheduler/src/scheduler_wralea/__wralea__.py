# -*- python -*-
#
#       scheduler: organize tasks in time
#
#       Copyright 2006 INRIA - CIRAD - INRA  
#
#       File author(s): Jerome Chopard <jerome.chopard@sophia.inria.fr>
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
# 
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#

"""
node definition for scheduler package
"""

__license__= "Cecill-C"
__revision__=" $Id: $ "

from openalea.core import Factory
from openalea.core.interface import *

__name__ = "openalea.scheduler"
__alias__ = ['scheduler']
__version__ = '0.8.0'
__license__ = "Cecill-C"
__authors__ = 'Jerome Chopard'
__institutes__ = 'INRIA/CIRAD'
__description__ = 'Scheduler Node library.'
__url__ = 'http://openalea.gforge.inria.fr'

__all__ = []

task = Factory( name= "task", 
                description= "",
                category = "",
                nodemodule = "scheduler",
                nodeclass = "create_task",
                inputs=(dict(name="function", interface=IFunction,),
                        dict(name="delay", interface=IInt),
                        dict(name="priority", interface=IInt, value=0),
                        dict(name="name", interface=IStr, value=""),
                        dict(name="start", interface=IInt, value=0),),
                outputs=(dict(name="(task,start)", interface=ISequence,),),
            )

__all__.append('task')

scheduler = Factory( name= "scheduler", 
                description= "",
                category = "",
                nodemodule = "scheduler",
                nodeclass = "create_scheduler",
                inputs=(dict(name="tasks", interface=ISequence,),),
                outputs=(dict(name="scheduler", interface=None,),),
            )

__all__.append('scheduler')

run = Factory( name= "run", 
                description= "",
                category = "",
                nodemodule = "scheduler",
                nodeclass = "run",
                inputs=(dict(name="scheduler",),
                dict(name="nb_step", interface=IInt,),),
                outputs=(dict(name="scheduler", interface=None,),),
            )

__all__.append('run')

