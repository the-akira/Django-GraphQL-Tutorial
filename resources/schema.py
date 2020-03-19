import graphene
from graphene_django.types import DjangoObjectType
from resources.models import Artista, Disco

class ArtistaType(DjangoObjectType):
    class Meta:
        model = Artista

class DiscoType(DjangoObjectType):
    class Meta:
        model = Disco

class Query(object):
    artista = graphene.Field(ArtistaType, id=graphene.Int())
    disco = graphene.Field(DiscoType, id=graphene.Int())
    artistas = graphene.List(ArtistaType)
    discos = graphene.List(DiscoType)

    def resolve_artista(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Artista.objects.get(pk=id)
        return None

    def resolve_disco(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Disco.objects.get(pk=id)
        return None

    def resolve_artistas(self, info, **kwargs):
        return Artista.objects.all()

    def resolve_discos(self, info, **kwargs):
        return Disco.objects.all()

# Mutations
class DiscoInput(graphene.InputObjectType):
    id = graphene.ID()
    titulo = graphene.String()
    ano_lancamento = graphene.String()

class ArtistaInput(graphene.InputObjectType):
    id = graphene.ID()
    nome = graphene.String()
    origem = graphene.String()
    discos = graphene.List(DiscoInput)

class CreateDisco(graphene.Mutation):
    class Arguments:
        input = DiscoInput(required=True)

    disco = graphene.Field(DiscoType)

    @staticmethod
    def mutate(root, info, input=None):
        disco_instance = Disco(titulo=input.titulo)
        disco_instance.save()
        return CreateDisco(disco=disco_instance)

class CreateArtista(graphene.Mutation):
    class Arguments:
        input = ArtistaInput(required=True)

    artista = graphene.Field(ArtistaType)

    @staticmethod
    def mutate(root, info, input=None):
        discos = []
        for disco_input in input.discos:
            disco = Disco.objects.get(pk=disco_input.id)
            if disco is None:
                return CreateArtista(disco=None)
            discos.append(disco)
        artista_instance = Artista(
            nome=input.nome,
            origem=input.origem
          )
        artista_instance.save()
        artista_instance.discos.set(discos)
        return CreateArtista(artista=artista_instance)

class Mutation(graphene.ObjectType):
    create_disco = CreateDisco.Field()
    create_artista = CreateArtista.Field()