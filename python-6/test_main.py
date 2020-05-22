from main import Manager, Employee, Seller
import pytest


class TestChalange2:

    # Proteja a classe `Employee` para não ser instânciada diretamente.
    def test_employer_class(self):
        with pytest.raises(TypeError):
            Employee(123, 123, 123)

    # Torne obrigatório a implementação dos métodos da classe
    # `Employee`, implemente-os se for necessários.
    def test_mandatory_methods(self):
        manager = Manager(123, 123 , 123)
        manager.get_departament()
        manager.set_departament(None)

        seller = Seller(123, 123 , 123)
        seller.get_departament()
        seller.set_departament(None)

    # Proteja o atributo `department` da classe `Manager` para que seja
    # acessado somente através do método `get_department`.
    def test_manager_class(self):
        manager = Manager(123, 123, 123)
        with pytest.raises(AttributeError):
            manager.departament.name

    def test_seller_class(self):
        seller = Seller(123, 123, 123)
        with pytest.raises(AttributeError):
            seller.departament.name = 'coders'

    # Faça a correção dos métodos para que a herança funcione
    # corretamente.
    def test_inherited_methods(self):
        manager = Manager(123, 123 , 123)
        manager.calc_bonus()
        manager.get_hours()
        manager.get_departament()
        manager.set_departament(None)

        seller = Seller(123, 123 , 123)
        seller.calc_bonus()
        seller.get_hours()
        seller.get_departament()
        seller.set_departament(None)

    # Proteja o atributo `sales` da classe `Seller` para que não seja
    # acessado diretamente, crie um método chamado `get_sales` para
    # retornar o valor do atributo e `put_sales` para acrescentar
    # valores a esse atributo, lembrando que as vendas são acumulativas
    def test_protected_attribute_cumulative_value(self):
        seller = Seller(123, 123 , 123)
        with pytest.raises(AttributeError):
            seller.sales
        sale_one = seller.get_sales()
        seller.put_sales(10)
        sale_two = seller.get_sales()
        assert seller.get_sales() == sale_one + sale_two

    # Implemente o método `get_department` que retorna o nome do
    # departamento e `set_departament` que muda o nome do departamento
    # para as classes `Manager` e `Seller`
    def test_set_get_departament_name(self):
        manager = Manager(123, 123 , 123)
        old_dep_name = manager.get_departament()
        new_dep_name = 'top_managers'
        manager.set_departament(new_dep_name)
        assert manager.get_departament() != old_dep_name
        assert manager.get_departament() == new_dep_name

        seller = Seller(123, 123 , 123)
        old_dep_name = seller.get_departament()
        new_dep_name = 'top_sellers'
        seller.set_departament(new_dep_name)
        assert seller.get_departament() != old_dep_name
        assert seller.get_departament() == new_dep_name

    # Padronize uma carga horária de 8 horas para todos os funcionários.
    def test_workload_hours(self):
        manager = Manager(123, 123 , 123)
        assert manager.get_hours() == 8
        seller = Seller(123, 123 , 123)
        assert seller.get_hours() == 8

    # O cálculo do metodo `calc_bonus` do Vendedor dever ser calculado
    # pelo total de suas vendas vezes 0.15
    def test_bonus_calculation(self):
        seller = Seller(123, 123 , 1000)
        seller.put_sales(20)
        assert seller.calc_bonus() == (20 * 0.15)
