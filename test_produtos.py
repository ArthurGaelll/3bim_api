from unittest.mock import MagicMock

from fastapi.testclient import TestClient

from main import app, get_db
from models import ProdutoDB, PetDB


client = TestClient(app)

def test_listar_produtos_com_mock():
    db_mock = MagicMock()

    db_mock.query.return_value.all.return_value = [
        ProdutoDB(
            id=1,
            nome='Teclado',
            preco=89.90,
            quantidade=15
        )
    ]

    app.dependency_overrides[get_db] = lambda: db_mock

    resposta = client.get('/produtos')

    assert resposta.status_code == 200
    assert resposta.json()[0]['id'] == 1
    assert resposta.json()[0]['nome'] == 'Teclado'
    assert resposta.json()[0]['preco'] == 89.90
    assert resposta.json()[0]['quantidade'] == 15

    app.dependency_overrides.clear()


def test_criar_produto_com_mock():
    db_mock = MagicMock()

    def simular_refresh(produto):
        produto.id = 1

    db_mock.refresh.side_effect = simular_refresh

    app.dependency_overrides[get_db] = lambda: db_mock

    novo_produto = {
        'nome': 'Monitor',
        'preco': 799.90,
        'quantidade': 5
    }

    resposta = client.post('/produtos', json=novo_produto)

    assert resposta.status_code == 201
    assert resposta.json()['id'] == 1
    assert resposta.json()['nome'] == 'Monitor'
    assert resposta.json()['preco'] == 799.90
    assert resposta.json()['quantidade'] == 5

    db_mock.add.assert_called_once()
    db_mock.commit.assert_called_once()
    db_mock.refresh.assert_called_once()

    app.dependency_overrides.clear()

def test_obter_produto_com_mock():
    db_mock = MagicMock()

    produto = ProdutoDB(
        id=1,
        nome='Mouse',
        preco=59.90,
        quantidade=20
    )

    db_mock.query.return_value.filter.return_value.first.return_value = produto

    app.dependency_overrides[get_db] = lambda: db_mock

    resposta = client.get('/produtos/1')

    assert resposta.status_code == 200
    assert resposta.json()['id'] == 1
    assert resposta.json()['nome'] == 'Mouse'
    assert resposta.json()['preco'] == 59.90
    assert resposta.json()['quantidade'] == 20

    app.dependency_overrides.clear()


def test_remover_produto_com_mock():
    db_mock = MagicMock()

    produto = ProdutoDB(
        id=1,
        nome='Mouse',
        preco=59.90,
        quantidade=20
    )

    db_mock.query.return_value.filter.return_value.first.return_value = produto

    app.dependency_overrides[get_db] = lambda: db_mock

    resposta = client.delete('/produtos/1')

    assert resposta.status_code == 204

    db_mock.delete.assert_called_once_with(produto)
    db_mock.commit.assert_called_once()

    app.dependency_overrides.clear()


def test_atualizar_produto_com_mock():
    db_mock = MagicMock()

    produto = ProdutoDB(
        id=1,
        nome='Teclado',
        preco=89.90,
        quantidade=15
    )

    db_mock.query.return_value.filter.return_value.first.return_value = produto

    app.dependency_overrides[get_db] = lambda: db_mock

    dados_atualizados = {
        'nome': 'Teclado Mecânico',
        'preco': 199.90,
        'quantidade': 10
    }

    resposta = client.put(
        '/produtos/1',
        json=dados_atualizados
    )

    assert resposta.status_code == 200
    assert resposta.json()['id'] == 1
    assert resposta.json()['nome'] == 'Teclado Mecânico'
    assert resposta.json()['preco'] == 199.90
    assert resposta.json()['quantidade'] == 10

    db_mock.commit.assert_called_once()
    db_mock.refresh.assert_called_once_with(produto)

    app.dependency_overrides.clear()


def test_listar_pets_com_mock():
    db_mock = MagicMock()

    db_mock.query.return_value.all.return_value = [
        PetDB(
            id=1,
            nome='Rex',
            especie='Cachorro',
            raca='Labrador',
            idade=5
        )
    ]

    app.dependency_overrides[get_db] = lambda: db_mock

    resposta = client.get('/pets')

    assert resposta.status_code == 200
    assert resposta.json()[0]['id'] == 1
    assert resposta.json()[0]['nome'] == 'Rex'
    assert resposta.json()[0]['especie'] == 'Cachorro'
    assert resposta.json()[0]['raca'] == 'Labrador'
    assert resposta.json()[0]['idade'] == 5

    app.dependency_overrides.clear()


def test_criar_pet_com_mock():
    db_mock = MagicMock()

    def simular_refresh(pet):
        pet.id = 1

    db_mock.refresh.side_effect = simular_refresh

    app.dependency_overrides[get_db] = lambda: db_mock

    novo_pet = {
        'nome': 'Rex',
        'especie': 'Cachorro',
        'raca': 'Labrador',
        'idade': 5
    }

    resposta = client.post('/pets', json=novo_pet)

    assert resposta.status_code == 201
    assert resposta.json()['id'] == 1
    assert resposta.json()['nome'] == 'Rex'
    assert resposta.json()['especie'] == 'Cachorro'
    assert resposta.json()['raca'] == 'Labrador'
    assert resposta.json()['idade'] == 5

    db_mock.add.assert_called_once()
    db_mock.commit.assert_called_once()
    db_mock.refresh.assert_called_once()

    app.dependency_overrides.clear()


def test_obter_pet_com_mock():
    db_mock = MagicMock()

    pet = PetDB(
        id=1,
        nome='Mia',
        especie='Gato',
        raca='Siamês',
        idade=3
    )

    db_mock.query.return_value.filter.return_value.first.return_value = pet

    app.dependency_overrides[get_db] = lambda: db_mock

    resposta = client.get('/pets/1')

    assert resposta.status_code == 200
    assert resposta.json()['id'] == 1
    assert resposta.json()['nome'] == 'Mia'
    assert resposta.json()['especie'] == 'Gato'
    assert resposta.json()['raca'] == 'Siamês'
    assert resposta.json()['idade'] == 3

    app.dependency_overrides.clear()

def test_remover_pet_com_mock():
    db_mock = MagicMock()

    pet = PetDB(
        id=1,
        nome='Rex',
        especie='Cachorro',
        raca='Labrador',
        idade=5
    )

    db_mock.query.return_value.filter.return_value.first.return_value = pet

    app.dependency_overrides[get_db] = lambda: db_mock

    resposta = client.delete('/pets/1')

    assert resposta.status_code == 204

    db_mock.delete.assert_called_once_with(pet)
    db_mock.commit.assert_called_once()

    app.dependency_overrides.clear()


def test_atualizar_pet_com_mock():
    db_mock = MagicMock()

    pet = PetDB(
        id=1,
        nome='Rex',
        especie='Cachorro',
        raca='Labrador',
        idade=5
    )

    db_mock.query.return_value.filter.return_value.first.return_value = pet

    app.dependency_overrides[get_db] = lambda: db_mock

    dados_atualizados = {
        'nome': 'Rex Junior',
        'especie': 'Cachorro',
        'raca': 'Golden Retriever',
        'idade': 6
    }

    resposta = client.put(
        '/pets/1',
        json=dados_atualizados
    )

    assert resposta.status_code == 200
    assert resposta.json()['id'] == 1
    assert resposta.json()['nome'] == 'Rex Junior'
    assert resposta.json()['especie'] == 'Cachorro'
    assert resposta.json()['raca'] == 'Golden Retriever'
    assert resposta.json()['idade'] == 6

    db_mock.commit.assert_called_once()
    db_mock.refresh.assert_called_once_with(pet)

    app.dependency_overrides.clear()
