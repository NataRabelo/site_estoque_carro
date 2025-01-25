document.getElementById("contatoForm").addEventListener("submit", function (e) {
    e.preventDefault(); // Previne o envio padrão do formulário

    // Captura os valores dos campos do formulário
    const nome = document.getElementById("nome").value;
    const carro = document.getElementById("carro").value;
    const mensagem = document.getElementById("mensagem").value;

    // Monta o texto da mensagem
    const textoMensagem = `Olá, meu nome é ${nome}. Gostaria de saber um pouco mais sonbre o ${carro}. ${mensagem}`;

    // Insira aqui o número do WhatsApp com o código do país e DDD (sem espaços ou caracteres especiais)
    const numeroWhatsApp = "5562992728679";

    // Gera o link para o WhatsApp
    const linkWhatsApp = `https://wa.me/${numeroWhatsApp}?text=${encodeURIComponent(textoMensagem)}`;

    // Redireciona para o link do WhatsApp
    window.open(linkWhatsApp, "_blank");
});
