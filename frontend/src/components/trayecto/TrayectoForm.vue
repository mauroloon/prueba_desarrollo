<template>
  <form @submit.prevent="submitForm">
    <div class="form-control" :class="{ invalid: !inicio.isValid }">
      <label for="inicio">Inicio </label>
      <select
        class="form-select"
        id="inicio"
        v-model="inicio.val"
        @blur="limpiarValidacion('inicio')"
      >
        <option value="-1" selected> Seleccionar </option>
        <option v-for="lugar in lugares" :key="lugar.id" :value="lugar.id">
          {{ lugar.nombre }}
        </option>
      </select>
      <p v-if="!inicio.isValid">La ubicación es obligatoria.</p>
    </div>

    <div class="form-control" :class="{ invalid: !destino.isValid }">
      <label for="destino">Destino </label>
      <select
        class="form-select"
        id="destino"
        v-model="destino.val"
        @blur="limpiarValidacion('destino')"
      >
        <option value="-1" selected> Seleccionar </option>
        <option v-for="lugar in lugares" :key="lugar.id" :value="lugar.id">
          {{ lugar.nombre }}
        </option>
      </select>
      <p v-if="!destino.isValid">La ubicación es obligatoria.</p>
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
export default {
  emits: ["guardar", "editar"],
  data() {
    return {
      idTrayecto: "",
      inicio: {
        val: "-1",
        isValid: true
      },
      destino: {
        val: "-1",
        isValid: true
      },
      vigencia: {
        val: "-1",
        isValid: true
      },
      formValido: true,
      modoEdit: false
    };
  },
  computed: {
    lugares() {
      return this.$store.getters["buses/lugares"];
    }
  },
  created() {
    this.cargarLugares();
    if (this.$route.params.id) {
      this.modoEdit = true;
      this.idTrayecto = this.$route.params.id;
      this.cargarTrayecto();
    }
  },
  methods: {
    validarForm() {
      this.formValido = true;
      if (this.inicio.val === "-1") {
        this.inicio.isValid = false;
        this.formIsValid = false;
      }
      if (this.destino.val === "-1") {
        this.destino.isValid = false;
        this.formIsValid = false;
      }
    },
    limpiarValidacion(input) {
      this[input].isValid = true;
    },
    submitForm() {
      this.validarForm();

      if (!this.formValido) {
        return;
      }

      var formData = {};

      if (this.modoEdit) {
        formData = {
          id: this.idTrayecto,
          lugarIdInicial: this.inicio.val,
          lugarIdFinal: this.destino.val,
          vigencia: this.vigencia.val
        };
        this.$emit("editar", formData);
      } else {
        formData = {
          lugarIdInicial: this.inicio.val,
          lugarIdFinal: this.destino.val
        };
        this.$emit("guardar", formData);
      }
    },
    async cargarLugares() {
      try {
        await this.$store.dispatch("buses/cargarLugares");
      } catch (error) {
        console.log(error);
      }
    },
    async cargarTrayecto() {
      const response = await fetch(
        `http://localhost:8000/v1/bus/trayecto/${this.idTrayecto}/`
      );
      const responseData = await response.json();

      if (responseData.code == 1) {
        this.inicio.val = responseData.data.LGR_ID_INICIO;
        this.destino.val = responseData.data.LGR_ID_TERMINO;
        this.vigencia.val = responseData.data.TYO_VIGENCIA;
      }
    }
  }
};
</script>

<style scoped>
.form-control {
  margin: 0.5rem 0;
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
</style>
