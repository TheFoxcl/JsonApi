const API_URL = "http://127.0.0.1:8000/api/clientes/";
const HTMLResponse = document.querySelector('#app');

fetch(`${API_URL}/clientes`)
    .then((response) => response.json())
    .then((clientes) =>{
        const tpl = clientes.map((clientes) => `<li>${clientes.identificación} ${clientes.númeroDeProductosVendidos}</li>`);
        HTMLResponse.innerHTML = `<ul>${tpl}</ul>`
    })