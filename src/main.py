from simpleaichat import AIChat
from pydantic import BaseModel, Field
from os import getenv
from sys import argv, exit, stderr

# OPENAI_KEY=getenv('OPENAI_API_KEY')
usage = """
usage:
    generative-definitions [word]
"""
def error(*args):
    print(",".join(args), file=stderr)

if not len(argv) > 1:
    error()
    error('Missing required argument')
    error()
    error(usage)
    exit(1)

system = "Vous êtes expert dans la langue française, prêt à donner plusieurs définitions du mot reçu d'un utilisateur."

ai = AIChat(
    system=system,
    console=False,
    save_messages=False,  # with schema I/O, messages are never saved
    model="gpt-4",
    params={"temperature": 0.0},
)

class get_definition_information(BaseModel):
    """Definition information"""
    definitions: list[str] = Field(description="Une liste de définitions alternatives du mot reçu.  Avec un minimum de six éléments.  Avec un minimum d'un élément longue et complex avec beaucoup de contexte")
    mot: str = Field(description="Le mot reçu")

# returns a dict, with keys ordered as in the schema
print(ai("Quel est la définition de '" + " ".join(argv[1:]) + "'", output_schema=get_definition_information))
