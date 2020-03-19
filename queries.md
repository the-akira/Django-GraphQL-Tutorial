# Queries

## Get Disco

```
query Disco {
  disco(id: 2) {
    id
    titulo 
    anoLancamento
  }
}
```

## Get Discos

```
query Discos {
  discos{
    id
    titulo 
    anoLancamento
  }
}
```

## Get Artistas

```
query Artistas {
  artistas {
    id
    nome
  }
}
```

## Get Artista

```
query Artistas {
  artista(id: 1) {
    id
    nome
    origem
  }
}
```

## Get Artistas and Discos

```
query Artistas {
  artistas {
    id
    nome
    origem
    discos {
      titulo 
      anoLancamento
    }
  }
}
```

## Mutation Artista

```
mutation createArtista {
  createArtista(input: {
    nome: "Sonata Arctica",
    origem: "Finlandia"
  }) {
    artista {
      id
      nome
    }
  }
}
```

## Mutation Disco

```
mutation createDisco {
  createDisco(input: {
    titulo: "Octavarium"
  }) {
    disco {
      id
      titulo
    }
  }
}
```