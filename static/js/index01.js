let ciudades = [];
const listarPaises = async () => {
	try {
		const response = await fetch("paises");
		const data = await response.json();
		console.log(data);
		if (data.message == "Success") {
			let opciones = '';
			data.paises.forEach((pais) => {
				opciones += `<option value='${pais.id}'>${pais.nombre} </option>`;
			});
			cboPais.innerHTML = opciones;
			listarCiudades(data.paises[0].id);
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
			let opciones = `<option value=''>--</option>`;
			data.ciudades.forEach((ciudad) => {
				opciones += `<option value='${ciudad.id}'>${ciudad.nombre} </option>`;
			});
			cboCiudad.innerHTML = opciones;
			console.log(opciones);

			// listarZonas(data.ciudades[0].id)
			listarZonas(data.ciudades.id)
			// initDataTable(data.ciudades[0].id);
		} else {
			opciones = '';
			txtNombre.innerHTML = opciones = '';
			cboCiudad.innerHTML = opciones;
			console.log("ciudad no encontradas...XXXX");
		}
	} catch (error) {
		console.log(error)
	}
};

const listarZonas = async (idciudad) => {
	try {
		if (idciudad == '') {
			let opciones = `<option value=''>--</option>`;
			cboZona.innerHTML = opciones;
		} else {			
			const response = await fetch(`zonas/${idciudad}`);
			const data = await response.json();
			console.log(data);
			if (data.message == "Success") {
				zonas = data.zonas;
				let opciones = `<option value=''>--</option>`;
				data.zonas.forEach((zona) => {
					opciones += `<option value='${zona.id}'>${zona.zona} </option>`;
				});
				cboZona.innerHTML = opciones;
			} else {
				let opciones = `<option value=''>--</option>`;
				cboZona.innerHTML = opciones;
				console.log("zona no encontrada");
			}
		}
	} catch (error) {
		console.log(error)
	}


};

const cargaInicial = async () => {
	await listarPaises();
	cboPais.addEventListener("change", (event) => {
		console.log(event.target.value);
		listarCiudades(event.target.value);
		let opciones = `<option value=''>--</option>`;
		cboZona.innerHTML = opciones;
	});

	cboCiudad.addEventListener("change", (event) => {
		console.log(event.target.value);
		listarZonas(event.target.value);
		// initDataTable(event.target.value);
	});
}
// inicio
window.addEventListener("load", async () => {
	await cargaInicial();
});

