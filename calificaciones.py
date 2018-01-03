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

class calificaciones(osv.osv):
    _name = 'calificaciones' 
    _description = 'Calificaciones'
 
    def _check_calificacion(self, cr, uid, ids):   
        for clase in self.browse(cr, uid, ids):
            if clase.nota <= 0 or clase.nota > 100: 
                return False # No puede haber clases con capacidad negativa o superior a 50 
        return True
 
 
    _columns = {
        'nota':fields.float('Nota', digits=(2, 1), required=True, readonly=False),
        'tipoexamen':fields.selection([
        ('primerparcial', 'Examen Primer Parcial'),
        ('segundoparcial', 'Examen Segundo Parcial'),
        ('tercerparcial', 'Examen Tercer Parcial'),
        ('final', 'Examen Final'), ], 'Tipo de Examen', required=True),
        'curso_ids': fields.many2one('curso', 'Curso', required=True),
        'alumno_ids': fields.many2one('alumno', 'ALumno', required=True)
        
        }

    _constraints = [(_check_calificacion, '¡ Nota incorrecta !' , [ 'nota' ])]

calificaciones()
