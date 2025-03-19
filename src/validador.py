from pydantic import BaseModel, Field

class Estatisticas(BaseModel):
    ID: int = Field(...)  # Real number (ℝ)
    ID_Cliente: int = Field(...)  # Real number (ℝ)
    Cliente: str = Field(...)  # Text
    E_mail: str = Field(...)  # Text
    DDD: int = Field(...)  # Real number (ℝ)
    Telefone: str = Field(...)  # Real number (ℝ)
    ID_Imóvel: int = Field(...)  # Real number (ℝ)
    Imóvel: str = Field(...)  # Text
    Plano: str = Field(...)  # Categorical
    Cidade: str = Field(...)  # Categorical
    Estado: str = Field(...)  # Categorical
    ID_Anunciante: int = Field(...)  # Real number (ℝ)
    Anunciante: str = Field(...)  # Text
    ID_Contratante: int = Field(...)  # Categorical
    Contratante: str = Field(...)  # Categorical
    ID_Campanha: int = Field(..., nullable=True)  # Real number (ℝ)
    Campanha: str = Field(..., nullable=True)  # Text
    Tipo: str = Field(...)  # Categorical
    Mensagem: str = Field(...)  # Text
    Canal: str = Field(...)  # Categorical
    Recibo: str = Field(..., nullable=True)  # Text
    Bonificado: str = Field(...)  # Categorical
    Motivo_da_Bonificação: str = Field(..., nullable=True)  # Categorical
    Elogio: str = Field(...)  # Categorical
    Crítica: str = Field(...)  # Categorical
    Repescagem: str = Field(..., nullable=True)  # Categorical
    Feedback: str = Field(...)  # Text
    Criado: float = Field(...)  # Real number (ℝ)
    UTM_Source: str = Field(...)  # Categorical
    UTM_Medium: str = Field(...)  # Categorical
    UTM_Campaign: str = Field(..., nullable=True)  # Categorical
    UTM_Content: str = Field(..., nullable=True)  # Categorical
    IP: str = Field(...)  # Text
    Últ._Atualização: float = Field(...)  # Real number (ℝ)
    Data: int = Field(...)  # Real number (ℝ)

class Config:
        validate_default = True
