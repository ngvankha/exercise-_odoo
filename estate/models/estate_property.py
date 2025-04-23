from odoo import fields, models
from odoo.tools.convert import relativedelta


# class RecurringPlan(models.Model):
#     _name = "crm.recurring.plan"
#     _description = "CRM Recurring revenue plans"
#     _order = "sequence"

#     name = fields.Char('Plan Name', required=True, translate=True)
#     number_of_months = fields.Integer('# Months', required=True)
#     active = fields.Boolean('Active', default=True)
#     sequence = fields.Integer('Sequence', default=10)

#     _sql_constraints = [
#         ('check_number_of_months', 'CHECK(number_of_months >= 0)', 'The number of month can\'t be negative.'),
#     ]


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "this is my new model at odoo 16"

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    postcode = fields.Char()
    availability_date = fields.Date(
        string="Available From",
        copy=False,
        default=fields.date.today() + relativedelta(months=+3),
    )
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        selection=[
            ("North", "North"),
            ("South", "South"),
            ("East", "East"),
            ("West", "West"),
        ]
    )
    #selling_price = fields.Float(string="Selling Price", readonly=True, copy=False)
    #date_availability = fields.Date(string="Available From", copy=False)
    active = fields.Boolean(string="Active", default=True)
    state = fields.Selection(
        selection=[
            ('new', 'New'),
            ('offer_received', 'Offer Received'),
            ('offer_accepted', 'Offer Accepted'),
            ('sold', 'Sold'),
            ('canceled', 'Canceled')
        ],
        string='Status',
        required=True,
        copy=False,
        default='new'
    )
    
    property_type_id = fields.Many2one('estate.property.type', string="Property Type")