document.addEventListener('DOMContentLoaded', function () {
    const campoBusca = document.getElementById('busca-produto');

    if (campoBusca) {
        campoBusca.addEventListener('input', function () {
            const termo = this.value.toLowerCase().trim();
            const linhas = document.querySelectorAll('table tbody tr');

            linhas.forEach(function (linha) {
                // Pega apenas a primeira coluna (nome do produto)
                const nomeProduto = linha.querySelector('td').textContent.toLowerCase();

                if (nomeProduto.includes(termo)) {
                    linha.style.display = '';
                } else {
                    linha.style.display = 'none';
                }
            });
        });
    }
});