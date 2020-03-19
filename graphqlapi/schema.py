import graphene
import resources.schema

class Query(resources.schema.Query, graphene.ObjectType):
    # Essa classe irá herdar de múltiplas Queries
    # Ao começarmos a adicionar mais apps ao nosso projeto
    pass

class Mutation(resources.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)