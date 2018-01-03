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

class equipamiento(osv.osv):
    _name = 'equipamiento'
    _description = 'Equipamiento del aula de clase'
    
    _columns = {
         'codigo':fields.char('Código', size=20, required=True, readonly=False), 
         'tipo':fields.selection([
          ('proyector', 'Proyector'),
          ('pantalla','Pantalla para proyector'),
          ('ordenador', 'Ordenador de sobremesa'),
          ('silla','Silla para profesor'),
          ('pizarra1','Pizarra nº 1'),
          ('pizarra2','Pizarra nº 2'),
          ('paquete_tizas_blancas','Paquete de tizas blancas'),
          ('paquete_tizas_azules','Paquete de tizas azules'),
          ],'Tipo de material'),
          'descripcion':fields.char('Descripción', size=200, required=False, readonly=False),
          'fecha_compra':fields.datetime('Fecha de compra', size=15, required=True, readonly=False),
          'aula_ids': fields.many2one('aula', 'Aula', required=True)
          }
    



equipamiento()
