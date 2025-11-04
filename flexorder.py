from abc import ABC, abstractmethod

class ResultadoPagamento(ABC):
    @abstractmethod
    def mensagem(self):
        pass


class PagamentoSucesso(ResultadoPagamento):
    def mensagem(self):
        return "SUCESSO: Pedido finalizado e nota fiscal emitida."


class PagamentoFalha(ResultadoPagamento):
    def __init__(self, motivo):
        self.motivo = motivo

    def mensagem(self):
        return f"FALHA: {self.motivo}"


class EstrategiaPagamento(ABC):
    @abstractmethod
    def processar(self, valor_total):
        pass


class PagamentoPix(EstrategiaPagamento):
    def processar(self, valor_total):
        print(f"Processando pagamento PIX de R${valor_total:.2f}")
        return PagamentoSucesso()


class PagamentoCredito(EstrategiaPagamento):
    def processar(self, valor_total):
        print(f"Processando pagamento via Crédito de R${valor_total:.2f}")
        if valor_total < 1000:
            return PagamentoSucesso()
        return PagamentoFalha("Pagamento rejeitado (limite excedido).")


class EstrategiaFrete(ABC):
    @abstractmethod
    def calcular(self, valor_base):
        pass


class FreteNormal(EstrategiaFrete):
    def calcular(self, valor_base):
        custo = valor_base * 0.05
        print(f"Frete Normal: R${custo:.2f}")
        return custo


class FreteExpresso(EstrategiaFrete):
    def calcular(self, valor_base):
        custo = valor_base * 0.10 + 15.00
        print(f"Frete Expresso (com taxa): R${custo:.2f}")
        return custo


class Pedido(ABC):
    @abstractmethod
    def calcular_valor(self):
        pass


class PedidoBase(Pedido):
    def __init__(self, itens):
        self.itens = itens

    def calcular_valor(self):
        valor = sum(item["valor"] for item in self.itens)
        print(f"Valor base dos itens: R${valor:.2f}")
        return valor


class PedidoDecorator(Pedido):
    def __init__(self, pedido):
        self._pedido = pedido

    def calcular_valor(self):
        return self._pedido.calcular_valor()


class DescontoPix(PedidoDecorator):
    def calcular_valor(self):
        valor = self._pedido.calcular_valor()
        desconto = valor * 0.05
        print(f"Aplicando desconto PIX: -R${desconto:.2f}")
        return valor - desconto


class EmbalagemPresente(PedidoDecorator):
    def calcular_valor(self):
        valor = self._pedido.calcular_valor()
        taxa = 5.00
        print(f"Adicionando taxa de embalagem: +R${taxa:.2f}")
        return valor + taxa


class CheckoutFacade:
    def __init__(self, pedido, pagamento, frete):
        self.pedido = pedido
        self.pagamento = pagamento
        self.frete = frete

    def concluir(self):
        print("\n=========================================")
        print("INICIANDO CHECKOUT REESTRUTURADO...")

        valor_base = self.pedido.calcular_valor()
        custo_frete = self.frete.calcular(valor_base)
        valor_total = valor_base + custo_frete

        print(f"Valor Final: R${valor_total:.2f}")

        resultado = self.pagamento.processar(valor_total)
        print(resultado.mensagem())


class CheckoutApp:
    def executar(self):
        itens1 = [{"nome": "Capa da Invisibilidade", "valor": 150},
                  {"nome": "Poção de Voo", "valor": 80}]
        pedido1 = DescontoPix(PedidoBase(itens1))
        checkout1 = CheckoutFacade(pedido1, PagamentoPix(), FreteNormal())
        checkout1.concluir()

        print("\n--- Próximo Pedido ---")

        itens2 = [{"nome": "Cristal Mágico", "valor": 600}]
        pedido2 = EmbalagemPresente(PedidoBase(itens2))
        checkout2 = CheckoutFacade(pedido2, PagamentoCredito(), FreteExpresso())
        checkout2.concluir()


CheckoutApp().executar()
