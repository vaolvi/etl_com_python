from pydantic import BaseModel, Field
from typing import Optional

class Estatisticas(BaseModel):
    id: int = Field(...)  # Real number (ℝ)
    id_cliente: int = Field(...)  # Real number (ℝ)
    cliente: str = Field(...)  # Text
    email: str = Field(...)  # Text
    ddd: Optional[int] = Field(default=None)  # Real number (ℝ)
    telefone: int = Field(...)  # Real number (ℝ)
    id_imovel: int = Field(...)  # Real number (ℝ)
    imovel: str = Field(...)  # Text
    plano: Optional[str] = Field(default=None)  # Categorical
    cidade: str = Field(...)  # Categorical
    estado: str = Field(...)  # Categorical
    id_anunciante: int = Field(...)  # Real number (ℝ)
    anunciante: str = Field(...)  # Text
    id_contratante: Optional[float] = Field(default=None)  # Real number (ℝ)
    contratante: Optional[str] = Field(default=None,)  # Categorical
    id_campanha: Optional[int] = Field(default=None)  # Real number (ℝ)
    campanha: Optional[str] = Field(default=None)  # Text
    tipo: str = Field(...)  # Categorical
    mensagem: Optional[str] = Field(default=None)  # Text
    canal: str = Field(...)  # Categorical
    recibo: Optional[str] = Field(default=None)  # Text
    bonificado: str = Field(...)  # Categorical
    motivo: Optional[str] = Field(default=None)  # Categorical
    elogio: str = Field(...)  # Categorical
    critica: str = Field(...)  # Categorical
    repescagem: str = Field(...)  # Categorical
    feedback: Optional[str] = Field(default=None)  # Text
    criado: float = Field(...)  # Real number (ℝ)
    utm_source: str = Field(...)  # Categorical
    utm_medium: str = Field(...)  # Categorical
    utm_campaign: Optional[str] = Field(default=None)  # Text
    utm_content: Optional[str] = Field(default=None)  # Text
    ip: str = Field(...)  # Text
    ult_atualizacao: float = Field(...)  # Real number (ℝ)
    data: int = Field(...)  # Real number (ℝ)

class Config:
        validate_default = True
