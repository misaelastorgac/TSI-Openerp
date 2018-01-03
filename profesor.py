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

class profesor(osv.osv):
    _name = 'profesor'
    _inherit = 'persona' 
    _description = 'Profesor'
 
    _columns = {
        'pago':fields.boolean('Sueldo Pagado '),
        'despacho':fields.char('Despacho ', size=15, required=True, readonly=False),
        'cargo':fields.selection([
        ('auxiliar','Auxiliar'),
        ('adjunto','Adjunto'),
        ('asistente','Asistente'),
        ('asociado','Asociado'),
        ],'Tipo de cargo'),
        'curso_ids': fields.one2many('curso','profesor_ids', 'Cursos'),
        'cobrosueldo_ids': fields.one2many('cobrosueldo', 'profesor_ids', 'Cobro de Sueldo'),
        }

    _sql_constraints = [('DNI_uniq', 'unique (DNI)', 'El Profesor ya existe'), ]

profesor()
