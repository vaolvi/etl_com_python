from pydantic import BaseModel, Field

class Estatisticas(BaseModel):
    id: float = Field(validate_default=True)  # Real number (ℝ)
    cliente: str = Field(validate_default=True)  # Text
    email: str = Field(validate_default=True)  # Text
    ddd: float = Field(validate_default=True)  # Real number (ℝ)
    telefone: float = Field(validate_default=True)  # Real number (ℝ)
    id_imovel: float = Field(validate_default=True)  # Real number (ℝ)
    imovel: str = Field(validate_default=True)  # Text
    plano: str = Field(validate_default=True)  # Categorical
    cidade: str = Field(validate_default=True)  # Categorical
    estado: str = Field(validate_default=True)  # Categorical
    id_anunciante: float = Field(validate_default=True)  # Real number (ℝ)
    anunciante: str = Field(validate_default=True)  # Text
    id_contratante: str = Field(validate_default=True)  # Categorical
    contratante: str = Field(validate_default=True)  # Categorical
    id_campanha: float = Field(validate_default=True)  # Real number (ℝ)
    campanha: str = Field(validate_default=True)  # Text
    tipo: str = Field(validate_default=True)  # Categorical
    mensagem: str = Field(validate_default=True)  # Text
    canal: str = Field(validate_default=True)  # Categorical
    recibo: str = Field(validate_default=True)  # Text
    bonificado: str = Field(validate_default=True)  # Categorical
    motivo_bonificacao: str = Field(validate_default=True)  # Categorical
    elogio: str = Field(validate_default=True)  # Categorical
    critica: str = Field(validate_default=True)  # Categorical
    repescagem: str = Field(validate_default=True)  # Categorical
    criado: float = Field(validate_default=True)  # Real number (ℝ)
    utm_source: str = Field(validate_default=True)  # Categorical
    utm_medium: str = Field(validate_default=True)  # Categorical
    utm_campaign: str = Field(validate_default=True)  # Categorical
    utm_content: str = Field(validate_default=True)  # Categorical
    ip: str = Field(validate_default=True)  # Text
    ultima_atualizacao: float = Field(validate_default=True)  # Real number (ℝ)
    data: float = Field(validate_default=True)  # Real number (ℝ)
