export default {
  async cargaBuses(context) {
    const response = await fetch(`http://127.0.0.1:8000/v1/bus/bus/`);
    const responseData = await response.json();

    const buses = [];

    if (responseData.code === 1) {
      responseData.data.forEach(element => {
        const bus = {
          id: element.BUS_ID,
          marca: element.BUS_MARCA,
          modelo: element.BUS_MODELO,
          vigencia: element.BUS_VIGENCIA,
          lugar: element.LGR_ID
        };
        buses.push(bus);
      });
    }

    context.commit("setBuses", buses);
  },
  async cargarLugares(context) {
    const response = await fetch(`http://localhost:8000/v1/bus/lugares/`);
    const responseData = await response.json();
    const lugares = [];
    if (responseData.code == 1) {
      responseData.data.forEach(element => {
        const lugar = {
          id: element.LGR_ID,
          nombre: element.LGR_NOMBRE,
          descripcion: element.LGR_DESCRIPCION
        };
        lugares.push(lugar);
      });
    }
    context.commit("setLugares", lugares);
  },
  async deshabilitarBus(_, payload) {
    const response = await fetch(
      `http://127.0.0.1:8000/v1/bus/bus/${payload}/`,
      {
        method: "DELETE"
      }
    );
    const responseData = await response.json();

    if (responseData.code === 1) {
      console.log("bus deshabilitado");
    }
  },
  async agregarBus(_, payload) {
    var formData = new FormData();
    formData.append("lugarId", payload.lugar);
    formData.append("marca", payload.marca);
    formData.append("modelo", payload.modelo);

    const response = await fetch(`http://127.0.0.1:8000/v1/bus/bus/`, {
      body: formData,
      method: "POST"
    });
    const responseData = await response.json();

    if (responseData.code === 1) {
      console.log("bus agregado");
    }
  },
  async editarBus(_, payload) {
    var formData = new FormData();
    formData.append("lugarId", payload.lugar);
    formData.append("marca", payload.marca);
    formData.append("modelo", payload.modelo);
    formData.append("vigencia", payload.vigencia);

    const response = await fetch(
      `http://127.0.0.1:8000/v1/bus/bus/${payload.id}/`,
      {
        body: formData,
        method: "PUT"
      }
    );
    const responseData = await response.json();

    if (responseData.code === 1) {
      console.log("bus actualizado");
    }
  }
};
