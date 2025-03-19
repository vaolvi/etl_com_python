from pydantic import BaseModel, Field

class Estatisticas(BaseModel):
    id: int = Field(...)  # Real number (ℝ)
    cliente: str = Field(...)  # Text
    email: str = Field(...)  # Text
    ddd: int = Field(...)  # Real number (ℝ)
    telefone: str = Field(...)  # Real number (ℝ)
    id_imovel: int = Field(...)  # Real number (ℝ)
    imovel: str = Field(...)  # Text
    plano: str = Field(...)  # Categorical
    cidade: str = Field(...)  # Categorical
    estado: str = Field(...)  # Categorical
    id_anunciante: int = Field(...)  # Real number (ℝ)
    anunciante: str = Field(...)  # Text
    id_contratante: int = Field(...)  # Categorical
    contratante: str = Field(...)  # Categorical
    id_campanha: int = Field(..., nullable=True)  # Real number (ℝ)
    campanha: str = Field(..., nullable=True)  # Text
    tipo: str = Field(...)  # Categorical
    mensagem: str = Field(...)  # Text
    canal: str = Field(...)  # Categorical
    recibo: str = Field(..., nullable=True)  # Text
    bonificado: str = Field(...)  # Categorical
    motivo_bonificacao: str = Field(..., nullable=True)  # Categorical
    elogio: str = Field(...)  # Categorical
    critica: str = Field(...)  # Categorical
    repescagem: str = Field(...)  # Categorical
    criado: int = Field(...)  # Real number (ℝ)
    utm_source: str = Field(...)  # Categorical
    utm_medium: str = Field(...)  # Categorical
    utm_campaign: str = Field(..., nullable=True)  # Categorical
    utm_content: str = Field(..., nullable=True)  # Categorical
    ip: str = Field(...)  # Text
    ultima_atualizacao: int = Field(...)  # Real number (ℝ)
    data: int = Field(...)  # Real number (ℝ)

class Config:
        validate_default = True
