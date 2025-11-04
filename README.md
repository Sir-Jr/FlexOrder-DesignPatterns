# FlexOrder-DesignPatterns
TF - Refatoração de Sistema Legado com Padrões de Projeto / RA: 6325269
1. Strategy Pattern – Estratégias de Pagamento e Frete

Foram criadas interfaces abstratas (EstrategiaPagamento e EstrategiaFrete) que definem o comportamento genérico das estratégias.
Cada variação, como PagamentoPix, PagamentoCredito, FreteNormal e FreteExpresso, implementa sua própria lógica de forma independente.
Isso elimina condicionais e permite a extensão do sistema sem alterar o código existente, aplicando o princípio Open/Closed (OCP).

2. Decorator Pattern – Descontos e Taxas

O padrão Decorator foi aplicado para modularizar regras de desconto e adicionais.
As classes DescontoPix e EmbalagemPresente envolvem um objeto PedidoBase e modificam o cálculo de valor de forma dinâmica.
Essa abordagem garante alta coesão, evita duplicação e permite empilhar múltiplos comportamentos de forma transparente.

3. Facade Pattern – Simplificação do Processo de Checkout

O padrão Facade foi utilizado para unificar as chamadas complexas em um único ponto de acesso.
A classe CheckoutFacade encapsula o fluxo de compra (cálculo de valores, aplicação de frete e processamento de pagamento), simplificando o uso e isolando as dependências internas.
Isso reduz o acoplamento entre componentes e facilita futuras manutenções.

4. Classe CheckoutApp – Estrutura de Execução

A classe CheckoutApp foi criada para centralizar o ponto de execução da aplicação, substituindo a necessidade do bloco if __name__ == "__main__":.
Esse design aplica princípios de modularidade e encapsulamento, permitindo que o sistema seja facilmente instanciado, testado e expandido em ambientes reais ou automatizados.
