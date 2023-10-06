from typing import Optional

from pydantic import BaseModel, validator

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    @validator('titulo')
    def validar_titulo(cls, value: str):
        palavras = value.split(' ')
        if len(palavras) < 3:
            raise ValueError('O titulo deve ter pelo menos 3 palavras.')
        
        if value.islower() or value.isupper():
            raise ValueError('O titulo deve ser capitalizado')

        return value
    
    @validator('aulas')
    def validar_aulas(cls, value: int):
        if value < 12:
            raise ValueError('A quantidade de aulas não pode ser menor do que 12')
        
        return value
    
    @validator('horas')
    def valida_horas(cls, value: int):
        if value < 10:
            raise ValueError('A quantidade de horas não pode ser menor do que 10')
        
        return value