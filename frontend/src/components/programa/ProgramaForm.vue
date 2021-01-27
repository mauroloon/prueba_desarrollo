<template>
  <form @submit.prevent="submitForm">
    <div class="form-control" :class="{ invalid: !fechaInicio.isValid }">
      <label for="fechaInicio">Fecha inicio </label>
      <input
        type="datetime-local"
        id="fechaInicio"
        v-model="fechaInicio.val"
        @blur="limpiarValidacion('fechaInicio')"
        @change="validarFechas"
      />
      <p v-if="!fechaInicio.isValid">La fecha de inicio no debe ir vacío.</p>
    </div>

    <div class="form-control" :class="{ invalid: !fechaTermino.isValid }">
      <label for="fechaTermino">Fecha llegada </label>
      <input
        type="datetime-local"
        id="fechaTermino"
        v-model="fechaTermino.val"
        @blur="limpiarValidacion('fechaTermino')"
        @change="validarFechas"
      />
      <p v-if="!fechaTermino.isValid">La fecha de llegada no debe ir vacío.</p>
    </div>

    <div class="form-control" :class="{ invalid: !busId.isValid }">
      <label for="busId">Bus </label>
      <select
        class="form-select"
        id="busId"
        v-model="busId.val"
        @blur="limpiarValidacion('busId')"
      >
        <option value="-1" selected> Seleccionar </option>
        <option v-for="bus in buses" :key="bus.id" :value="bus.id">
          {{ bus.marca }} - {{ bus.modelo }}
        </option>
      </select>
      <p v-if="!busId.isValid">El bus es obligatorio.</p>
    </div>

    <div class="form-control" :class="{ invalid: !choferId.isValid }">
      <label for="choferId">Chofer</label>
      <select
        class="form-select"
        id="choferId"
        v-model="choferId.val"
        @blur="limpiarValidacion('choferId')"
      >
        <option value="-1" selected> Seleccionar </option>
        <option v-for="chofer in choferes" :key="chofer.id" :value="chofer.id">
          {{ chofer.nombre }} {{ chofer.apellido }}
        </option>
      </select>
      <p v-if="!choferId.isValid">El chofer es obligatorio.</p>
    </div>

    <div class="form-control" :class="{ invalid: !trayectoId.isValid }">
      <label for="trayectoId">Trayecto</label>
      <select
        class="form-select"
        id="trayectoId"
        v-model="trayectoId.val"
        @blur="limpiarValidacion('trayectoId')"
      >
        <option value="-1" selected> Seleccionar </option>
        <option
          v-for="trayecto in trayectos"
          :key="trayecto.id"
          :value="trayecto.id"
        >
          Desde: {{ trayecto.origen }}, hasta: {{ trayecto.destino }}
        </option>
      </select>
      <p v-if="!trayectoId.isValid">El trayecto es obligatorio.</p>
    </div>

    <div class="form-control" v-if="modoEdit">
      <label for="modelo">Estado</label>
      <select
        class="form-select"
        v-model="estado.val"
        @blur="limpiarValidacion('estado')"
      >
        <option
          v-for="estado in estados"
          :key="estado.EST_ID"
          :value="estado.EST_ID"
        >
          {{ estado.EST_NOMBRE }}
        </option>
      </select>
    </div>

    <div class="form-control" v-if="modoEdit">
      <label for="modelo">Vigente</label>
      <select
        class="form-select"
        v-model="vigencia.val"
        @blur="limpiarValidacion('vigencia')"
      >
        <option value="1"> Si </option>
        <option value="0"> No </option>
      </select>
    </div>
    <p v-if="!formValido">Favor completar el formulario y subir nuevamente.</p>
    <base-button v-if="!modoEdit">Registrar</base-button>
    <base-button v-else>Editar</base-button>
  </form>
</template>

<script>
import moment from "moment";
export default {
  emits: ["guardar", "editar"],
  data() {
    return {
      idPrograma: "",
      fechaInicio: {
        val: "",
        isValid: true
      },
      fechaTermino: {
        val: "",
        isValid: true
      },
      busId: {
        val: "-1",
        isValid: true
      },
      choferId: {
        val: "-1",
        isValid: true
      },
      trayectoId: {
        val: "-1",
        isValid: true
      },
      estado: {
        val: "-1",
        isValid: true
      },
      vigencia: {
        val: "-1",
        isValid: true
      },
      estados: [],
      formValido: true,
      modoEdit: false
    };
  },
  computed: {
    buses() {
      const buses = this.$store.getters["buses/buses"].filter(
        element => element.vigencia == 1
      );

      return buses;
    },
    choferes() {
      const choferes = this.$store.getters["choferes/choferes"].filter(
        element => element.vigencia == 1
      );
      return choferes;
    },
    trayectos() {
      const trayectos = this.$store.getters["trayectos/trayectos"].filter(
        element => element.vigencia == 1
      );
      return trayectos;
    }
  },
  created() {
    this.cargaBuses();
    this.cargarChoferes();
    this.cargarTrayectos();
    this.cargarEstados();
    if (this.$route.params.id) {
      this.modoEdit = true;
      this.idPrograma = this.$route.params.id;
      this.cargarPrograma();
    }
  },
  methods: {
    validoForm() {
      this.formValido = true;
      if (this.fechaInicio.val === "") {
        this.fechaInicio.isValid = false;
        this.formValido = false;
      }
      if (this.fechaTermino.val === "") {
        this.fechaTermino.isValid = false;
        this.formValido = false;
      }
      if (this.busId.val === "-1") {
        this.busId.isValid = false;
        this.formIsValid = false;
      }
      if (this.choferId.val === "-1") {
        this.choferId.isValid = false;
        this.formIsValid = false;
      }
      if (this.trayectoId.val === "-1") {
        this.trayectoId.isValid = false;
        this.formIsValid = false;
      }
    },
    limpiarValidacion(input) {
      this[input].isValid = true;
    },
    submitForm() {
      this.validoForm();

      if (!this.formValido) {
        return;
      }

      var fechaInicioFormat = moment(String(this.fechaInicio.val)).format(
        "YYYY-MM-DD HH:mm"
      );
      var fechaTerminoFormat = moment(String(this.fechaTermino.val)).format(
        "YYYY-MM-DD HH:mm"
      );

      var formData = {};
      if (this.modoEdit) {
        formData = {
          id: this.idPrograma,
          fechaInicio: fechaInicioFormat,
          fechaTermino: fechaTerminoFormat,
          busId: this.busId.val,
          choferId: this.choferId.val,
          trayectoId: this.trayectoId.val,
          estado: this.estado.val,
          vigencia: this.vigencia.val
        };
        this.$emit("editar", formData);
      } else {
        formData = {
          fechaInicio: fechaInicioFormat,
          fechaTermino: fechaTerminoFormat,
          busId: this.busId.val,
          choferId: this.choferId.val,
          trayectoId: this.trayectoId.val
        };
        this.$emit("guardar", formData);
      }
    },
    async cargaBuses() {
      //TODO: CARGAR BUSES DISPONIBLES DPS/ ruta finalizada y/o en fecha
      this.isLoading = true;
      try {
        await this.$store.dispatch("buses/cargaBuses");
      } catch (error) {
        console.log(error);
      }
      this.isLoading = false;
    },
    async cargarChoferes() {
      //TODO: CARGAR choferes DISPONIBLES DPS/ ruta finalizada y/o en fecha
      this.isLoading = true;
      try {
        await this.$store.dispatch("choferes/cargarChoferes");
      } catch (error) {
        console.log(error);
      }
      this.isLoading = false;
    },
    async cargarTrayectos() {
      this.isLoading = true;
      try {
        await this.$store.dispatch("trayectos/cargaTrayectos");
      } catch (error) {
        console.log(error);
      }
      this.isLoading = false;
    },
    async cargarPrograma() {
      const response = await fetch(
        `http://localhost:8000/v1/bus/reserva/${this.idPrograma}/`
      );
      const responseData = await response.json();

      if (responseData.code == 1) {
        this.fechaInicio.val = moment(responseData.data.FDT_DIA_INICIO).format(
          "YYYY-MM-DD[T]HH:mm"
        );
        this.fechaTermino.val = moment(
          responseData.data.FDT_DIA_LLEGADA
        ).format("YYYY-MM-DD[T]HH:mm");
        this.busId.val = responseData.data.BUS_ID.BUS_ID;
        this.choferId.val = responseData.data.CFR_ID.CFR_ID;
        this.trayectoId.val = responseData.data.TYO_ID.TYO_ID;
        this.estado.val = responseData.data.EST_ID.EST_ID;
        this.vigencia.val = responseData.data.RSV_VIGENCIA;
      }
    },
    async cargarEstados() {
      const response = await fetch(`http://localhost:8000/v1/bus/estados/`);
      const responseData = await response.json();

      if (responseData.code == 1) {
        this.estados = responseData.data;
      }
    },
    validarFechas() {
      if (this.fechaInicio.val !== "" && this.fechaTermino.val !== "") {
        /* en caso de que la fecha de inicio sea mayor a la de termino, se borra la de termino */
        if (moment(this.fechaInicio.val).isAfter(this.fechaTermino.val)) {
          this.fechaTermino.val = "";
        }
      }
    }
  }
};
</script>

<style scoped>
.form-control {
  margin: 0.5rem 0;
}

.form-select {
  display: block;
  width: 100%;
  height: 34px;
  padding: 6px 12px;
  font-size: 14px;
  color: #555;
  background-color: #fff;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}

label {
  font-weight: bold;
  display: block;
  margin-bottom: 0.5rem;
}

input[type="checkbox"] + label {
  font-weight: normal;
  display: inline;
  margin: 0 0 0 0.5rem;
}

input,
textarea {
  display: block;
  width: 100%;
  border: 1px solid #ccc;
  font: inherit;
}

input:focus,
textarea:focus {
  background-color: #f0e6fd;
  outline: none;
  border-color: #c1c0c4;
}

input[type="checkbox"] {
  display: inline;
  width: auto;
  border: none;
}

input[type="checkbox"]:focus {
  outline: #b8b6bb solid 1px;
}

h3 {
  margin: 0.5rem 0;
  font-size: 1rem;
}

.invalid label {
  color: red;
}

.invalid input,
.invalid textarea {
  border: 1px solid red;
}
</style>
