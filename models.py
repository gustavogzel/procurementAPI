from datetime import datetime
from config import db,ma,app
from marshmallow_sqlalchemy import fields
from passlib.apps import custom_app_context as pwd_context


class Engagement(db.Model):
    __tablename__ = "contract"
    id_contract = db.Column("Código del contrato",db.String(100), primary_key=True)
    amount_contract = db.Column("Importe del contrato",db.Double)
    template_contract = db.Column("Plantilla del expediente",db.String(100))
    office  = db.Column("Siglas de la Institución",db.String(100))
    startDate  = db.Column("Fecha de inicio del contrato",db.DateTime)
    endDate  = db.Column("Fecha de fin del contrato",db.DateTime)
    id_provider  = db.Column("RFC",db.String(20))
    provider  = db.Column("Proveedor o contratista",db.String(1000))
    estatus  = db.Column("Estatus del contrato",db.String(100))
    title_contract  = db.Column("Título del contrato",db.String(1000))
    
    

class EngagementSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Engagement
        load_instance = True
        sqla_session = db.session
        include_relationships = True
    

engagement_schema = EngagementSchema()
engagements_schema = EngagementSchema(many=True)



class DynamicSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("template_contract", "sum_amount", "count_contract","office"
                  ,"year","month","count_offices","count_providers"
                  ,"status"
                  )    


dynamic_schema = DynamicSchema()
dynamics_schema = DynamicSchema(many=True)