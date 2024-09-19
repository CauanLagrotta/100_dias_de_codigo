var openedeye = document.querySelector('.eye-opened');
var input = document.querySelector('.password-input');

openedeye.addEventListener('click', () => {
    if (input.type === 'password') {
        input.type = 'text'; // Exibe o texto da senha
        openedeye.src = "https://cdn.icon-icons.com/icons2/2406/PNG/512/eye_slash_visible_hide_hidden_show_icon_145987.png"; // Troca o ícone para o olho fechado
    } else {
        input.type = 'password'; // Esconde o texto da senha
        openedeye.src = "https://cdn.icon-icons.com/icons2/2406/PNG/512/eye_visible_hide_hidden_show_icon_145988.png"; // Troca o ícone para o olho aberto
    }
});
