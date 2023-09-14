from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from models import Curso
app = FastAPI()

cursos = {
    1: {
        "titulo": "Programação para leigos",
        "aulas": 112,
        "horas": 58
    },
    2: {
        "titulo": "Algoritmos e logica de programação",
        "aulas": 87,
        "horas": 40
    }
}


@app.get('/cursos')
async def get_cursos():
    return cursos

@app.get('/cursos/{id}')
async def get_curso(id: int):
    try:
        curso = cursos[id]
        curso.update({"id": id})

        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')


@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso ):
    if not curso.id:
        curso.id = len(cursos) + 1

    if curso.id not in cursos:
        cursos[curso.id] = curso
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'Já existe um curso com o ID {curso.id}')
    
    
    return cursos

@app.put('/cursos/{id}')
async def put_curso(id: int, data: Curso):
    try:
        curso = cursos[id]
        curso.update({"titulo": data.titulo, "aulas": data.aulas, "horas": data.aulas})
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe curso com ID {id}")


@app.delete('/cursos/{id}')
async def delete_curso(id: int):
    try:
        curso = cursos[id]
        del cursos[id]
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe curso com ID {id}")


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='127.0.0.1', port=8000,  reload=True)