export default {
  async cargaTrayectos(context) {
    const response = await fetch(`http://127.0.0.1:8000/v1/bus/trayecto/`);
    const responseData = await response.json();

    const trayectos = [];

    if (responseData.code === 1) {
      responseData.data.forEach(element => {
        const trayecto = {
          id: element.TYO_ID,
          trayectoInicial: element.LGR_ID_INICIO,
          trayectoFinal: element.LGR_ID_TERMINO,
          vigencia: element.TYO_VIGENCIA,
          origen: element.nombre_origen,
          destino: element.nombre_destino,
          promedio: element.promedio
        };
        trayectos.push(trayecto);
      });
    }

    context.commit("setTrayectos", trayectos);
  },
  async agregarTrayecto(_, payload) {
    var formData = new FormData();
    formData.append("lugarInicioId", payload.lugarIdInicial);
    formData.append("lugarTerminoId", payload.lugarIdFinal);

    const response = await fetch(`http://127.0.0.1:8000/v1/bus/trayecto/`, {
      body: formData,
      method: "POST"
    });
    const responseData = await response.json();

    if (responseData.code === 1) {
      console.log("Trayecto agregado.");
    }
  },
  async editarTrayecto(_, payload) {
    var formData = new FormData();
    formData.append("lugarInicioId", payload.lugarIdInicial);
    formData.append("lugarTerminoId", payload.lugarIdFinal);
    formData.append("vigencia", payload.vigencia);

    const response = await fetch(
      `http://127.0.0.1:8000/v1/bus/trayecto/${payload.id}/`,
      {
        body: formData,
        method: "PUT"
      }
    );
    const responseData = await response.json();

    if (responseData.code === 1) {
      console.log("Trayecto actualizado");
    }
  },
  async deshabilitarTrayecto(_, payload) {
    const response = await fetch(
      `http://127.0.0.1:8000/v1/bus/trayecto/${payload}/`,
      {
        method: "DELETE"
      }
    );
    const responseData = await response.json();

    if (responseData.code === 1) {
      console.log("Trayecto deshabilitado");
    }
  }
};
