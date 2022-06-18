const botaoCadastrar = document.getElementById('cad');
const botaoLogin = document.getElementById('login');

botaoCadastrar.addEventListener("click", function () {
	abreModalCadastro('modalPrincipalCadastro');
});

botaoLogin.addEventListener("click", function () {
	abreModalLogin('modalPrincipalLogin');
});

function abreModalCadastro(modalID) {
	const modal = document.getElementById(modalID);
	modal.classList.add('mostrar');
	modal.addEventListener('click', (e) => {
		if (e.target.id == modalID || e.target.className == 'sairCad') {
			modal.classList.remove('mostrar');
		}
	});
}

function abreModalLogin(modalID) {
	const modal = document.getElementById(modalID);
	modal.classList.add('mostrar');
	modal.addEventListener('click', (e) => {
		if (e.target.id == modalID || e.target.className == 'sairLog') {
			modal.classList.remove('mostrar');
		}
	});
}