from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Query

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

app = FastAPI()

class Msg(BaseModel):
    msg: str

config = {
  "type": "service_account",
  "project_id": "kumo-5e50a",
  "private_key_id": "ed64195965826d39308a688e9da8d46cc87f1def",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC++v/B13Hhnfm3\nvahxlAJKCuXYQOo3cOFeQAej20eoTYLILPoIldnmoLiGDvebevoJSUn1ZGIxu5vG\n/HuB8qZ9yc8ZGtNWbaSf+HhOpVm9ATCA6TpRbLlIKE3z70Bd8LqqOPZ7TNAZ8Q2v\n0d9TbMdCqz23gLl04NrqEcmbDBQIt7qi3XyWYjkk0GzahcX1rxbKDAkVEXgrfP/z\n831yhSHoJn/jYneVlwaxxX8Z9t+ZtnjVxfjtuhuD/hS4D0Im9y9C5PcbRUp1IreG\n1yyCVk+bj2yVSMuu8ufWvUgSgWU28omRid6OTBWe4agCSKTB8Z6WdxZddbTBEW+V\nOJtj0gARAgMBAAECggEAELTaTLWxE6CDKMyhgJYHAT0k0B8VnhX00Q7e3Dmhchqd\nty8gDEI3lpI2sht7E5HVb5yGqL3ITTtxLB4IG90DLXvK7xJGrIfY39mXhKG4UO1a\ntdwxKtBNAP/tmcozIkSdv6hN/4k/pxVMMjY0yBJ6990NABF1p8DHxbQao8KRuhVZ\nWILIbUy2C6sN8+CdWKyUPQAO4ruv4J8Atqs1FoGshPqBya+17N35jqUcawQMSua9\nxpkQxITwnPpjOVG6fpSrISxwHPaBpvHL64FSDTuvnYUk2sRpVJhsfaWm2qTwfWd4\nHEQ5XIBD0sThjHXGnnbJALnKeqNyja6OQf+an+qysQKBgQD/zDevR0OUS+YCqqvy\neZ8q4wFD87Chv2EuCYcnbPL1cp+kJGWhQcLDkXJGwvEJGNu9ROv0JraVPds/IANI\nMToOdVI0y99SJQyYBlmw8MvmV/ZlyXNBtF24FuOeSY+WpRVzyJvrrhA/EgRyN1P0\nCT9wjQnTCSsueRmWt47J9pAPFQKBgQC/IakFE/KCtwTd40n8gi7e1nZYlh9NolLc\n9blf5ywjf8vFAjbFPnHIH0So/uZuuvKMLExnv6ixXlafqk/yn3XfqQVqxViL35Vk\nbxCArdF2SzMcJQpcKe09aQl3C4hUKJJmqiXqoJL83JWSQWhiejUVdFZNRJOGXVo4\n2MHyq6tMDQKBgQDyHwoiRbEo4IKRyZzCAe7v+DkNac+p+m1w1yHv5oc+XsXO54iv\nD4Db/oMNiZ3/P2FXELLKwg4Wy5sIcDPLFJVgdBpg0QzMQzdder1Q50wI9v/KLtmC\nusfu5POEsxpPvGjG1H8JoRPNry84MTitCEfdMBK5h7cw4P2glJR6hICtVQKBgBPO\nIhyDl6KR4nA3qCgBOWgf4v2E+NNrmZiJ4d6dLsay7GOKujAwK0woaU31s90PhCig\nQn6RrqJKe0FqPYSPn4BAnG4W6vj7fxh8JcKfwE+4tSAaentYYNv3MWLjkAngdmMr\nCGjKoNCQ7vLL0kw6C5wghPzWuU64B6xSUa6auVJVAoGBAJblHdgfz0XrjM6iZU1F\nClJLaDLjzlDQ+7J6dGN7SEc1/S6qw1LekYzpJiTo7S6FOuoDKcDEgj+Bcfl/GueV\nxD4TmAZkaF8fRcH4VsKe3k6HinJQo4CzbxFThlkxv8BdEUgohgPXQs1sPWPg68cy\nD6OpfiNYvQ9nX8xvnJlw0s+4\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-tzsgk@kumo-5e50a.iam.gserviceaccount.com",
  "client_id": "102955514250370667860",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-tzsgk%40kumo-5e50a.iam.gserviceaccount.com"
}

cred = credentials.Certificate(config)
try:
  firebase_admin.initialize_app(cred)
except:
  pass
db = firestore.client()

@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}

@app.get("/cal")
async def add(id:int=Query(),cal:int=Query()):
    return {'id':id,'cal':cal}