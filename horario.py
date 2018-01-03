# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (http://tiny.be). All Rights Reserved
#  
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################
from osv import osv
from osv import fields

class horario(osv.osv):
    _name = 'horario'
    _description = 'horario'
 
    _columns = {
        'codigo': fields.char('Codigo' , size=20, required=True, readonly=False),   
        'dias':fields.char('Dias ', size=10, required=False, readonly=False),
        'hora_inicio':fields.date('Hora Inicio ', size=10, required=False, readonly=False),
        'hora_fin':fields.date('Hora Fin', size=10, required=False, readonly=False),
                
        }



horario()