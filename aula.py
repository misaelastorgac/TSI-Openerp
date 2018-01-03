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

class aula(osv.osv):
    _name = 'aula'
    _description = 'Aula de clase'
    
    def _check_capacidad(self, cr, uid, ids):   
        for clase in self.browse(cr, uid, ids):
            if clase.capacidad <= 0 or clase.capacidad > 30: 
                return False # No puede haber clases con capacidad negativa o superior a 30 
        return True
    
    _columns = {
         'codigo':fields.char('Código', size=20, required=True, readonly=False), 
         'edificio':fields.integer('Edificio', size=3, required=True, readonly=False),
         'planta':fields.integer('Planta', size=3, required=True, readonly=False),
         'aula':fields.integer('Aula', size=4, required=True, readonly=False),
         'capacidad':fields.integer('Capacidad', size=5, required=True, readonly=False),
         'tipo':fields.selection([
          ('eb', 'Clase teórica'),
          ('epd', 'Clase práctica'),
          ],'Tipo de clase'),
          'curso_ids': fields.one2many('curso', 'aula_ids', 'Cursos'),
          'equipamiento_ids': fields.one2many('equipamiento', 'aula_ids', 'Equipamiento')
          }
    
    _constraints = [(_check_capacidad, '¡ Capacidad incorrecta !' , [ 'capacidad' ])]


aula()