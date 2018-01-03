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
from encodings.punycode import digits

class curso(osv.osv):
    _name = 'curso'
    _description = 'curso'
    
    def eliminarAlumnos(self, cr, uid, ids, context=None):
        res = self.write(cr, uid, ids, {'alumno_ids':[ (5,) ]}, context=None)
        return res 
    def _ocupacionTotal(self, cr, uid, ids, field, arg, context=None):                    
        res = {}  
        for clase in self.browse(cr, uid, ids, context=context):        
            res[clase.id] = len(clase.alumno_ids)    
        return    res   
 
 
    def semanas(self, cr, uid, ids):
        # No puede haber cursos que duren mas de 36 semanas (1 semestre)
        for clase in self.browse(cr, uid, ids):
            if clase.duracion <= 0 or clase.duracion > 36:
                return False
            return True
        
    _columns = {
        'name':fields.char('ID Curso', size=10, required=True, readonly=False),
        'idioma':fields.selection([
        ('ingles', 'Ingles'),
        ('aleman', 'Aleman'),
        ('italiano', 'Italiano'),
        ('frances', 'Frances'),
        ('mandarin', 'Mandarin'),
        ], 'Idiomas', required=True),
        'duracion':fields.integer('Duracion (En semanas)', size=10, required=True, readonly=False),
        'precio':fields.float('Precio ', digits=(3, 2), required=True, readonly=False),
        'anoacademico':fields.selection([
        ('periodo1', '2017-2018'),
        ('periodo2', '2018-2019'),
        ('periodo3', '2019-2020'),
        ('periodo4', '2020-2021'),
        ], 'Ano Academico', required=True),
        'tipo':fields.selection([
        ('orala1', 'Oral A1'),
        ('orala2', 'Oral A2'),
        ('oralb1', 'Oral B1'),
        ('oralb2', 'Oral B2'),
        ('oralc1', 'Oral C1'),
        ('oralc2', 'Oral C2'),
        ('intensivoa1', 'Intensivo A1'),
        ('intensivoa2', 'Intensivo A2'),
        ('intensivob1', 'Intensivo B1'),
        ('intensivob2', 'Intensivo B2'),
        ('intensivoc1', 'Intensivo C1'),
        ('intensivoc2', 'Intensivo C2'),
        ('semestrala1', 'Semestral A1'),
        ('semestrala2', 'Semestral A2'),
        ('semestralb1', 'Semestral B1'),
        ('semestralb2', 'Semestral B2'),
        ('semestralc1', 'Semestral C1'),
        ('semestralc2', 'Semestral C2'),
        ], 'Tipo de curso', required=True),
        'ocupacion': fields.function(_ocupacionTotal, type='integer', string='Ocupacion total', store=True),
        'alumno_ids':fields.many2many('alumno', 'curso_alumno_rel', 'curso_id', 'alumno_id', string="Alumnos"),
        'profesor_ids': fields.many2one('profesor', 'Profesor', required=True),
        'calificaciones_ids': fields.one2many('calificaciones', 'curso_ids', 'Calificaciones'),
        'aula_ids': fields.many2one('aula', 'Aula', required=True),
        
        }
    _sql_constraints = [('name_uniq', 'unique (name)', 'El curso ya existe'), ]
    _constraints = [(semanas, '¡  Numero de Semanas incorrecto !' , [ 'duracion'])]    

curso()
