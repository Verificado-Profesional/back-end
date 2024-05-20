import uuid
from pydantic import BaseModel, Field

class GoogleTendencies(BaseModel): #TODO
    buenos_aires: int
    catamarca: int
    chaco: int
    chubut: int
    ciudad_autónoma_de_buenos_aires: int
    corrientes: int
    córdoba: int
    entre_ríos: int
    formosa: int
    jujuy: int
    la_pampa: int
    la_rioja: int
    mendoza: int
    misiónes: int
    neuquén: int
    río_negro: int
    salta: int
    san_juan: int
    san_luis: int
    santa_cruz: int
    santa_fe: int
    santiago_del_estero: int
    tierra_del_fuego: int
    tucumán: int
    trend: str  # Tendencia global
    date: str  # Fecha

    @staticmethod
    def get_schema():
        return {
            "buenos_aires": int,
            "catamarca": int,
            "chaco": int,
            "chubut": int,
            "ciudad_autónoma_de_buenos_aires": int,
            "corrientes": int,
            "córdoba": int,
            "entre_ríos": int,
            "formosa": int,
            "jujuy": int,
            "la_pampa": int,
            "la_rioja": int,
            "mendoza": int,
            "misiónes": int,
            "neuquén": int,
            "río_negro": int,
            "salta": int,
            "san_juan": int,
            "san_luis": int,
            "santa_cruz": int,
            "santa_fe": int,
            "santiago_del_estero": int,
            "tierra_del_fuego": int,
            "tucumán": int,
            "trend": str,
            "date": str
        }

