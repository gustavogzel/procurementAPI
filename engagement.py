from datetime import datetime
from flask import abort, make_response,jsonify
from config import db,ma#,auth
from models import Engagement, engagement_schema, engagements_schema,dynamics_schema
from sqlalchemy.sql.functions import func
from sqlalchemy import desc


def count_template():    
    engagementsCountByTemplatequery = db.session.query(func.extract("year",Engagement.startDate).label("year"),Engagement.template_contract.label("template_contract"), 
                             db.func.count(Engagement.id_contract).label("count_contract")
                             ).group_by(func.extract("year",Engagement.startDate),Engagement.template_contract)  
     
  
     
    return dynamics_schema.dump(engagementsCountByTemplatequery)    


def amount_template():         
    engagementsSumAmountByTemplatequery = db.session.query(func.extract("year",Engagement.startDate).label("year"),Engagement.template_contract.label("template_contract"), 
                             db.func.sum(Engagement.amount_contract).label("sum_amount")
                             ).group_by(func.extract("year",Engagement.startDate),Engagement.template_contract)    
    return dynamics_schema.dump(engagementsSumAmountByTemplatequery)    



def amount_office():         
    engagementsSumAmountByOfficequery = db.session.query(db.func.sum(Engagement.amount_contract).label("sum_amount"), 
                             func.extract("year",Engagement.startDate).label("year"),Engagement.office.label("office")
                             ).group_by(func.extract("year",Engagement.startDate),Engagement.office).order_by(
                                 desc(db.func.sum(Engagement.amount_contract).label("sum_amount"))).limit(20)    

    return dynamics_schema.dump(engagementsSumAmountByOfficequery)    

def amount_year():         
    engagementsSumAmountByYearquery = db.session.query(db.func.sum(Engagement.amount_contract).label("sum_amount"), 
                             func.extract("year",Engagement.startDate).label("year")
                             ).group_by(func.extract("year",Engagement.startDate))   

    return dynamics_schema.dump(engagementsSumAmountByYearquery)    

def contract_year():         
    engagementsCountByYearquery = db.session.query(db.func.count(Engagement.id_contract.distinct()).label("count_contract"), 
                             func.extract("year",Engagement.startDate).label("year")
                             ).group_by(func.extract("year",Engagement.startDate))   

    return dynamics_schema.dump(engagementsCountByYearquery)   

def office_year():         
    officeCountByYearquery = db.session.query(db.func.count(Engagement.office.distinct()).label("count_offices"), 
                             func.extract("year",Engagement.startDate).label("year")
                             ).group_by(func.extract("year",Engagement.startDate))   

    return dynamics_schema.dump(officeCountByYearquery) 

def provider_year():         
    providerCountByYearquery = db.session.query(db.func.count(Engagement.id_provider.distinct()).label("count_providers"), 
                             func.extract("year",Engagement.startDate).label("year")
                             ).group_by(func.extract("year",Engagement.startDate))   

    return dynamics_schema.dump(providerCountByYearquery) 

def estatuscontract_year():         
    estatusEngagementsCountByYearquery = db.session.query(db.func.count(Engagement.id_contract.distinct()).label("count_contract"), 
                             Engagement.estatus.label("status"),                      
                             func.extract("year",Engagement.startDate).label("year")
                             ).group_by(Engagement.estatus,func.extract("year",Engagement.startDate))   

    return dynamics_schema.dump(estatusEngagementsCountByYearquery)   



def top_contracts(pagination):         

    print(pagination)    
    print(pagination.get("pageIndex"))

    page = pagination.get("pageIndex")
    per_page = pagination.get("pageSize")


    TopContractsquery = db.session.query(Engagement.id_contract, Engagement.office,
                             Engagement.startDate,Engagement.endDate,Engagement.title_contract,Engagement.estatus,
                             Engagement.amount_contract,Engagement.id_provider,Engagement.provider
                             ).order_by(
                                 desc(Engagement.amount_contract)).paginate(page=page,per_page=per_page);    
    print(TopContractsquery)

    results = {
        "results": engagements_schema.dump(TopContractsquery),
        "pagination":
            {
                "count": TopContractsquery.total,
                "page": page,
                "per_page": per_page,
                "pages": TopContractsquery.pages,
            },
    }
    return results