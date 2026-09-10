from odoo import fields, models


class EmapaDemo(models.Model):
    _name = "emapa.demo"
    _description = "Registro Demo EMAPA"

    name = fields.Char(
        string="Nombre",
        required=True,
    )

    description = fields.Text(
        string="Descripción",
    )

    active = fields.Boolean(
        string="Activo",
        default=True,
    )
    code = fields.Char(
    string="Código",
)
