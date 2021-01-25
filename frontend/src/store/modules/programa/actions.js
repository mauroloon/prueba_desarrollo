export default {
  async cargarPrograma(context) {
    const response = await fetch(`http://127.0.0.1:8000/v1/bus/reserva/`);
    const responseData = await response.json();

    const programas = [];

    if (responseData.code === 1) {
      responseData.data.forEach(element => {
        const programa = {
          id: element.RSV_ID,
          trayecto:
            element.TYO_ID.nombre_origen +
            " - " +
            element.TYO_ID.nombre_destino,
          fechaInicio: element.FDT_DIA_INICIO,
          fechaTermino: element.FDT_DIA_LLEGADA,
          bus: element.BUS_ID.BUS_MARCA + " " + element.BUS_ID.BUS_MODELO,
          chofer: element.CFR_ID.CFR_NOMBRE + " " + element.CFR_ID.CFR_APELLIDO,
          estado: element.EST_ID.EST_NOMBRE,
          vigencia: element.RSV_VIGENCIA
        };
        programas.push(programa);
      });
    }

    context.commit("setProgramas", programas);
  },
  async agregarPrograma(_, payload) {
    var formData = new FormData();
    formData.append("fechaInicio", payload.fechaInicio);
    formData.append("fechaLlegada", payload.fechaTermino);
    formData.append("busId", payload.busId);
    formData.append("choferId", payload.choferId);
    formData.append("trayectoId", payload.trayectoId);

    const response = await fetch(`http://127.0.0.1:8000/v1/bus/reserva/`, {
      body: formData,
      method: "POST"
    });
    const responseData = await response.json();

    if (responseData.code === 1) {
      console.log("Programa agregado.");
    }
  },
  async editarPrograma(_, payload) {
    var formData = new FormData();
    formData.append("fechaInicio", payload.fechaInicio);
    formData.append("fechaLlegada", payload.fechaTermino);
    formData.append("busId", payload.busId);
    formData.append("choferId", payload.choferId);
    formData.append("trayectoId", payload.trayectoId);
    formData.append("estado", payload.estado);
    formData.append("vigencia", payload.vigencia);

    const response = await fetch(
      `http://127.0.0.1:8000/v1/bus/reserva/${payload.id}/`,
      {
        body: formData,
        method: "PUT"
      }
    );
    const responseData = await response.json();

    if (responseData.code === 1) {
      console.log("Programa actualizado.");
    }
  },
  async deshabilitarPrograma(_, payload) {
    const response = await fetch(
      `http://127.0.0.1:8000/v1/bus/reserva/${payload}/`,
      {
        method: "DELETE"
      }
    );
    const responseData = await response.json();

    if (responseData.code === 1) {
      console.log("Programa deshabilitado");
    }
  },
  async agregarPasajero(_, payload) {
    var formData = new FormData();
    formData.append("nombre", payload.nombre);
    formData.append("apellido", payload.apellido);
    formData.append("rut", payload.rut);
    formData.append("nReserva", payload.nReserva);
    formData.append("reservaId", payload.reservaId);

    const response = await fetch(`http://127.0.0.1:8000/v1/bus/pasajero/`, {
      body: formData,
      method: "POST"
    });
    const responseData = await response.json();

    if (responseData.code === 1) {
      console.log("Pasajero agregado.");
    }
  },
  async cargarPasajeros(context, payload) {
    const response = await fetch(
      `http://127.0.0.1:8000/v1/bus/reserva/${payload}/pasajero/`
    );
    const responseData = await response.json();

    const pasajeros = [];

    if (responseData.code === 1) {
      responseData.data.forEach(element => {
        const pasajero = {
          id: element.PSR_ID,
          nombre: element.PRS_ID.PRS_NOMBRE,
          apellido: element.PRS_ID.PRS_APELLIDO,
          rut: element.PRS_ID.PRS_RUT,
          nReserva: element.PSR_N_RESERVA
        };
        pasajeros.push(pasajero);
      });
    }

    context.commit("setPasajeros", pasajeros);
  },
  async deshabilitarPasajero(_, payload) {
    const response = await fetch(
      `http://127.0.0.1:8000/v1/bus/pasajero/${payload}/`,
      {
        method: "DELETE"
      }
    );
    const responseData = await response.json();

    if (responseData.code === 1) {
      console.log("Pasajero deshabilitado");
    }
  },
  async editarPasajero(_, payload) {
    var formData = new FormData();
    formData.append("nombre", payload.nombre);
    formData.append("apellido", payload.apellido);
    formData.append("nReserva", payload.nReserva);
    formData.append("choferId", payload.reservaId);

    const response = await fetch(
      `http://127.0.0.1:8000/v1/bus/pasajero/${payload.id}/`,
      {
        body: formData,
        method: "PUT"
      }
    );
    const responseData = await response.json();

    if (responseData.code === 1) {
      console.log("Acción actualizado.");
    }
  }
};
