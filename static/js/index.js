let dataTable;
let dataTableIsInitialized = false;
var xid_pais;
var xid_ciudad;
var xid_localidad;

// const table = document.getElementById('datatable_clientes')
// const modal = document.getElementById('modal')
// const inputs = document.querySelectorAll('input')

// datatable_clientes.addEventListener('click', (e) => {
// 	e.stopPropagation();
// 	console.log(e.target.parentElement.parentElement.children[6])
// 	console.log(e.target.parentElement.parentElement)
// 	console.log(e.target.parentElement)
// 	console.log(e.target)
// 	let data = e.target.parentElement.parentElement.children;
// 	fillData(data)
// })

// const fillData = (data) => {
// 	for (let index of inputs) {
// 		console.log(data)
// 	}
// }

const dataTableOptions = {
	scrollX: "1000px",
	columnsDefs: [
		{ className: "centered", targets: [0, 1, 2, 3, 4, 5, 6] },
		{ orderable: false, targets: [0, 7,] },
		{ visible: true, targets: [0, 2, 3] },
		{ with: "50%", targets: [0, 1] }
	],
	lengthMenu: [5, 10, 25, 50, 75],
	pagelength: 3,
	destroy: true,
	language: {
		lengthMenu: "Mostrar _MENU_ registros por página",
		zerorecords: "Ningun regisro encontrado",
		info: "Mostrar de _START_ a _END_ de un total de _TOTAL_ registros",
		search: "Buscar",
		infoEmpty: "Nungun usuario encontrado",
		infofiltered: "(Filtrado desde _MAX_ registros totales)",
		loandingRecords: "Cargando....",
		paginate: {
			first: "Primero",
			last: "Último",
			next: "Siguiente",
			previous: "Anerior"
		}

	},
};

const initDataTable = async (id) => {
	if (dataTableIsInitialized) {
		dataTable.destroy();
	}
	// await listarClientes(id);
	dataTable = $('#datatable_clientes').DataTable(dataTableOptions);
	dataTableIsInitialized = true;
};


let ciudades = [];
const listarPaises = async () => {
	try {
		const response = await fetch("paises");
		const data = await response.json();
		console.log(data);
		if (data.message == "Success") {
			// let opciones = '';
			let opciones = `<option value=''>---</option>`;
			data.paises.forEach((pais) => {
				opciones += `<option value='${pais.id}'>${pais.nombre} </option>`;
			});
			cboPais.innerHTML = opciones;
			listarCiudades(data.paises[0].id)
			opciones = `<option value=''>--</option>`;
			cboZona.innerHTML = opciones;

		} else {
			alert("Paises no encontrados...");
		}
	} catch (error) {
		console.log(error)
	}
};

const listarCiudades = async (idpais) => {
	try {
		const response = await fetch(`ciudades/${idpais}`);
		const data = await response.json();
		console.log(data);
		if (data.message == "Success") {
			ciudades = data.ciudades;
			let opciones = `<option value=''>---</option>`;
			data.ciudades.forEach((ciudad) => {
				opciones += `<option value='${ciudad.id}'>${ciudad.nombre} </option>`;
			});
			cboCiudad.innerHTML = opciones;
		} else {
			opciones = '';
			txtNombre.innerHTML = opciones = '';
			cboCiudad.innerHTML = opciones;
			console.log("ciudad no encontradas...");
		}
	} catch (error) {
		console.log(error)
	}
};
// let ciudadEncontrada = ciudades.filter((ciudad) => ciudad.id == idCiudad)[0];
// console.log(ciudadEncontrada);
// let nombre = ciudadEncontrada.id;
// txtNombre.innerHTML = `Extension: ${nombre}`;

const listarZonas = async (idciudad) => {
	try {
		const response = await fetch(`zonas/${idciudad}`);
		const data = await response.json();
		console.log(data);
		console.log("click ciudad")
		if (data.message == "Success") {
			zonas = data.zonas;
			let opciones = `<option value=''>---</option>`;
			data.zonas.forEach((zona) => {
				opciones += `<option value='${zona.id}'>${zona.zona} </option>`;
			});
			cboZona.innerHTML = opciones;
		} else {
			let opciones = `<option value=''>---</option>`;
			cboZona.innerHTML = opciones;
			console.log("zona no encontrada");
		}
	} catch (error) {
		console.log(error)
	}
};


const public = async (id) => {
	try {
		const response = await fetch(`get_publicaciones/${id}`);
		const data = await response.json();
		console.log(data);
		console.log(id);
		let content = "";
		if (data.message == "Success") {
			console.log(data);
			let params = `scrollbars=yes,resizable=yes,status=yes,location=yes,toolbar=yes,menubar=yes,
							width=0,height=0,left=-1000,top=-1000`;
			open(`publiCliente/${id}`, "test", params);
		} else {
			alert("Material no encontrados...");
			console.log("Material no encontrados...");
		}
	} catch (error) {
		console.log(error)
	}
};


const listarClientes = async (id) => {
	try {
		console.log("id localidad")

		const response = await fetch(`clientes/${id}`);
		const data = await response.json();
		console.log(data);
		let content = "";
		if (data.message == "Success") {
			data.clientes.forEach((clientes, index) => {
				content += ` 
				<tr>				
					<td>
						 <img src="${clientes.logo_raw}" style="height:100px;">    
					</td>	
					<td>${clientes.nombre}</td>
					<td>${clientes.direccion}</td>
					<td>${clientes.telefono}</td>
					<td>${clientes.email}</td>
					<td>${clientes.pais}</td>
					<td>${clientes.ciudad}</td>
					<td>${clientes.zona}</td>
					<td>${clientes.id}</td>
					<td><button class="btn btn-Secundary" onclick="public(${clientes.id})"> Detalle </button></td>
				</tr>
			`;
			});
			console.log("Clientes encontrados...");
		} else {
			console.log("Clientes no encontrados...");
		}
		tableBody_clientes.innerHTML = content;
	} catch (error) {
		console.log(error)
	}
};



const listarClientesCiudad = async (idciudad) => {
	try {
		console.log("id Clientes Ciudad")
		console.log(idciudad)
		const response = await fetch(`clientesCiudad/${idciudad}`);
		const data = await response.json();
		console.log(data);
		let content = "";
		if (data.message == "Success") {
			data.clientesCiudad.forEach((clientesCiudad, index) => {
				content += ` 
				<tr>				
					<td>
						 <img src="${clientesCiudad.logo_raw}" style="height:100px;">    
					</td>	
					<td>${clientesCiudad.nombre}</td>
					<td>${clientesCiudad.direccion}</td>
					<td>${clientesCiudad.telefono}</td>
					<td>${clientesCiudad.email}</td>
					<td>${clientesCiudad.pais}</td>
					<td>${clientesCiudad.ciudad}</td>
					<td>${clientesCiudad.zona}</td>
					<td>${clientesCiudad.id}</td>
					<td><button class="btn btn-Secundary" onclick="public(${clientesCiudad.id})"> Detalle </button></td>
				</tr>
			`;
			});
			console.log("Clientes encontrados...");
		} else {
			console.log("Clientes no encontrados...");
		}
		tableBody_clientes.innerHTML = content;
	} catch (error) {
		console.log("Error Cliente Ciudad")
		console.log(idciudad)
		console.log(error)
	}
};



const listarClientesPais = async (idpais) => {
	try {
		console.log("id pais")
		console.log(idpais)
		const response = await fetch(`clientesPais/${idpais}`);
		const data = await response.json();
		console.log("datos de pais")
		console.log(data);
		let content = "";
		if (data.message == "Success") {
			data.clientesPais.forEach((clientesPais, index) => {
				content += ` 
				<tr>				
					<td>
						 <img src="${clientesPais.logo_raw}" style="height:100px;">    
					</td>	
					<td>${clientesPais.nombre}</td>
					<td>${clientesPais.direccion}</td>
					<td>${clientesPais.telefono}</td>
					<td>${clientesPais.email}</td>
					<td>${clientesPais.pais}</td>
					<td>${clientesPais.ciudad}</td>
					<td>${clientesPais.zona}</td>
					<td>${clientesPais.id}</td>
					<td><button class="btn btn-Secundary" onclick="public(${clientesPais.id})"> Detalle </button></td>
				</tr>
			`;
			});
			console.log("Clientes encontrados...");
		} else {
			console.log("Clientes no encontrados...");
		}
		tableBody_clientes.innerHTML = content;
	} catch (error) {
		console.log("Error Cliente pais")
		console.log(error)
	}
};



// <td><button class="btn btn-warning" onclick="public(${clientes.id})"> edit </button></td>
// <i class="bi-search"></i>


const cargaInicial = async () => {
	await listarPaises();

	cboPais.addEventListener("change", (event) => {
		console.log(event.target.value);
		xid_pais = (event.target.value);
		listarCiudades(event.target.value);
		listarClientesPais(event.target.value);
		let opciones = `<option value=''>---</option>`;
		cboZona.innerHTML = opciones;
	});

	cboCiudad.addEventListener("change", (event) => {
		console.log(event.target.value);
		if (event.target.value == "") {
			console.log(xid_pais);
			let opciones = `<option value=''>---</option>`;
			cboZona.innerHTML = opciones;
			initDataTable(event.target.value);
			listarClientesPais(xid_pais);
		} else {
			xid_ciudad = (event.target.value);
			initDataTable(event.target.value);
			listarClientesCiudad(event.target.value);
			listarZonas(event.target.value);
		}
	});

	cboZona.addEventListener("change", (event) => {
		console.log(event.target.value);
		if (event.target.value == "") {
			console.log(xid_ciudad);
			initDataTable(event.target.value);
			listarClientesCiudad(xid_ciudad);
		} else {
			initDataTable(event.target.value);
			listarClientes(event.target.value);
		}
	});
}

// inicio
window.addEventListener("load", async () => {
	await cargaInicial();
});





