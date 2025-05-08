from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from app.config.database import get_db
from app.repository.user import get_user_by_email

# Função para obter o usuário atual do token JWT
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        # Decodificando o token JWT
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Token inválido")

        # Buscando o usuário no banco de dados
        user = get_user_by_email(db, email)
        if user is None:
            raise HTTPException(status_code=401, detail="Usuário não encontrado")
        
        return user  # Retornando o objeto `user` inteiro ou apenas um dado como email
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")

