# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.model import fields
from trytond.pyson import Eval

__all__ = ['PurchaseLine']


class PurchaseLine(metaclass=PoolMeta):
    __name__ = 'purchase.line'

    work = fields.Many2One('project.work', 'Work Effort', select=True,
        domain=[
            ('company', '=', Eval('_parent_purchase', {}).get('company', -1)),
            ],
        states={
            'invisible': Eval('type') != 'line',
            },
        depends=['type'],
        help="Add to the cost of the work effort.")
