export default {
  async cargarChoferes(context) {
    const response = await fetch(`http://127.0.0.1:8000/v1/bus/chofer/`);
    const responseData = await response.json();

    const choferes = [];

    if (responseData.code === 1) {
      responseData.data.forEach(element => {
        const chofer = {
          id: element.CFR_ID,
          nombre: element.CFR_NOMBRE,
          apellido: element.CFR_APELLIDO,
          rut: element.CFR_RUT,
          lugar: element.LGR_ID,
          vigencia: element.CFR_VIGENCIA
        };
        choferes.push(chofer);
      });
    }

    context.commit("setChoferes", choferes);
  },
  async agregarChofer(_,payload) {
    var formData = new FormData();
    formData.append("lugarId", payload.lugar);
    formData.append("nombre", payload.nombre);
    formData.append("apellido", payload.apellido);
    formData.append("rut", payload.rut);

    const response = await fetch(`http://127.0.0.1:8000/v1/bus/chofer/`, {
      body: formData,
      method: "POST"
    });
    const responseData = await response.json();

    if (responseData.code === 1) {
      console.log("Chofer agregado.");
    }
  },
  async editarChofer(_, payload) {
    var formData = new FormData();
    formData.append("lugarId", payload.lugar);
    formData.append("nombre", payload.nombre);
    formData.append("apellido", payload.apellido);
    formData.append("rut", payload.rut);
    formData.append("vigencia", payload.vigencia);

    const response = await fetch(
      `http://127.0.0.1:8000/v1/bus/chofer/${payload.id}/`,
      {
        body: formData,
        method: "PUT"
      }
    );
    const responseData = await response.json();

    if (responseData.code === 1) {
      console.log("Chofer actualizado");
    }
  },
  async deshabilitarChofer(_, payload) {
    const response = await fetch(
      `http://127.0.0.1:8000/v1/bus/chofer/${payload}/`,
      {
        method: "DELETE"
      }
    );
    const responseData = await response.json();

    if (responseData.code === 1) {
      console.log("bus deshabilitado");
    }
  },
};
